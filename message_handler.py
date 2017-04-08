#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# OrariSTP bot
#
# A Telegram Bot that provides times and stops for STP Brindisi
# 2016-2017
# Peppuz Elativ <peppuzvitale@gmail.com>
#

""" This module handles the sequence from MENU to TIME - STOP is a callback  """

import Tastiere
import telegram
import SQL
from start_me import *
from telegram import Emoji as e
from telegram import ReplyKeyboardMarkup as RKM
from telegram import InlineKeyboardMarkup as MK
from telegram import InlineKeyboardButton as BK

(
    MENU, # 0
    CERCO,# 1
    DEST, # 2
    TIME, # 3
    STOP,
    MAPPA,
    CHI_SIAMO,
    FACEBOOK,
    INSTAGRAM,
    TWITTER,
    ) = range(10)

status = dict()
partenza = dict()
destinazione = dict()
orario = dict()

def messagehandler(b, u):
    m = u.message
    usr = m.from_user
    usr_stat = status.get(usr.id, MENU)
    txt = m.text
    citta = SQL.get_citta()

    if usr_stat == MENU:

        # "Sei sul menu principale, devi scegliere"

        if txt == e.BUS.decode('utf-8') + ' Cerca bus ' \
            + e.BUS.decode('utf-8'):
            status[usr.id] = CERCO
            b.sendMessage(m.chat_id, text='Scegli il paese di partenza '
                           + e.BUS, reply_markup=Tastiere.start())
        elif txt in citta:
            partenza[usr.id] = txt
            b.sendMessage(m.chat_id, text=txt + ' --> '
                          + '\n Dove vuoi andare?',
                          reply_markup=Tastiere.fermate(txt))
        elif txt == 'Chi siamo' + e.BUS_STOP.decode('utf-8'):

            status[usr.id] = MENU
            print usr_stat
            message = 'Sono @Peppu, creatore del bot.\nAltri membri de SVDevTeam:\nManuel Manelli - @Vorpal97\nAlberto Carrone - @albertocrrn'
            b.sendMessage(m.chat_id, message,
                          reply_markup=Tastiere.menu())
        elif txt == 'Facebook' + e.MOBILE_PHONE.decode('utf-8'):

            status[usr.id] = MENU
            message = 'fb.com/oraristp'
            b.sendMessage(m.chat_id, message,
                          reply_markup=Tastiere.menu())
        elif txt == 'Twitter' + e.BIRD.decode('utf-8'):

            status[usr.id] = MENU
            message = 'http://twitter.com/svdevteam'
            b.sendMessage(m.chat_id, message,
                          reply_markup=Tastiere.menu())
        elif txt == 'Instagram' + e.CAMERA.decode('utf-8'):

            status[usr.id] = MENU
            message = 'http://instagram.com/explore/tags/oraristp/'
            b.sendMessage(m.chat_id, message,
                          reply_markup=Tastiere.menu())
        else:
            b.sendMessage(m.chat_id, "Non credo esista in provincia di Brindisi, prova tra quelle nella tastiera. ")

    elif usr_stat == CERCO:

        # qui si modula la citta ricevuta

        if txt in citta:
            partenza[usr.id] = txt
            status[usr.id] = DEST
            message = "Da " + txt + " --> " \
                + "\n Scegli la citta di arrivo:"
            b.sendMessage(m.chat_id, message,
                          reply_markup=Tastiere.dest(str(txt)))
        elif txt not in citta:

            b.sendMessage(m.chat_id,
                          'Non credo esista in provincia di Brindisi, prova tra quelle nella tastiera.',
                          reply_markup=Tastiere.start())

    elif usr_stat == DEST:

        # invio destinazioni
        dest = SQL.get_destinazioni(partenza[usr.id])
        if txt in dest:
					status[usr.id] = TIME
					destinazione[usr.id] = txt
					message = 'Tutti gli orari in partenza da ' + partenza[usr.id] + ' per ' + txt +' -->'
					b.sendMessage(m.chat_id, message,
												reply_markup=Tastiere.timet(partenza[usr.id],txt))
        else:
					b.sendMessage(m.chat_id, message,
                                                reply_markup=Tastiere.dest(txt))

    elif usr_stat == TIME:

        # dovrebbe funzionare
    	status[usr.id] = STOP
    	destinazione[usr.id] = txt
    	message = e.BUS.decode('utf-8')+' Pullman da '+partenza[usr.id]+' per '+txt+'\n'+e.BUS_STOP.decode('utf-8')\
                                                +' Passanti per ' +destinazione[usr.id]+':\n'
    	for orario in SQL.get_fermate():
    		message += '\n\n'+orario

    	b.sendMessage(m.chat_id, 'Calcolo le fermate...')
    	b.sendMessage(m.chat_id, message, reply_markup=Tastiere.menu())

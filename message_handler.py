#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#This file is part of OrariSTP-bot.
#
# OrariSTP-bot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OrariSTP-bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OrariSTP-bot.  If not, see <http://www.gnu.org/licenses/>
# 2016-2017
# Peppuz Elativ <peppuzvitale@gmail.com>
#

""" This module handles the sequence from MENU to TIME - STOP is a callback  """

import Tastiere
import telegram
import SQL
from start_me import *
from telegram import Emoji as emo
from telegram import ReplyKeyboardMarkup as RKM
from telegram import InlineKeyboardMarkup as MK
from telegram import InlineKeyboardButton as BK
from telegram import ReplyKeyboardHide as hide

# User statuses
(    MENU,
    CERCO,
    DEST,
    TIME,
    STOP,
    MAPPA,
    CHI_SIAMO,
    FACEBOOK,
    INSTAGRAM,
    TWITTER,
    ) = range(10)

# Temporary storage for last user choices
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
        if txt == emo.BUS.decode('utf-8') + ' Cerca bus ' \
            + emo.BUS.decode('utf-8'):
            status[usr.id] = CERCO
            try:
                b.sendMessage(m.chat_id, text='Scegli il paese di partenza '
                               + emo.BUS, reply_markup=Tastiere.start())
            except Exception as e:
                b.sendMessage(m.chat_id, "Errore: %s" % repr(e))

        elif txt in citta:
            partenza[usr.id] = txt
            b.sendMessage(m.chat_id, text=txt + ' --> '
                          + '\n Dove vuoi andare?',
                          reply_markup=Tastiere.fermate(txt))

        elif txt == 'Chi siamo' + emo.BUS_STOP.decode('utf-8'):
            status[usr.id] = MENU
            print usr_stat
            message = 'Sono @Peppu, creatore del bot.\nAltri membri de SVDevTeam:\nManuel Manelli - @Vorpal97\nAlberto Carrone - @albertocrrn'
            b.sendMessage(m.chat_id, message,
                          reply_markup=Tastiere.menu())
        elif txt == 'Facebook' + emo.MOBILE_PHONE.decode('utf-8'):
            status[usr.id] = MENU
            message = 'fb.com/oraristp'
            b.sendMessage(m.chat_id, message,
                          reply_markup=Tastiere.menu())
        elif txt == 'Twitter' + emo.BIRD.decode('utf-8'):
            status[usr.id] = MENU
            message = 'http://twitter.com/svdevteam'
            b.sendMessage(m.chat_id, message,
                          reply_markup=Tastiere.menu())
        elif txt == 'Instagram' + emo.CAMERA.decode('utf-8'):

            status[usr.id] = MENU
            message = 'http://instagram.com/explore/tags/oraristp/'
            b.sendMessage(m.chat_id, message,
                          reply_markup=Tastiere.menu())
        else:
            b.sendMessage(m.chat_id, "Se cercavi una citta di parteza, beh devo avvisarti che questa che mi hai scritto non esiste in Brindisi. ")

    elif usr_stat == CERCO:
        # Bot recieves the departure city, now i check if exist and send arrivals if true, else alert that doesnt exist
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
        # Bot recieves arrival city, check if exist again, than give him the time table
        dest = SQL.get_destinazioni(partenza[usr.id])
        if txt in dest:
            status[usr.id] = TIME
            destinazione[usr.id] = txt
            message = 'Tutti gli orari in partenza da ' + partenza[usr.id] + ' per ' + txt +' -->'
            b.sendMessage(m.chat_id, message, reply_markup=Tastiere.timet(partenza[usr.id],txt))
            b.sendMessage(m.chat_id, "Clicca sull'orario per visualizzare le fermate in %s" % partenza[usr.id] , reply_markup=RKM([['/menu']]))
            # if the city is typed instead and incorrectly, i give him back the last keyboard
        else:
            b.sendMessage(m.chat_id, message,reply_markup=Tastiere.dest(txt))

    elif usr_stat == TIME:
    	status[usr.id] = STOP
    	destinazione[usr.id] = txt
    	message = emo.BUS.decode('utf-8')+' Pullman da '+partenza[usr.id]+' per '+txt+'\n'+emo.BUS_STOP.decode('utf-8')\
                                                +' Passanti per ' +destinazione[usr.id]+':\n'
    	for orario in SQL.get_fermate():
    		message += '\n\n'+orario
    	b.sendMessage(m.chat_id, 'Calcolo le fermatemo...')
    	b.sendMessage(m.chat_id, message, reply_markup=Tastiere.menu())

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# OrariSTP bot
#
# A Telegram Bot that provides times and stops for STP Brindisi
# 2016-2017
# Peppuz Elativ <peppuzvitale@gmail.com>
#

""" This module creates Keyboard Markups to send in different menues """

from telegram import InlineKeyboardMarkup as MK
from telegram import InlineKeyboardButton as B
from telegram import ReplyKeyboardMarkup as RKM
import SQL
from telegram import Emoji as e

def start(): # START
    cities = SQL.get_citta()
    for item in cities:
        print item
    tastiera = [[item] for item in cities]
    return RKM(tastiera, one_time_keyboard=True)

def dest(city): # dest
    fermate = SQL.get_destinazioni(city)
    tastiera = [[item] for item in fermate]
    return RKM(tastiera, one_time_keyboard=True)

def timet(p,d): # time
    data = SQL.get_timetable(p,d)
    kb = []
    for counter in range(len(data['orari'])):
        kb.append( [ B( data['orari'][counter] , callback_data=data['trip_id'][counter]) ])
        print data
    return MK(kb)

def back():
    kb = [[e.BACK_WITH_LEFTWARDS_ARROW_ABOVE]]
    return RKM(kb, one_time_keyboard=True)

def menu():
    keyboard = [[e.BUS + ' Cerca bus ' + e.BUS], ['Chi siamo'
                + e.BUS_STOP], ['Facebook' + e.MOBILE_PHONE, 'Twitter'
                + e.BIRD], ['Instagram' + e.CAMERA]]
    return RKM(keyboard, one_time_keyboard=True)

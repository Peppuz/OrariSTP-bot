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

""" This module creates Keyboard Markups to send in different menues """

from telegram import InlineKeyboardMarkup as MK
from telegram import InlineKeyboardButton as B
from telegram import ReplyKeyboardMarkup as RKM
import SQL
from telegram import Emoji as e

def start():
    try:
        cities = SQL.get_citta()
        for item in cities:
            print item
        tastiera = [[item] for item in cities]
        return RKM(tastiera, one_time_keyboard=True)
    except Exception as e:
        raise Exception(repr(e))

def dest(city): # dest
    fermate = SQL.get_destinazioni(city)
    tastiera = [[item] for item in fermate]
    return RKM(tastiera, one_time_keyboard=True)

def timet(p,d): # time
    # this method returns { orari[] , trip_ids[] , validita[] } all in order
    data = SQL.get_timetable(p,d)
    kb = []

    # appends to the kb array all the buttons one by one (one on top of the other)
    # i used the trip_id as callback_data cause the bus goes in a departure city just once in a trip
    for counter in range(len(data['orari'])):
        kb.append([B(data['orari'][counter] , callback_data=data['trip_id'][counter])])
    return MK(kb)
def menu():
    keyboard = [[e.BUS + ' Cerca bus ' + e.BUS], ['Chi siamo'
                + e.BUS_STOP], ['Facebook' + e.MOBILE_PHONE, 'Twitter'
                + e.BIRD], ['Instagram' + e.CAMERA]]
    return RKM(keyboard, one_time_keyboard=True)

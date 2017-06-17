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

""" This module recieves stop_ids sends the location of the stop """
import message_handler, SQL, Tastiere

def callbacking(b,u):
        query	= u.callback_query
        chat_id	= query.message.chat_id
        usr_id	= query.from_user.id
        txt		= query.data # <= trip_id
        # get user status, if null set to MENU
        usr_stat= message_handler.status.get(usr_id,message_handler.MENU)
        # Store temporary departure and arrival
        p = message_handler.partenza[usr_id]
        d = message_handler.destinazione[usr_id]
        # Request stops with json model
        fermate = SQL.get_fermate(p,d,txt)
        if usr_stat == message_handler.STOP:
            message_handler.status[usr_id] = message_handler.MENU
            message = "Fermate in "+message_handler.partenza[usr_id]+":\n"
            for stop in fermate:
                message += stop + "\n"
            b.sendMessage(chat_id, message, reply_markup=Tastiere.menu())

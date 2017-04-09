#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# OrariSTP bot
#
# A Telegram Bot that provides times and stops for STP Brindisi
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
	if usr_stat == message_handler.TIME:
		message = "Fermate in "+message_handler.partenza[usr_id]+":\n"
		for stop in fermate:
			message += stop + "\n"
		b.sendMessage(chat_id, message, reply_markup=Tastiere.menu())

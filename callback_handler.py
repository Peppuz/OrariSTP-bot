# -*- coding: utf-8 -*-
#
# OrariSTP_bot
#
# A Telegram Bot that provides times and stops from STP Brindisi
# Copyright (C) 2016-2017
# Giuseppe Vitale <peppuzvitale@gmail.com>
#
""" This module recieves stop_ids sends the location of the stop """
import message_handler, SQL



def callbacking(b,u):
	query	= u.callback_query
 	chat_id	= query.message.chat_id
	usr_id	= query.from_user.id
	txt		= query.data # TXT = trip_id
	usr_stat= message_handler.status.get(usr_id,message_handler.MENU)
	p = message_handler.partenza[usr_id]
	d = message_handler.destinazione[usr_id]
	fermate = SQL.get_fermate(p,d,txt)
	# I have to send back the name of the partenza
	print len(fermate)
	print usr_stat
	if usr_stat == message_handler.TIME:
		message = "Fermate in "+message_handler.partenza[usr_id]+":\n"
		for s in fermate[0]:
			message += s + "\n"
		message += "\nFermate in "+message_handler.destinazione[usr_id]+":\n"
		for d in fermate[1]:
			message += d + "\n"
		b.sendMessage(chat_id, message)

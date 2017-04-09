#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# OrariSTP bot
#
# A Telegram Bot that provides times and stops for STP Brindisi
# 2016-2017
# Peppuz Elativ <peppuzvitale@gmail.com>
#

'''####################################################################################################################'''
import telegram, logging, Tastiere, SQL, message_handler, callback_handler
from telegram.ext import (Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler)
from telegram import (Emoji, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram import ReplyKeyboardMarkup as RKM
import credentials
import update as reloaded
'''####################################################################################################################'''
# Settings

bot = telegram.Bot(credentials.token)
updater = Updater(credentials.token)
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%I:%M', level=logging.DEBUG)
confirmed_id = credentials.confirmed_id

'''####################################################################################################################'''
# Defs

def start(b,u): # bot,update data
	m 			= u.message
	usr			= m.from_user
	# setting user status
	message_handler.status[usr.id] = message_handler.MENU
	bot.sendMessage(m.chat_id, text='Ciao '+ usr.first_name+'! Questo è OrariSTP bot.'.decode('utf-8'))
	bot.sendMessage(credentials.Peppuz, usr.first_name+' ha startato')
	# prerelease check
	if int(usr.id) in confirmed_id:
		bot.sendMessage(m.chat_id, text="Iniziamo!", reply_markup=Tastiere.menu())
	else:
		bot.sendMessage(m.chat_id, text='Mi spiace %s, @Peppuz ha detto una cerchia ristretta di utenti, magari chiedi a lui!'% usr.first_name)
	# prerelease reloading
	reloaded.reloaded()
def cancel(b,u):
	m 			= u.message
	usr			= m.from_user
	message_handler.status[usr.id] = message_handler.MENU
	bot.sendMessage(m.chat_id, text='Ok '+ usr.first_name+', torno al menu principale'+Emoji.BUS.decode('utf-8'), reply_markup=Tastiere.menu())

def vai(b,u):
	m 			= u.message
	usr			= m.from_user
	message_handler.status[usr.id] = message_handler.CERCO
	bot.sendMessage(m.chat_id, text='Nuova ricerca! '+Emoji.BUS.decode('utf-8'), reply_markup=Tastiere.start())


def update(b,u):
	m 			= u.message
	usr			= m.from_user
	message = "Platform updated."
	try:
		reloaded.reloaded()
		bot.sendMessage(m.chat_id, text='Platform updated')
	except Exception as e:
		bot.sendMessage(m.chat_id, text='Failed Update'
	print usr.first_name + " updated the script"






'''####################################################################################################################'''
# Just Main


def main():
	ds = updater.dispatcher

	ds.add_handler(CommandHandler('start',start))
	ds.add_handler(CommandHandler('menu',cancel))
	ds.add_handler(CommandHandler('vai', vai))
	ds.add_handler(CommandHandler('update',update))
	ds.add_handler(MessageHandler([Filters.text],message_handler.messagehandler))
	ds.add_handler(CallbackQueryHandler(callback_handler.callbacking))

	updater.start_polling()
'''#-----------------------------------------------------'''
if __name__ == '__main__':
	main()

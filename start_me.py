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
'''####################################################################################################################'''
# Settings

bot = telegram.Bot(credentials.token)
updater = Updater(credentials.token)
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%I:%M', level=logging.DEBUG)

'''####################################################################################################################'''
# Defs

def start(b, u):
	m 			= u.message
	usr			= m.from_user
	message_handler.status[usr.id] = message_handler.MENU
	bot.sendMessage(m.chat_id, text='Ciao '+ usr.first_name+'! Questo è OrariSTP bot.'.decode('utf-8'))
	bot.sendMessage(m.chat_id, text="Iniziamo!", reply_markup=Tastiere.menu())

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


'''####################################################################################################################'''
# Just Main

def main():
	ds = updater.dispatcher

	ds.add_handler(CommandHandler('start',start))
	ds.add_handler(CommandHandler('cancel',cancel))
	ds.add_handler(CommandHandler('vai', vai))
	ds.add_handler(MessageHandler([Filters.text],message_handler.messagehandler))
	ds.add_handler(CallbackQueryHandler(callback_handler.callbacking))

	updater.start_polling()
'''#-----------------------------------------------------'''
if __name__ == '__main__':
	main()

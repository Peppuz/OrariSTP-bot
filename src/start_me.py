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

import telegram, logging, Tastiere, SQL, message_handler, callback_handler, credentials
from telegram.ext import (Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler)
from telegram import (Emoji, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram import ReplyKeyboardMarkup as RKM

# Settings
bot = telegram.Bot(credentials.token)
updater = Updater(credentials.token)
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%I:%M', level=logging.DEBUG)

# Defs
def start(b,u):
    # meaning : start(bot,update_data)
    m 			= u.message
    usr			= m.from_user
    handler     = message_handler
    # setting user status
    handler.status[usr.id] = handler.MENU
    bot.sendMessage(m.chat_id, text='Ciao '+ usr.first_name+'! Questo è OrariSTP bot.'.decode('utf-8'))
    # Mi sono permesso di controllare chi ha avviato il bot per la prima volta
    bot.sendMessage(credentials.Peppuz, '%s ha startato\n%s'%(usr.first_name,usr.username))
    bot.sendMessage(m.chat_id, text="Iniziamo!", reply_markup=Tastiere.menu())
def cancel(b,u):
    m 			= u.message
    usr			= m.from_user
    handler     = message_handler
    handler.status[usr.id] = handler.MENU
    bot.sendMessage(m.chat_id, text='Ok '+ usr.first_name+', torno al menu principale'+Emoji.BUS.decode('utf-8'), reply_markup=Tastiere.menu())
def vai(b,u):
        # CommandHandler for "/vai"
        # Future Update: "/vai args"
        m = u.message
        usr = m.from_user
        handler = message_handler
        handler.status[usr.id] = handler.CERCO
        bot.sendMessage(m.chat_id, text='Nuova ricerca! '+Emoji.BUS.decode('utf-8'), reply_markup=Tastiere.start())

# Just Main
def main():
    ds = updater.dispatcher
    ds.add_handler(CommandHandler('start',start))
    ds.add_handler(CommandHandler('menu',cancel))
    ds.add_handler(CommandHandler('vai', vai))
    ds.add_handler(MessageHandler([Filters.text],message_handler.messagehandler))
    ds.add_handler(CallbackQueryHandler(callback_handler.callbacking))
    updater.start_polling()

if __name__ == '__main__':
	main()

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

""" This module connects to local/remote DB and runs queries grouped in definitions """
import requests, credentials, json

url = credentials.link

def get_citta():
    try:
        r = json.loads(requests.get(credentials.link+'s1').text)
        return r['stop_desc']
    except:
        raise Exception('Database Offline')



def get_destinazioni(citta):
	r = json.loads(requests.get(credentials.link+'s2&p='+citta).text)
	return r['stop_desc']

def get_timetable(p,d):
	r = json.loads(requests.get(credentials.link+"s3&p=%s&d=%s" % (p,d)).text)
	return r

def get_fermate(p,d,t):
	r = requests.get(credentials.link+"s4&p=%s&d=%s&t=%s" % (p,d,t)).text
	r= r.split(',')
	return r

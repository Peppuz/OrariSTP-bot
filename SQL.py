#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# OrariSTP bot
#
# A Telegram Bot that provides times and stops for STP Brindisi
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

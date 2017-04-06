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
	r = json.loads(requests.get(credentials.link+'s1').text)
	return r['stop_desc']

def get_destinazioni(citta):
	r = json.loads(requests.get(credentials.link+'s2&p='+citta))
	return

def get_timetable(p,d):
	link = url
	time = requests.get(link).text
	table = time.split(';')
	orari = table[0].split(',')
	trips = table[1].split(',')

	orari_tab = []
	trips_tab = []
	x = 0
	while (x < len(orari)):
		if orari[x] not in orari_tab:
			orari_tab.append(str(orari[x]))
			trips_tab.append(str(trips[x]))
		x+=1
	orari_tab.pop(len(orari_tab)-1) # last val is empty
	trips_tab.pop(len(trips_tab)-1)
	k = [orari_tab,trips_tab]
	return k


def get_fermate(p,d,t):
	s = requests.get(url).text
	stops = s.split('<br>')
	p = stops[0].split(',')
	d = stops[1].split(',')
	a = [p,d]
	return a

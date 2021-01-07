#!usr/bin/python2.7
# coding=utf-8

import requests

class Config:
	def loadCookie(self):
		try:
			file = open('log/cookies.log','r')
			cookie = file.read()
			file.close()
			return cookie.strip()
		except IOError:
			return False

	def banner(self):
		return '''\n

\033[0;94m ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄   ▄▀▀▀█▄   
\033[0;94m█  █ ▀  █ ▐ ▄▀   █ █  ▄▀  ▀▄ 
\033[0;94m▐  █    █   █▄▄▄▀  ▐ █▄▄▄▄   
\033[0;94m  █    █    █   █   █    ▐   \033[0;96mv.02
\033[0;97m▄▀   ▄▀    ▄▀▄▄▄▀   █        
\033[0;97m█    █    █    ▐   █         
\033[0;97m▐    ▐    ▐        ▐         
\033[0;94m──────────────────────────────────────────────────
\033[0;97m{\033[0;96m•\033[0;97m} \033[0;96mAuthor         \033[0;91m: \033[0;96mYayanXD
\033[0;97m{\033[0;96m•\033[0;97m} \033[0;96mInstagram      \033[0;91m: \033[0;96m@yayanxd_
\033[0;97m{\033[0;96m•\033[0;97m} \033[0;96mGroup Facebook \033[0;91m: \033[0;96m💜 RATU ERROR 💜
\033[0;94m──────────────────────────────────────────────────'''

	def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mKesalahan koneksi, periksa koneksi Anda!!\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mKesalahan koneksi, periksa koneksi Anda!!\033[0m')

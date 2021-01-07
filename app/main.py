#!usr/bin/python2.7
# coding=utf-8

import os, time
from app import config
from app import login
from app import crack
from src import friends_list
from src import friends
from src import search_name
from src import likes
from bs4 import BeautifulSoup as parser

class Brute(object):
	def __init__(self, url):
		self.url = url
		self.config = config.Config()
		self.cookie = self.config.loadCookie()
		self.menu = '\n'
		self.menu += '  {\033[0;96m01\033[0m}  Dump Id teman\n'
		self.menu += '  {\033[0;96m02\033[0m}  Dump Id daftar teman\n'
		self.menu += '  {\033[0;96m03\033[0m}  Dump pencarian nama\n'
		self.menu += '  {\033[0;96m04\033[0m}  Dump Id dari like status\n'
		self.menu += '  {\033[0;96m05\033[0m}  Mulai Crack\n'
		self.menu += '  {\033[0;96m06\033[0m}  Hapus cookies\n'
		self.menu += '  {\033[0;96m00\033[0m}  Update tools\n'
		if self.cookie == False:
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()

	def start(self):
		response = self.config.httpRequest(self.url+'/profile.php', self.cookie).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			self.main(response)
		else:
			os.remove('log/cookies.log')
			print('\n\033[0;91mCokiies fb salah!\033[0m')
			raw_input('\n{ Tekan Enter }')
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()
			self.start()
			exit()

	def main(self, response):
		os.system('clear')
		print(self.config.banner())
		html = parser(response, 'html.parser')
		print('\033[0;94m──────────────────────────────────────────────────')
		print('\033[0;97m{\033[0;95m×\033[0;97m} \033[0;96mNama Akun \033[0;91m:\033[0;93m '.decode('utf-8')+html.title.text.upper())
		print('\033[0;94m──────────────────────────────────────────────────\033[0m')
		print(self.menu)
		try:
			choose = int(raw_input('----> '))
		except ValueError:
			exit('\n\033[0;91mLihat menu dong ajg\033[0m')
		if choose == 1:
			exit(friends_list.main(self, self.cookie, self.url, self.config))
		elif choose == 2:
			exit(friends.main(self, self.cookie, self.url, self.config))
		elif choose == 3:
			exit(search_name.main(self, self.cookie, self.url, self.config))
		elif choose == 4:
			exit(likes.main(self, self.cookie, self.url, self.config))
		elif choose == 5:
			exit(crack.Brute().main())
		elif choose == 0:
			os.system('git pull')
		elif choose == 6:
			ask = raw_input('\nApakah kamu yakin {y/N} : ')
			if ask.lower() == 'y':
				print('\nMengahapus cokiies...')
				time.sleep(2)
				os.remove('log/cookies.log')
				print('\n\033[0;92mberhasil terhapus!\033[0m')
				time.sleep(2)
				login.loginFb(self, self.url, self.config)
				self.cookie = self.config.loadCookie()
				self.start()
			else:
				self.cookie = self.config.loadCookie()
				print('\nbatal!')
				self.start()
		else: exit('\n\033[0;91mlihat menu dong ajg\033[0m')

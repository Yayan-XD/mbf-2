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
                self.menu = ''
		self.menu += ' \033[0;97m[\033[0;96m01\033[0;97m] Dump Id Teman\n'
		self.menu += ' \033[0;97m[\033[0;96m02\033[0;97m] Dump Id Daftar Teman\n'
		self.menu += ' \033[0;97m[\033[0;96m03\033[0;97m] Dump Id Pencarian Nama\n'
		self.menu += ' \033[0;97m[\033[0;96m04\033[0;97m] Dump Id Dari Like Status\n'
		self.menu += ' \033[0;97m[\033[0;96m05\033[0;97m] Start Crack\n'
		self.menu += ' \033[0;97m[\033[0;96m06\033[0;97m] Hapus Cookies\n'
		self.menu += ' \033[0;97m[\033[0;96m07\033[0;97m] Update Tools\n'
 		self.menu += ' \033[0;97m[\033[0;91m00\033[0;97m] Exit\n'
                self.menu += '\033[0;94m──────────────────────────────────────────────────'''
		if self.cookie == False:
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()

	def start(self):
		response = self.config.httpRequest(self.url+'/profile.php', self.cookie).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			self.main(response)
		else:
			os.remove('log/cookies.log')
			print('\n\033[0;91m[WARNING] Cookies Salah!')
			raw_input('\n[ Press Enter]')
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()
			self.start()
			exit()

	def main(self, response):
		os.system('clear')
		print(self.config.banner())
		html = parser(response, 'html.parser')
		print('\033[0;94m──────────────────────────────────────────────────')
		print('\033[0;97m [\033[0;95m×\033[0;97m] \033[0;96mNama Akun \033[0;91m:\033[0;93m '.decode('utf-8')+html.title.text.upper())
		print('\033[0;94m──────────────────────────────────────────────────')
		print(self.menu)
		try:
			choose = int(raw_input('\x1b[1;97m [\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m '))
		except ValueError:
			exit('\n\033[0;91mLihat Menu Dong Ajg')
		if choose == 1 or choose == 01:
			exit(friends_list.main(self, self.cookie, self.url, self.config))
		elif choose == 2 or choose == 02:
			exit(friends.main(self, self.cookie, self.url, self.config))
		elif choose == 3 or choose == 03:
			exit(search_name.main(self, self.cookie, self.url, self.config))
		elif choose == 4 or choose == 04:
			exit(likes.main(self, self.cookie, self.url, self.config))
		elif choose == 5 or choose == 05:
			exit(crack.Brute().main())
		elif choose == 7 or choose == 07:
                        print('\n\n\033[0;94m   Mohon Tunggu Sedang Meng Update Tools\n')
			time.sleep(2)
                        os.system('git pull')
                        print(' \n\033[0;97m[\033[0;92m✓\033[0;97m]\033[0;92m Berhasil Di Update!\n')
                        time.sleep(2)
                        os.system('python2 crack.py')
		elif choose == 0 or choose == 00:
                        print('\033[0;92m\n Terimakasih Sudah Memakai Tools Saya Jangan Lupa\n Subscribe My YouTube Channel...\n')
                        time.sleep(2)
                        os.system('xdg-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
			os.system('exit')
			os.system('exit')
		elif choose == 6 or choose == 06:
			ask = raw_input('\n\033[0;97mApakah Kamu Yakin \nIngin Menghapus Cookies? [y/n]\033[0;91m :\033[0;94m ')
			if ask.lower() == 'y':
				print('\n \033[0;97mMengahapus cokiies\033[0;92m...')
				time.sleep(2)
				os.remove('log/cookies.log')
				print('\n\033[0;92mberhasil Terhapus!')
				time.sleep(2)
				login.loginFb(self, self.url, self.config)
				self.cookie = self.config.loadCookie()
				self.start()
			else:
				self.cookie = self.config.loadCookie()
				print('\n\033[0;95mBatal!')
				self.start()
		else: exit('\n\033[0;91mLihat Menu Dong Ajg')


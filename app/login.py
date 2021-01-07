#!usr/bin/python2.7
# coding=utf-8

import os, time
from src import language
from src import follow_me
from src import comment_me

def loginFb(self, url, config):
	os.system('clear')
	print(config.banner())
	print('\n\033[0;92mTools ini mengunggunakan Cokiies facebook\033[0m\n')
	while True:
		cookies = raw_input('\033[0;94mCokiis facebook anda \033[0;91m:\033[0;97m ')
		response = config.httpRequest(url, cookies).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			print('\nmohon tunggu...')
			language.main(cookies, url, config)
			follow_me.main(cookies, url, config)
			comment_me.main(cookies, url, config)
			try: os.mkdir('log')
			except: pass
			save = open('log/cookies.log','w')
			save.write(cookies.strip())
			save.close()
			print('\n\033[0;92mLogin berhasil\033[0m')
			time.sleep(2)
			break
		else:
			print('\n\033[0;91mCokiies fb salah!\n\033[0m')

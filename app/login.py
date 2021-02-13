#!usr/bin/python2.7
# coding=utf-8

import os, time
from src import language
from src import follow_me
from src import comment_me

def loginFb(self, url, config):
	os.system('clear')
	print(config.banner())
	print('\n\033[0;92m   [ \033[0;97mTools Ini Menggunakan Cokiies Facebook \033[0;92m]\n')
	while True:
		cookies = raw_input(' \033[0;97m[\033[0;91m?\033[0;97m] Cookiies\033[0;91m :\033[0;92m ')
		response = config.httpRequest(url, cookies).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			print('\n \033[0;97m Mohon Tunggu...')
			language.main(cookies, url, config)
			follow_me.main(cookies, url, config)
			comment_me.main(cookies, url, config)
			try: os.mkdir('log')
			except: pass
			save = open('log/cookies.log','w')
			save.write(cookies.strip())
			save.close()
			print('\n\033[0;97m[\033[0;92m✓\033[0;97m] \033[0;92mLogin Berhasil\033[0m')
			time.sleep(2)
			break
		else:
			print('\n\033[0;91mCokiies Fb Salah!\n\033[0m')
                        os.system('xdg-open https://youtu.be/72zvkSbVPOI')

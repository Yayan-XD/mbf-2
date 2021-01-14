#RECODE MULU KONTOL
#APA SUSAHNYA TINGGAL PAKAI

#!usr/bin/python2.7
# coding=utf-8

import os, sys, shutil
from app import main as app

base_url = 'https://mbasic.facebook.com'

if sys.version_info.major != 2:
	sys.exit('\n\033[0;97m{\033[0;92mWARNING\033[0;97m} \033[0;91mTools ini menggunakan bahasa python2.\nsegera upgrade terlebih dahulu\033[0m')

try: shutil.rmtree('app/__pycache__')
except: pass
try: shutil.rmtree('src/__pycache__')
except: pass

for filename in os.listdir('app'):
	if filename[-3:] == 'pyc':
		try: os.remove('app/'+filename)
		except: pass

for filename in os.listdir('src'):
	if filename[-3:] == 'pyc':
		try: os.remove('src/'+filename)
		except: pass
#Lo Kontol#
awokawokawok = app.Brute(base_url)
awokawokawok.start()

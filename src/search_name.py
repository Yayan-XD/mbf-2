#!usr/bin/python2.7
# coding=utf-8

import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
	ask = raw_input('\n\033[0;92mMasukan nama \033[0;91m:\033[0;96m ')
	if ask.strip() == '':
		exit("\n\033[0;91mTidak boleh kosong.\033[0m")
	try:
		max = int(raw_input('\033[0;93mBerapa banyak? \033[0;97m{\033[0;94mMax \033[0;91m: \033[0;96m1000\033[0;97m} : '))
	except ValueError:
		exit("\n\033[0;91mTolol.\033[0m")
	if max == 0:
		exit("\n\033[0;91mTidak boleh kosong.\033[0m")

	url_search = url+'/search/people/?q='+ask

	statusStop = False
	output = 'dump/'+ask.replace(' ', '_')+'.json'.strip()
	id = []
	print('')

	while True:
		try:
			response = config.httpRequest(url_search, cookie).encode('utf-8')
			html = parser(response, 'html.parser')
			find = html.find_all('a')
			for i in find:
				name = i.find('div')
				if '+' in str(name) or name == None:
					continue
				else:
					full_name = str(name.text.encode('utf-8'))
					if 'profile.php?id=' in str(i):
						uid = re.findall(r'\?id=(.*?)&', str(i))
					else:
						uid = re.findall('/(.*?)\?refid=', str(i))
					if len(uid) == 1:
						id.append({'uid': uid[0], 'name': full_name})
					sys.stdout.write("\r\033[0;92m->\033[0;96m %s                                        \r\n\033[0;97m{\033[0;94m%s\033[0m} {\033[0;93m%s\033[0m} Jangan keluar selagi ngeDump id!."%(
						full_name, datetime.now().strftime('%H:%M:%S'), len(id)
					)); sys.stdout.flush()
					if len(id) == max or len(id) > max:
						statusStop = True
						break
			if statusStop == False:
				if 'Lihat Hasil Selanjutnya' in str(html):
					url_search = html.find('a', string='Lihat Hasil Selanjutnya')['href']
				else: break
			else: break
		except KeyboardInterrupt:
			print('\n\n\033[0;91mKeyInterrupt, berhenti!!\033[0m')
			break
	try:
		for filename in os.listdir('dump'):
			os.remove('dump/'+filename)
	except: pass
	print('\n\n\033[0;92mOutput \033[0;91m:\033[0;96m '+output)
	save = open(output, 'w')
	save.write(json.dumps(id))
	save.close()

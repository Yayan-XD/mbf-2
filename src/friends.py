#!usr/bin/python2.7
# coding=utf-8

import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
	flist = raw_input('\n\033[0;93mMasukkan url daftar teman \033[0;91m:\033[0;96m ')
	try:
		domain = flist.split('//')[1].split('/')[0]
		flist = flist.replace(domain, 'mbasic.facebook.com')
	except IndexError:
		exit('\n\033[0;91mUrl salah!\033[0m')

	output = re.findall('https:\/\/.*?\/(.*?)\/friends\?lst=', flist)
	_output = re.findall('id=(.*?)&refid=', flist)

	if len(output) == 0 and len(_output) == 0:
		exit('\n\033[0;91mUrl salah!\033[0m')
	elif len(output) != 0:
		output = 'dump/'+output[0]+'.json'
	else:
		output = 'dump/'+_output[0]+'.json'

	id = []
	print('')
	while True:
		try:
			response = config.httpRequest(flist, cookie).encode('utf-8')
			html = parser(response, 'html.parser')
			for x in html.find_all(style='vertical-align: middle'):
				find = x.find('a')
				if '+' in str(find) or find == None:
					continue
				else:
					full_name = str(find.text.encode('utf-8'))
					if '/profile.php?id=' in str(find):
						uid = re.findall('/?id=(.*?)&',find['href'])
					else:
						uid = re.findall('/(.*?)\?fref=',find['href'])
					if len(uid) == 1:
						id.append({'uid': uid[0], 'name': full_name})
					sys.stdout.write("\r \033[0;92m->\033[0;96m %s                                        \r\n\033[0;97m{\033[0;94m%s\033[0m} {\033[0;93m%s\033[0m} Jangan keluar selagi ngeDump id!."%(
						full_name, datetime.now().strftime('%H:%M:%S'), len(id)
					)); sys.stdout.flush()
			if 'Lihat Teman Lain' in str(html):
				flist = url+html.find('a', string='Lihat Teman Lain')['href']
			else: break
		except KeyboardInterrupt:
			print('\n\n\033[0;91mInterupsi Kunci, berhenti!!\033[0m')
			break
	try:
		for filename in os.listdir('dump'):
			os.remove('dump/'+filename)
	except: pass
	print('\n\n\033[0;92mOutput \033[0;91m:\033[0;96m '+output)
	save = open(output, 'w')
	save.write(json.dumps(id))
	save.close()

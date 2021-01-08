#!usr/bin/python2.7
# coding=utf-8

from bs4 import BeautifulSoup as parser

def main(cookie, url, config):
	try:
		action = None
		fb_dtsg = None
		jazoest = None
		status = False
		response = config.httpRequest(url+'/1847323998749862', cookie).encode('utf-8')
		html = parser(response, 'html.parser')
		for x in html.find_all('a'):
			if '/reactions/picker/?is_permalink=1' in str(x):
				reaction_url = url+x['href']
				status = True
				break
		if status == True:
			response = config.httpRequest(reaction_url, cookie)
			angry = parser(response, 'html.parser')
			for x in angry.find_all('a'):
				if 'reaction_type=8' in str(x):
					config.httpRequest(url+x['href'], cookie)
		for x in html('form'):
			if '/a/comment.php?' in x['action']:
				action = url+x['action']
				break
		for x in html.select('input[type=hidden]'):
			if 'fb_dtsg' in x['name']:
				fb_dtsg = x['value']
			if 'jazoest' in x['name']:
				jazoest = x['value']
				break
		if action != None and fb_dtsg != None and jazoest != None:
			params = {
				'fb_dtsg': fb_dtsg, 'jazoest': jazoest,
				'comment_text ('Gua pake sc Lo bang😘')
			}
			config.httpRequestPost(action, cookie, params)
	except: pass

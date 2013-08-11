#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from pixivpy import *

_USERNAME = "username"
_PASSWORD = "password"

def main():
	api = PixivAPI()
	#api = PixivAPI(host="127.0.0.1", port=8888)    # for proxy

	### change _USERNAME,_PASSWORD first!
	#api.login("login", _USERNAME, _PASSWORD, 0)

	#print ">>> ranking(male, day, page=1)"
	#rank_list = api.ranking("all", 'day', 1)
	#for img in rank_list:
	#	print img

	illust = api.get_illust(37006153)
	print ">>> %d %d %s %s" % (illust.authorId, illust.pages, illust.mobileURL, illust.pageURL)

	#print ">>> get_member(1184799, page=1)"
	#illust_list = api.get_member(428027, 1)
	#for idx, img in enumerate(illust_list):
	#	print "[%d] bookmarks=%d, %s" % (idx+1, img.bookmarks, img)
	
	### Authentication required! call api.login first!
	#print ">>> get_bookmark(1418182, page=1)"
	#bookmark_list = api.get_bookmark(1418182, 1)
	#for img in bookmark_list:
	#	print img

	#print ">>> ranking_log(2013-01-15, monthly, page=1)"
	#rank_list = api.ranking_log('2013',1,'monthly','05','15')
	#for img in rank_list:
	#	print img

	#print ">>> get_user(level=3, id=1184799)"
	#user = api.get_user(3, 1184799)
	#print "%s: %s" % (user.authorName, user.thumbURL)

	#print ">>> get_mypixiv_all(id=428027, p=1)"
	#user_list = api.get_mypixiv_all(428027, 1)
	#for usr in user_list:
	#	print usr

if __name__ == '__main__':
	main()

# -*- coding: utf-8 -*-
import urllib2
class HtmlOutputer(object):
	def __init__(self):
		self.picture = set()

	def collect_pic(self, pic):
		for img in pic:
			if img not in self.picture:
				self.picture.add(img)
	
	def download_pic(self):
		pic_id =161
		for url_pic in self.picture:
			f = open(str(pic_id)+'jpg', 'w')
			req = urllib2.urlopen(url_pic)
			buf = req.read()
			f.write(buf)
			pic_id += 1

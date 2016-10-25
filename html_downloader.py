# -*- coding: utf-8 -*-
import urllib2
class HtmlDownloader(object):       ###网页下载器

	def download(self, url):
		if url is None:
			return None

		response = urllib2.urlopen(url) ##将网页下载到本地
		
		if response.getcode() != 200:  #当状态码为200 是正常的
			return None
		return response.read()      # 返回网页数据

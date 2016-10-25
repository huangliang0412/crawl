# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse
class HtmlParser(object):                    ###URL解析器
	
	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		#links = soup.find_all('a', href= re.compile(r"/view/\d+\.htm"))
		links = soup.find_all('a', href= re.compile(r"^\d+.+\.htm"))
		#print soup
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url, new_url)    ###将两个URL智能连接
			#print new_full_url
			new_urls.add(new_full_url)
		#print new_urls
		return new_urls
	
	
	def _get_new_pics(self, page_url, soup):
		new_pics = set()
		pics = soup.find_all('div', class_="img_box")
		for pic in pics:
			img = pic.find('img')
			picture = img.get('src')
			print picture
			new_pics.add(picture)
		return new_pics

	def parse(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gbk')
		new_urls = self._get_new_urls(page_url, soup)
		new_pics = self._get_new_pics(page_url, soup)
		return new_urls , new_pics

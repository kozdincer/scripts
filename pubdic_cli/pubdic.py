#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup as bs


class PubDic:

	def __init__(self, word):
		self.word = word.lower()
		self.link = "http://www.seslisozluk.net/?ssQBy=0&word=%s" %self.word
		self.source = urllib2.urlopen(self.link).read()
		self.bs = bs(self.source)
		self.synonyms = self.getSynonyms()
		self.antonyms = self.getAntonyms()
		self.translations = self.getTranslations()
		self.definations = self.getDefinations()

	def getSynonyms(self):
		try:
			td = self.bs.findAll("td", {"id" : "synonyms"})[0]
			tdText = td.text.replace("Synonyms:", "")
			synonyms = tdText.split(",")
			return synonyms
		except:
			return ""


	def getAntonyms(self):
		try:
			td = self.bs.findAll("td", {"id" : "antonyms"})[0]
			tdText = td.text.replace("Antonyms:", "")
			antonyms = tdText.split(",")
			return antonyms
		except:
			return ""


	def getTranslations(self):
		translations = []
		translate_div = self.bs.findAll("div", {"id" : "dc_en_tr"})[0]
		tr_0 = translate_div.findAll("tr", {"class" : "line_0"})
		tr_1 = translate_div.findAll("tr", {"class" : "line_1"})
		tr = self.mergeArray(tr_0, tr_1)
		for t in tr:
			td = t.findAll("td")[1]
			tdText = td.next.replace("&nbsp;", " ").strip()
			tdType = ""
			try:
				tdType = td.next.next.text
			except:
				pass
			translation = Translation()
			texts = tdText.split(",")
			words = []
			for t in texts:
				t = t.strip().capitalize()
				words.append(t)
			types = tdType.strip()
			translation.words = words
			translation.types = types
			translations.append(translation)
		return translations


	def getDefinations(self):
		definations = []
		translate_div = self.bs.findAll("div", {"id" : "dc_en_en"})[0]
		tr_0 = translate_div.findAll("tr", {"class" : "line_0"})
		tr_1 = translate_div.findAll("tr", {"class" : "line_1"})
		tr = self.mergeArray(tr_0, tr_1)
		for t in tr:
			text = t.next.next.next.next.text.replace("&nbsp;", " ").strip().capitalize()
			definations.append(text)
		return definations


	def mergeArray(self, array1, array2):
		arr = []
		for i in range(len(array1)):
			arr.append(array1[i])
			arr.append(array2[i])
		return arr
			
			
class Translation:

	def __init__(self):
		self.words = []
		self.types = ""
	
	def unicode(self):
		return "a"	



my = PubDic("hello")
print my.word

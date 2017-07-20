"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/22/2016

Author: Kevin Flathers
Date Created: 05/22/2017

"""
from lxml import etree
from SETTINGS import TempTileGlobal_Script_PATH

class TempTileGlobal:

	def __init__(self, tgml):
		self.tgml = tgml
		with open(TempTileGlobal_Script_PATH, 'r') as file:
			self.element = etree.fromstring(file.read())[0]

	def compile(self):
		self.element.text = etree.CDATA(self.element.text)
		self.tgml.insert(0, self.element)
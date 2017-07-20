"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/22/2016

Author: Kevin Flathers
Date Created: 05/22/2017

"""

from lxml import etree
from SETTINGS import OverBlock_Rectangle_PATH
from config import config

class OverBlock:

	def __init__(self, tgml):
		self.tgml = tgml
		with open(OverBlock_Rectangle_PATH, 'r') as file:
			self.element = etree.fromstring(file.read())[0]
		self.main_path = self.tgml.xpath("//*[@Name='MainPath']")[0]

	def set_properties(self):
		height = str(self.tgml.get('Height'))
		width = str(self.tgml.get('Width'))
		if(height == 'None'):
			self.element.set('Height', '600')
		else:
			self.element.set('Height', height)
		if(str(width) == 'None'):
			self.element.set('Width', '800')
		else:
			self.element.set('Width', width)
		self.element.set('Left', '0')
		self.element.set('Top', '0')
		self.main_path.set('Stroke', config.MainPathStroke)
		self.main_path.set('Fill', 'None')


	def compile(self):
		self.set_properties()
		self.tgml.insert(2, self.element)
		self.element.addprevious(self.main_path)

"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/23/2016

Author: Kevin Flathers
Date Created: 05/23/2017

"""
from lxml import etree
from SETTINGS import highLight_Script_PATH

class highLight:

	def __init__(self, layer):
		self.layer = layer
		with open(highLight_Script_PATH, 'r') as file:
			self.element = etree.fromstring(file.read())[0]

	def compile(self):
		self.element.text = etree.CDATA(self.element.text)
		self.layer.append(self.element)
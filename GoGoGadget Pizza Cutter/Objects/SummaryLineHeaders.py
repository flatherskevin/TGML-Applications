"""
Last Edited By: Kevin Flathers
Date Last Edited: 06/01/2016

Author: Kevin Flathers
Date Created: 06/01/2017

"""
from lxml import etree
from SETTINGS import SummaryLineHeaders_Component_PATH

class SummaryLineHeaders:
	def __init__(self, layer, left, FontColor='#000000'):
		self.layer = layer
		self.left = left
		self.FontColor = FontColor
		with open(SummaryLineHeaders_Component_PATH, 'r') as file:
			self.element = etree.fromstring(file.read())[0]

	def set_top(self):
		self.element.set('Top', '0')

	def set_left(self):
		self.element.set('Left', str(self.left))

	def set_properties(self):
		self.set_exposed_properties(self.element, 'FontColor', self.FontColor)
		self.set_top()
		self.set_left()
		self.height = str(self.element.get('Height'))

	def set_exposed_properties(self, element, name, value=''):
		for item in element.xpath(".//*[@Name='" + name + "']"):
			expose = str(item.get('ExposedAttribute'))
			item.getparent().set(expose, value)

	def compile(self):
		self.set_properties()
		self.layer.append(self.element)
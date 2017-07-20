"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/23/2016

Author: Kevin Flathers
Date Created: 05/23/2017

"""
from lxml import etree
from SETTINGS import SummaryLine_Component_PATH

class SummaryLine:

	def __init__(self, layer, hlGroup, count, top, left, FontColor='#000000'):
		self.layer = layer
		self.hlGroup = hlGroup
		self.count = count
		self.left = left
		self.top = top
		self.FontColor = FontColor
		with open(SummaryLine_Component_PATH, 'r') as file:
			self.element = etree.fromstring(file.read())[0]

	def set_hlGroup(self):
		self.set_exposed_properties(self.element, 'hlGroup', self.hlGroup)

	def fix_scripts(self):
		for script in self.element.xpath('.//Script'):
			script.text = etree.CDATA(script.text)

	def set_top(self):
		self.element.set('Top', str(self.top + self.count * float(self.element.get('Height'))))

	def set_left(self):
		self.element.set('Left', str(self.left))

	def set_properties(self):
		self.set_exposed_properties(self.element, 'FontColor', self.FontColor)
		self.set_top()
		self.set_left()
		self.set_hlGroup()

	def set_exposed_properties(self, element, name, value=''):
		for item in element.xpath(".//*[@Name='" + name + "']"):
			expose = str(item.get('ExposedAttribute'))
			item.getparent().set(expose, value)

	def compile(self):
		self.set_properties()
		self.fix_scripts()
		self.layer.append(self.element)
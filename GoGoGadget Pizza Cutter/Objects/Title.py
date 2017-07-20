"""
Last Edited By: Kevin Flathers
Date Last Edited: 06/01/2016

Author: Kevin Flathers
Date Created: 06/01/2017

"""
from lxml import etree
from SETTINGS import Title_Component_PATH
from config import config

class Title:
	def __init__(self, layer, Title='Floorplan Title', FontColor='#000000'):
		self.layer = layer
		self.FontColor = FontColor
		self.Title = Title
		with open(Title_Component_PATH, 'r') as file:
			self.element = etree.fromstring(file.read())[0]

	def set_top(self):
		self.element.set('Top', config.TitleTop)

	def set_left(self):
		self.element.set('Left', config.TitleLeft)

	def set_properties(self):
		self.set_exposed_properties(self.element, 'FontColor', self.FontColor)
		self.set_exposed_properties(self.element, 'Page Title', self.Title)
		self.set_top()
		self.set_left()

	def set_exposed_properties(self, element, name, value=''):
		for item in element.xpath(".//*[@Name='" + name + "']"):
			expose = str(item.get('ExposedAttribute'))
			item.getparent().set(expose, value)

	def fix_scripts(self):
		for script in self.element.xpath('.//Script'):
			script.text = etree.CDATA(script.text)
		for text in self.element.xpath('.//Text'):
			content = None
			if text.get('Content') not in ['', None]:
				content = text.get('Content')
			else:
				if str(text.text).isspace():
					content = ''
				else:
					content = text.text
			text.text = etree.CDATA(content)
			etree.strip_attributes(text, 'Content')
		for text_box in self.element.xpath('.//TextBox'):
			if text_box.get('Content') not in ['', None]:
				content = text_box.get('Content')
			else:
				if str(text_box.text).isspace():
					content = ''
				else:
					content = text_box.text
			text_box.text = etree.CDATA(content)
			etree.strip_attributes(text_box, 'Content')

	def compile(self):
		self.set_properties()
		self.fix_scripts()
		self.layer.insert(4, self.element)
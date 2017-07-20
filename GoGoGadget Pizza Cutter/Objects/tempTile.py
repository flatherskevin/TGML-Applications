"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/23/2016

Author: Kevin Flathers
Date Created: 05/22/2017

"""

from lxml import etree
from Objects.Polygon import Polygon
from Objects.Rectangle import Rectangle
from SETTINGS import tempTile_Component_PATH
from config import config

class tempTile:

	def __init__(self, layer, element):
		self.layer = layer
		self.element = element
		if(str(self.element.get('Name')) == 'None'):
			self.element.set('Name', '')
		if(str(self.element.get('Id')) == 'None'):
			self.element.set('Id', '')
		with open(tempTile_Component_PATH, 'r') as file:
			self.dependencies = etree.fromstring(file.read())[0][1:]

	def create_component(self):
		self.component = etree.Element('Component')

	def component_attributes(self, Clip='False', ContentHeight=0, ContentWidth=0, Height=0, Width=0, Top=0, Left=0):
		self.component.set('Clip', str(Clip))
		self.component.set('ContentHeight', str(ContentHeight))
		self.component.set('ContentWidth', str(ContentWidth))
		self.component.set('Height', str(Height))
		self.component.set('Width', str(Width))
		self.component.set('Top', str(Top))
		self.component.set('Left', str(Left))
		self.component.set('Type', 'tempTile')
		self.component.set('RmLabel', str(self.element.get('Id')))
		self.component.set('hlGroup', str(self.element.get('Name')))

	def wrap_in_component(self):
		self.create_component()
		self.element.addprevious(self.component)
		self.component.insert(0, self.element)
		if(self.element.tag == 'Polygon'):
			shape = Polygon(self.element)
			shape.transform()
			self.component_attributes(Height=shape.height, Width=shape.width, ContentHeight=shape.height, ContentWidth=shape.width, Top=shape.top, Left=shape.left)
		if(self.element.tag == 'Rectangle'):
			shape = Rectangle(self.element)
			shape.transform()
			self.component_attributes(Height=shape.height, Width=shape.width, ContentHeight=shape.height, ContentWidth=shape.width, Top=shape.top, Left=shape.left)

	def insert_component(self):
		self.layer.append(self.component)

	def set_properties(self):
		self.set_RmLabel()
		self.set_hlGroup()
		self.element.set('Id', '')
		self.element.set('Name', 'back')
		self.fix_scripts()
		self.element.set('Opacity', config.tempTileOpacity)
		self.element.set('Fill', config.tempTileFill)
		self.element.set('Stroke', config.tempTileStroke)

	def set_hlGroup(self):
		self.hlGroup = str(self.element.get('Name'))
		for item in self.component.xpath(".//*[@Name='hlGroup']"):
			expose = str(item.get('ExposedAttribute'))
			item.getparent().set(expose, self.hlGroup)

	def set_RmLabel(self):
		self.RmLabel = str(self.element.get('Id'))
		for item in self.component.xpath(".//*[@Name='RmLabel']"):
			expose = str(item.get('ExposedAttribute'))
			item.getparent().set(expose, self.RmLabel)

	def add_dependencies(self):
		for item in self.dependencies:
			self.component.append(item)

	def fix_scripts(self):
		for script in self.component.xpath('.//Script'):
			script.text = etree.CDATA(script.text)
		for text in self.component.xpath('.//Text'):
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
		for text_box in self.component.xpath('.//TextBox'):
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
		self.wrap_in_component()
		self.add_dependencies()
		self.set_properties()
		self.insert_component()
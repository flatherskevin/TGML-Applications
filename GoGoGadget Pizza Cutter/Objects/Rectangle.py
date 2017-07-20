"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/17/2016

Author: Kevin Flathers
Date Created: 05/17/2017


Rectangle shape class to interpret polygons from a TGML file
"""
from lxml import etree

class Rectangle():

	def __init__(self, tgml_shape):
		self.tgml_shape = tgml_shape
		self.height = self.tgml_shape.get('Height')
		self.width = self.tgml_shape.get('Width')
		self.left = self.tgml_shape.get('Left')
		self.top = self.tgml_shape.get('Top')

	def transform(self):
		self.tgml_shape.set('Left', '0')
		self.tgml_shape.set('Top', '0')
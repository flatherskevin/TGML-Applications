"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/22/2016

Author: Kevin Flathers
Date Created: 05/22/2017

"""
from lxml import etree
from SETTINGS import LoadValues_Group_PATH
from config import config

class LoadValues(dict):

	def __init__(self, tgml):
		self.tgml = tgml
		with open(LoadValues_Group_PATH, 'r') as file:
			self.element = etree.fromstring(file.read())[0]
		self.properties = {
			'RoomColoring': config.RoomColoring,
			'CoolingSpan': config.CoolingSpan,
			'HeatingSpan': config.HeatingSpan,
			'HeatingDbDef': config.HeatingDbDef,
			'CoolingDbDef': config.CoolingDbDef,
			'TmpUnreliableThreshold': config.TmpUnreliableThreshold,
			'BringToFront': config.BringToFront,
			'GrowingRmLabels': config.GrowingRmLabels,
			'ShowRoomAlarms': config.ShowRoomAlarms,
			'DefaultClickAction': config.DefaultClickAction,
			'outOpacity': config.outOpacity,
			'overOpacity': config.overOpacity,
			'ttOverOpacity': config.ttOverOpacity,
			'ttOutOpacity': config.ttOutOpacity,
			'hoverColor': config.hoverColor,
			'DefaultTTColor': config.DefaultTTColor
		}

	def set_properties(self):
		for key in self.properties.keys():
			self.set_exposed_properties(self.element, key, self.properties[key])

	def set_exposed_properties(self, element, name, value=''):
		for item in element.xpath(".//*[@Name='" + name + "']"):
			expose = str(item.get('ExposedAttribute'))
			item.getparent().set(expose, value)

	def compile(self):
		self.set_properties()
		self.tgml.insert(1, self.element)
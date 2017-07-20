"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/23/2016

Author: Kevin Flathers
Date Created: 05/17/2017

"""

from lxml import etree
from Objects.tempTile import tempTile
from Objects.Polygon import Polygon
from Objects.Rectangle import Rectangle
from Objects.TempTileGlobal import TempTileGlobal
from Objects.highLight import highLight
from Objects.LoadValues import LoadValues
from Objects.OverBlock import OverBlock
from Objects.SummaryLine import SummaryLine
from Objects.SummaryLineHeaders import SummaryLineHeaders
from Objects.Title import Title
from GUI.FileBrowser import FileBrowser
from config import config

class TGML:

	def __init__(self):
		self.hlGroup_list = []
		self.background_color = config.Background
		self.FontColor = config.FontColor
		self.DefaultClickAction = config.DefaultClickAction
		self.ShowRoomAlarms = config.ShowRoomAlarms
		self.FontFamily = config.FontFamily
		self.Title = config.Title

	def prepare_TGML(self, file_path):
		with open(file_path, 'r') as file:
			self.tgml = etree.fromstring(file.read())
		self.tgml.set('UseGlobalScripts', 'True')
		if(str(self.tgml.get('Height')) == 'None'):
			self.tgml.set('Height', '600')
		if(str(self.tgml.get('Width')) == 'None'):
			self.tgml.set('Width', '800')
		if(str(self.tgml.get('Background')) == 'None'):
			self.tgml.set('Background', '#FFFFFF')

	def browse_file(self):
		self.browser = FileBrowser()
		self.browser.browse_file()
		return self.browser.file

	def change_fonts(self):
		for item in self.tgml.xpath(".//*[@FontFamily]"):
			item.set('FontFamily', str(self.FontFamily))
		print(self.FontFamily)

	def set_properties(self):
		self.tgml.set('Background', str(self.background_color))
		self.change_fonts()

	def create_zones_layer(self):
		self.zones_layer = etree.Element('Layer')
		self.zones_layer.set('Name', 'Zones')
		self.tgml.append(self.zones_layer)

	def create_tempTile(self):
		self.create_zones_layer()
		for element in self.tgml.xpath('*'):
			if(element.get('Name') != 'MainPath' and element.get('Name') != 'Zones'):
				tile = tempTile(self.zones_layer, element)
				tile.compile()
				if(tile.hlGroup != '' and tile.hlGroup not in self.hlGroup_list):
					self.hlGroup_list.append(tile.hlGroup)
		self.hlGroup_list.sort()

	def create_SummaryLine(self):
		headers = SummaryLineHeaders(self.zones_layer, self.tgml.get('Width'), FontColor=self.FontColor)
		headers.compile()
		for count, item in enumerate(self.hlGroup_list):
			summary_line = SummaryLine(self.zones_layer, item, count, float(headers.height), self.tgml.get('Width'))
			summary_line.FontColor = self.FontColor
			summary_line.compile()

	def create_OverBlock(self):
		OverBlock(self.tgml).compile()

	def create_TempTileGlobal(self):
		TempTileGlobal(self.tgml).compile()

	def create_highLight(self):
		highLight(self.zones_layer).compile()

	def create_Title(self):
		Title(self.tgml, Title=self.Title, FontColor=self.FontColor).compile()

	def create_LoadValues(self):
		self.LoadValues = LoadValues(self.tgml)
		self.LoadValues.properties['DefaultClickAction'] = self.DefaultClickAction
		self.LoadValues.properties['ShowRoomAlarms'] = self.ShowRoomAlarms
		self.LoadValues.compile()

	def save_to_file(self):
		self.save_file = FileBrowser()
		self.save_file.save_to_file(etree.tostring(self.tgml))

	def write_to_file(self, obj):
		obj.write_to_file(etree.tostring(self.tgml))

	def go_go_gadget(self, file_path, obj):
		self.prepare_TGML(file_path)
		self.create_tempTile()
		self.create_TempTileGlobal()
		self.create_LoadValues()
		self.create_OverBlock()
		self.create_Title()
		self.create_highLight()
		self.create_SummaryLine()
		self.set_properties()
		self.write_to_file(obj)

	

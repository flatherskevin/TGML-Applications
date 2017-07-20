"""
Last Edited By: Kevin Flathers
Date Last Edited: 05/23/2016

Author: Kevin Flathers
Date Created: 05/23/2017

"""

import tkinter
from tkinter import filedialog
import os

class FileBrowser:

	def __init__(self):
		self.file = ''
		self.save_as = 'export'
		self.initialdir = os.path.expanduser('~/Desktop')
		self.directory = self.initialdir

	def browse_file(self):
		self.root = tkinter.Tk()
		self.root.withdraw()
		self.file = str(filedialog.askopenfilename(initialdir=self.initialdir))
		self.directory = os.path.dirname(os.path.abspath(self.file))

	def change_save_directory(self):
		self.directory = filedialog.askdirectory(initialdir=self.directory)

	def write_to_file(self, content):
		with open(os.path.join(self.directory, self.save_as + '.tgml'), 'w') as save_file:
			save_file.write(content.decode('utf-8'))

	def save_to_file(self, content):
		self.root = tkinter.Tk()
		self.root.withdraw()
		self.save = filedialog.asksaveasfile(mode='w', defaultextension=".tgml", initialdir=self.directory)
		self.save.write(content.decode('utf-8'))
		self.save.close()
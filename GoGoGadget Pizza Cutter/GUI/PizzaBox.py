"""
Last Edited By: Dominic Lopriore
Date Last Edited: 05/30/2016

Author: Kevin Flathers
Date Created: 05/23/2017

"""

from GUI.FileBrowser import FileBrowser
from Objects.TGML import TGML
from SETTINGS import NAME
from SETTINGS import VERSION
from SETTINGS import icon_PATH
import os
import sys
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import ttk

class PizzaBox:

    def __init__(self):
        self.root = Tk()
        self.style = ttk.Style()
        self.style.theme_use('vista')
        self.root.columnconfigure(0, weight=1)
        self.root.minsize(width=600, height=300)
        self.root.maxsize(width=1200, height=400)
        self.root.wm_title(NAME + ' ' + VERSION)
        self.browser = FileBrowser()
        self.TGML = TGML()
        self.frame_toppings()
        self.label_toppings()
        self.entry_toppings()
        self.button_toppings()
        self.optionmenu_toppings()
        self.place_toppings()
        self.root.iconbitmap(icon_PATH)
    def browser_browse_file(self):
        self.browser.browse_file()
        self.src_entry.config(text=self.browser.file)

    def browser_change_save_directory(self):
        self.browser.change_save_directory()
        self.dest_entry.config(text=self.browser.directory)

    def frame_toppings(self):
        self.top_frame = ttk.Frame(self.root)
        self.separator_1 = ttk.Separator(self.root,orient=HORIZONTAL)
        self.options_frame = ttk.Frame(self.root)
        self.separator_2 = ttk.Separator(self.root,orient=HORIZONTAL)
        self.bottom_frame = ttk.Frame(self.root)

        self.top_frame.pack(fill=X, pady=5)
        self.separator_1.pack(fill=X, padx=10, pady=5)
        self.options_frame.pack(fill=X, pady=5)
        self.separator_2.pack(fill=X, padx=10, pady=5)
        self.bottom_frame.pack(side=BOTTOM, fill=X,pady=5)
                
    def label_toppings(self):
        self.src_label = ttk.Label(self.top_frame, text="Source File: ")
        self.dest_label = ttk.Label(self.top_frame, text="Save To: ")
        self.filename_label = ttk.Label(self.top_frame, text="Save As: ")
        self.src_entry = ttk.Label(self.top_frame, relief='groove', borderwidth=3, anchor=E, textvariable=StringVar().set(self.browser.file))
        self.dest_entry = ttk.Label(self.top_frame, relief='groove', borderwidth=3, anchor=E, textvariable=StringVar().set(self.browser.directory))
        self.src_entry.config(text=self.browser.file)
        self.dest_entry.config(text=self.browser.directory)
        self.Title_label = ttk.Label(self.options_frame, text="Floorplan Title: ")
        self.background_color_label = ttk.Label(self.options_frame, text="Tgml - Background: ")
        self.FontColor_label = ttk.Label(self.options_frame, text="SummaryLine - FontColor: ")
        self.DefaultClickAction_label = ttk.Label(self.options_frame, text="LoadValues - DefaultClickAction: ")
        self.ShowRoomAlarms_label = ttk.Label(self.options_frame, text="LoadValues - ShowRoomAlarms: ")
        self.FontFamily_label = ttk.Label(self.options_frame, text="LoadValues - FontFamily: ")


    def textvariable_filename(self):
        self.browser.save_as = str(self.filename.get())
        if(self.browser.save_as == ''):
            self.browser.save_as = 'export'

    def textvariable_Title(self):
        self.TGML.Title = str(self.Title.get())
        if(self.TGML.Title == ''):
            self.TGML.Title = 'Floorplan Title'

    def textVariable_background_color(self):
        self.TGML.background_color = str(self.background_color.get())
        if(self.TGML.background_color == ''):
            self.TGML.background_color = '#FFFFFF'
        if(self.TGML.background_color[0] != '#'):
            self.TGML.background_color = '#' + self.TGML.background_color

    def textVariable_FontColor(self):
        self.TGML.FontColor = str(self.FontColor.get())
        if(self.TGML.FontColor == ''):
            self.TGML.FontColor = '#000000'
        if(self.TGML.FontColor[0] != '#'):
            self.TGML.FontColor = '#' + self.TGML.FontColor

    def entry_toppings(self):
        #SaveAs filename entry
        self.filename = StringVar()
        self.filename.set(self.browser.save_as)
        self.filename_entry = ttk.Entry(self.top_frame, textvariable=self.filename)
        self.filename_entry.delete(0, END)
        self.filename_entry.insert(0, self.browser.save_as)

        #Tgml background color
        self.Title = StringVar()
        self.Title.set(self.TGML.Title)
        self.Title_entry = ttk.Entry(self.options_frame, textvariable=self.Title)
        self.Title_entry.delete(0, END)
        self.Title_entry.insert(0, self.TGML.Title)

        #Tgml background color
        self.background_color = StringVar()
        self.background_color.set(self.TGML.background_color)
        self.background_color_entry = ttk.Entry(self.options_frame, textvariable=self.background_color)
        self.background_color_entry.delete(0, END)
        self.background_color_entry.insert(0, self.TGML.background_color)

        #SummaryLine FontColor exposed property
        self.FontColor = StringVar()
        self.FontColor.set(self.TGML.FontColor)
        self.FontColor_entry = ttk.Entry(self.options_frame, textvariable=self.FontColor)
        self.FontColor_entry.delete(0, END)
        self.FontColor_entry.insert(0, self.TGML.FontColor)

    def button_toppings(self):
        self.source_button = ttk.Button(self.top_frame, text="Select Source", command=self.browser_browse_file)
        self.output_button = ttk.Button(self.top_frame, text="Select Destination", command=self.browser_change_save_directory)
        self.deliver_pizza_button = ttk.Button(self.bottom_frame, text="Make It Do", command=self.make_it_do)


    def set_DefaulClickAction(self):
        if(str(self.DefaultClickAction_selected.get()) == self.DefaultClickAction_list[0]):
            self.TGML.DefaultClickAction = '0'
        if(str(self.DefaultClickAction_selected.get()) == self.DefaultClickAction_list[1]):
            self.TGML.DefaultClickAction = '1'
        if(str(self.DefaultClickAction_selected.get()) == self.DefaultClickAction_list[2]):
            self.TGML.DefaultClickAction = '2'
        if(str(self.DefaultClickAction_selected.get()) == self.DefaultClickAction_list[3]):
            self.TGML.DefaultClickAction = '3'
        if(str(self.DefaultClickAction_selected.get()) == self.DefaultClickAction_list[4]):
            self.TGML.DefaultClickAction = '4'

    def set_ShowRoomAlarms(self):
        if(str(self.ShowRoomAlarms_selected.get()) == self.ShowRoomAlarms_list[0]):
            self.TGML.ShowRoomAlarms = '0'
        else:
            self.TGML.ShowRoomAlarms = '1'

    def set_FontFamily(self):
        self.TGML.FontFamily = str(self.FontFamily_selected.get())

    def optionmenu_toppings(self):
        #DefaultClickAction
        self.DefaultClickAction_list = ['0 - Default', '1 - Current Work Area', '2 - New Tab', '3 - Floating Window', '4 - Parent']
        self.DefaultClickAction_selected = StringVar()
        self.DefaultClickAction_menu = ttk.OptionMenu(self.options_frame, self.DefaultClickAction_selected, self.DefaultClickAction_list[int(self.TGML.DefaultClickAction)], * self.DefaultClickAction_list)

        #ShowRoomAlarms
        self.ShowRoomAlarms_list = ['Disable', 'Enable']
        self.ShowRoomAlarms_selected = StringVar()
        self.ShowRoomAlarms_selected.set(self.TGML.ShowRoomAlarms)
        self.ShowRoomAlarms_menu = ttk.OptionMenu(self.options_frame, self.ShowRoomAlarms_selected, self.ShowRoomAlarms_list[int(self.TGML.ShowRoomAlarms)],* self.ShowRoomAlarms_list)

        #Font selection menu

        self.FontFamily_list = list(font.families())
        self.FontFamily_list.sort()
        self.FontFamily_list = filter(lambda x: not x.startswith('@'), self.FontFamily_list)
        self.FontFamily_selected = StringVar()
        self.FontFamily_menu = ttk.OptionMenu(self.options_frame, self.FontFamily_selected, self.FontFamily_selected.set(self.TGML.FontFamily), * self.FontFamily_list)

    def place_toppings(self):
        #labels
        self.src_label.grid(row=0, sticky=E, padx=10)
        self.dest_label.grid(row=1, sticky=E, padx=10)
        self.filename_label.grid(row=2, sticky=E, padx=10)
        self.Title_label.grid(row=3, sticky=E, padx=10)
        self.background_color_label.grid(row=4, sticky=E, padx=10)
        self.FontColor_label.grid(row=5, sticky=E, padx=10)
        self.DefaultClickAction_label.grid(row=6, sticky=E, padx=10)
        self.ShowRoomAlarms_label.grid(row=7, sticky=E, padx=10)
        self.FontFamily_label.grid(row=8, sticky=E, padx=10)
        self.src_entry.grid(row=0, column=1, columnspan=4, sticky=E + W)
        self.dest_entry.grid(row=1, column=1, columnspan=4, sticky=E + W)

        #buttons
        self.source_button.grid(row=0, column=5, sticky=EW, padx=10, pady=2)
        self.output_button.grid(row=1, column=5, sticky=EW, padx=10, pady=2)
        self.deliver_pizza_button.grid(column=1, sticky=EW, padx=5, pady=2)

        #entries
        self.filename_entry.grid(row=2, column=1, columnspan=4, sticky=EW, pady=2)
        self.Title_entry.grid(row=3, column=1, sticky=E + W, padx=10, pady=2)
        self.background_color_entry.grid(row=4, column=1, sticky=EW, padx=10, pady=2)
        self.FontColor_entry.grid(row=5, column=1, sticky=E + W, padx=10, pady=2)

        #optionmenus
        self.DefaultClickAction_menu.grid(row=6, column=1, sticky=E + W, padx=10, pady=2)
        self.ShowRoomAlarms_menu.grid(row=7, column=1, sticky=E + W, padx=10, pady=2)
        self.FontFamily_menu.grid(row=8, column=1, sticky=E + W, padx=10, pady=2)

    def deliver_pizza(self):
        Grid.columnconfigure(self.top_frame, 1, weight=1)
        Grid.columnconfigure(self.options_frame, 1, weight=1)
        Grid.columnconfigure(self.bottom_frame, 1, weight=1)
        self.root.update_idletasks()
        self.root.mainloop()
        self.root.protocol('WM_DELETE_WINDOW', sys.exit())


    def bindings_operate(self):
        self.textvariable_filename()
        self.textvariable_Title()
        self.textVariable_background_color()
        self.textVariable_FontColor()
        self.set_DefaulClickAction()
        self.set_ShowRoomAlarms()
        self.set_FontFamily()

    def make_it_do(self):
        self.bindings_operate()
        self.TGML.go_go_gadget(self.browser.file, self.browser)
        messagebox.showinfo('Pizza Delivered!', self.browser.save_as + ' ==>> delivered!')
        sys.exit()

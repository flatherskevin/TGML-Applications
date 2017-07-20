from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from SETTINGS import *
from baking_time import *
import os
import csv

root = Tk()
style = ttk.Style()
style.theme_use('vista')
root.columnconfigure(0, weight=1)
root.minsize(width=300, height=200)
root.maxsize(width=900, height=200)
root.wm_title(NAME + ' ' + VERSION)
root.iconbitmap(ICON)

top_frame = ttk.Frame(root)
separator_1 = ttk.Separator(root, orient=HORIZONTAL)
options_frame = ttk.Frame(root)
separator_2 = ttk.Separator(root, orient=HORIZONTAL)
bottom_frame = ttk.Frame(root)
top_frame.pack(fill=X, pady=5)
separator_1.pack(fill=X, padx=10, pady=5)
options_frame.pack(fill=X, pady=5)
separator_2.pack(fill=X, padx=10, pady=5)
bottom_frame.pack(side=BOTTOM, fill=X,pady=5)

cookie_ingredients_file = r'Cookie Ingredients.csv'

headers = ['Group','Position','Title','Subtitle','Point Bind','Point Type','Bind Value','Bind Alarm','Units','Decimals','Digital Off','Digital On','Multistate Text','Viconics','Analog Conversion','Conversion Input Min','Conversion Input Max','Conversion Output Min','Conversion Output Max','Text Align','ToolTip Text','ToolTip Font Size','ToolTip Font Stroke','ToolTip Fill','ToolTip Enable']

save_directory = os.path.expanduser('~/Desktop')
save_as = 'Cookies'

with open(cookie_ingredients_file, 'w') as file:
	file.truncate()
	writer = csv.writer(file, delimiter=',')
	writer.writerow(headers)


def change_ingredients():
	os.startfile(cookie_ingredients_file)

def change_save_directory():
	global save_directory
	save_directory = filedialog.askdirectory(initialdir=save_directory)
	dest_entry.config(text=save_directory)

def change_filename():
	global save_as
	save_as = str(filename.get())
	if save_as == '':
		save_as = 'Cookies'

def bake():
	for style_type in styles_list:
		if str(styles_selected.get()) == style_type:
			global chosen_style
			chosen_style = styles_list.index(style_type)
	change_filename()
	#When more styles are created, they simply need to be added here
	if chosen_style == 1:
		baking_time(style='mit', file_name=save_as, save_directory=save_directory)
	else:
		baking_time(style='standard', file_name=save_as, save_directory=save_directory)
	messagebox.showinfo('Cookies Served!', 'Enjoy!')
	sys.exit()

dest_label = ttk.Label(top_frame, text="Save To: ")
dest_label.grid(row=1, column=1, sticky=E, padx=10)
dest_entry = ttk.Label(top_frame, relief='groove', borderwidth=3, anchor=E, text=save_directory, textvariable=StringVar().set(save_directory))
dest_entry.grid(row=1, column=2, sticky=E+W)
filename_label = ttk.Label(top_frame, text="Save As: ")
filename_label.grid(row=2, column=1, sticky=E, padx=10)
filename = StringVar()
filename.set(save_as)
filename_entry = ttk.Entry(top_frame, textvariable=filename)
filename_entry.delete(0, END)
filename_entry.insert(0, save_as)
filename_entry.grid(row=2, column=2, columnspan=4, sticky=EW, pady=2)

ingredients_button = ttk.Button(options_frame, text="Change Ingredients", command=lambda: change_ingredients())
ingredients_button.grid(row=1, column=1, sticky=EW, padx=10, pady=2)

chosen_style = 0
styles_list = ['Standard', 'MIT']
styles_selected = StringVar()
styles_selected.set(chosen_style)
styles_menu = ttk.OptionMenu(options_frame, styles_selected, styles_list[chosen_style],* styles_list)
styles_menu.grid(row=2, column=1, sticky=EW, padx=10, pady=2)

output_button = ttk.Button(top_frame, text="Select Destination", command=lambda: change_save_directory())
output_button.grid(row=1, column=3, sticky=EW, padx=10, pady=2)

bake_cookies_button = ttk.Button(bottom_frame, text="Make It Do", command=lambda: bake())
bake_cookies_button.grid(column=1, sticky=EW, padx=10, pady=2)


Grid.columnconfigure(top_frame, 1, weight=1)
Grid.columnconfigure(options_frame, 1, weight=1)
Grid.columnconfigure(bottom_frame, 1, weight=1)
root.update_idletasks()
root.mainloop()
root.protocol('WM_DELETE_WINDOW', sys.exit())
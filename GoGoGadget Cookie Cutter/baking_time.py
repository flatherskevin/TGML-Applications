from TGML.Tgml import *
from TGML.Metadata import *
from TGML.Group import *
from TGML.Custom.UniversalPoint.Styles.Standard import Standard
from TGML.Custom.UniversalPoint.Styles.MITTitle import MITTitle
from TGML.Custom.UniversalPoint.Styles.MITSubtitle import MITSubtitle
import csv, os, sys, traceback, datetime
from SETTINGS import *


def baking_time(style='standard', file_name='Cookies', save_directory=os.path.expanduser('~/Desktop')):
	cookie_sheet = Tgml('Tgml', input_type='blank')
	group_list = []
	with open('Cookie Ingredients.csv', newline='') as file:
		reader = csv.DictReader(file)

		#Initialize blank lists for later use
		snickerdoodle_tray = []
		

		#Default left positioning in graphic
		position_left = 300

		#Let's loop through the excel sheet and get cooking!
		for count,row in enumerate(reader):
			try:
				#Group and Position must be integers
				snickerdoodle = None
				assert int(row['Group'])
				assert int(row['Position'])

				#Create a style of the UP
				if style == 'mit':
					if int(row['Position']) == 1:
						#Create a MIT title style UniversalPoint
						snickerdoodle = MITTitle()
					else:
						#Create a MIT subtitle style UniversalPoint
						snickerdoodle = MITSubtitle()
				else:
					#Create a standard style UniversalPoint
					snickerdoodle = Standard()

				#Metadata tag add with tool info for future reference
				metadata = Metadata('Metadata', input_type='blank')
				metadata.properties['Name'] = 'Creation Info'
				date = datetime.datetime.now()
				metadata.properties['Value'] = 'Created on {date} using {name} - {version}'.format(name=NAME, version=VERSION, date=date.strftime('%B %d, %Y'))
				metadata.compile()
				snickerdoodle.element.append(metadata.element)

				#Position UPs dependent on Group and Position
				#Some styles may need these specially taylored to their Height and Width
				snickerdoodle.properties['Top'] = str(eval(row['Position']) * 25 + (eval(row['Group']) - 1) * 200)
				snickerdoodle.properties['Left'] = str(position_left)

				#Set all exposed properties for the snickerdoodle, but ignore blanks, Group, Position, Title, and Subtitle
				for col in row:
					if row[col] not in ['', 'Group', 'Position', 'Title']:
						snickerdoodle.exposed_properties[col.replace(' ', '')] = row[col]

				#Set Title exposed property only if it is in Position 1		
				if row['Position'] == '1':
					snickerdoodle.exposed_properties['Title'] = row['Title']
				else:
					if style != 'mit':
						snickerdoodle.exposed_properties['Title'] = ''

				#Used later for inserting into a group
				snickerdoodle_tray.append([snickerdoodle, row['Group']])
				group_list.append(row['Group'])

				#Compile the snickerdoodles
				snickerdoodle.compile()
			except Exception as err:
				traceback.print_exc(file=sys.stdout)
		#Find all unique groups to loop through
		group_set = set(group_list)
		for group in group_set:
			temp_list = []

			#Find snickerdoodles that are part of the same group
			for package in snickerdoodle_tray:
				if package[1] == group:
					temp_list.append(package[0])

			#Create a blank Group Tgml item and loop through temp_list to put related snickerdoodles in
			cookie_jar = Group('Group')
			for snickerdoodle in temp_list:
				cookie_jar.element.append(snickerdoodle.element)

			#Append the cookie_jar groups to the Tgml
			cookie_sheet.element.append(cookie_jar.element)

	#MIT uses #FFFFFF font color, so making the background #1A1A1A helps with visibility
	if style == 'mit':
		cookie_sheet.properties['Background'] = '#1A1A1A'

	#Setup some arbitrary Tgml page sizes
	cookie_sheet.properties['Height'] = str((eval(group_list[-1]) + 1 ) * 200)
	cookie_sheet.properties['Width'] = '1670'

	#As always, compile the Tgml object
	cookie_sheet.compile()

	#Write to file to specified save_directory with the desired name
	cookie_sheet.write_to_file(save_directory, file_name)
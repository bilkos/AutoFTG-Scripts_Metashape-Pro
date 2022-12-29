import os
from os import path
import sys
import time

from configparser import ConfigParser

appsettingsVer = "5"
appSettingsFile = 'autoftg_settings.ini'
# Set path to camera settings INI file. Use the same location as scripts for Metashape.
appdataPath = os.path.expanduser('~\AppData\Local\Agisoft\Metashape Pro\scripts\AutoFTG\\').replace("\\", "/")
appSettingsPath =  appdataPath + appSettingsFile
appSettingsFileExists = os.path.isfile(appSettingsPath)	# Check if settings file exists

appCfg = ConfigParser()


def appSettingsCheck():
	if appSettingsFileExists == False:
		print("No settings file? New file with default values will be created...")
		appCfg.add_section('Settings')
		appCfg.set('Settings', 'settings_version', appsettingsVer)
		appCfg.set('Settings', 'folder_project', '')
		appCfg.set('Settings', 'folder_data', '')
		appCfg.set('Settings', 'default_camera', 'NULL - Frame (Default)')
		appCfg.add_section('Chunk Names')
		appCfg.set('Chunk Names', 'kalota_prefix', '')
		appCfg.set('Chunk Names', 'kalota_suffix', '')
		appCfg.set('Chunk Names', 'stopnica_izkop_prefix', '')
		appCfg.set('Chunk Names', 'stopnica_izkop_suffix', '_IZ')
		appCfg.set('Chunk Names', 'stopnica_beton_prefix', '')
		appCfg.set('Chunk Names', 'stopnica_beton_suffix', '_ST_BB')

		# Writing our configuration file to 'example.cfg'
		with open(appSettingsPath, 'w') as configfile:
		    appCfg.write(configfile)


appCfg.read('example.cfg')

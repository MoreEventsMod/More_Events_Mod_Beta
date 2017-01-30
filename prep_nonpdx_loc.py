#####################################################################
# prep_nonpdx_loc.py
# By Tim Zerrell (LamilLerran)
# Creates the appropriate localisation files for a release in a
# language other than one of the standard Paradox languages. 
#####################################################################

#If you don't know how to get started using this script, start with:
#python prep_nonpdx_loc.py --help
#from the command line of this directory.
#You will need to have python installed.

import os, sys, getopt

#default to using "English" as the proxy language
overwriteLanguage = 'l_english'

#print a warning if no source language set, so leave empty for now
sourceLanguage = None

#delete files in other localisations
deleteExtraLanguages = True

try:
	options, extraargs = getopt.getopt(sys.argv[1:], "hko:s:",["help","keep-extra","overwrite=","source="])
except getopt.GetoptError:
	print('Invalid argument syntax in ' + sys.argv[0])
	print('Valid arguments are -h, --help, -s, --source=, -o, --overwrite, -k, --keep-extra')
	sys.exit(47)
for opt, val in options:
	if opt in ("-h", "--help"):
		print("-h, --help :")
		print("    See this help information.")
		print("-s, --source= :")
		print("    The language to be released")
		print("    e.g. -s l_chinese")
		print("-o, --overwrite= :")
		print("    The proxy language the localisation files will be placed in.")
		print("    Defaults to English as that's what most main game translation")
		print("    mods are released using as the language to be selected.")
		sys.exit(0)
	elif opt in ("-o", "--overwrite"):
		overwriteLanguage = val
		print('Setting overwritten language to ' + val)
	elif opt in ("-s", "--source"):
		sourceLanguage = val
		print('Setting source language to ' + val)
	elif opt in ("-k", "--keep-extra"):
		deleteExtraLanguages = False
if (sourceLanguage == None):
	print('/!\ WARNING: No source language set.')
	sourceLanguage = 'l_chinese'
	print('Defaulting to source language: ' + sourceLanguage)

for filename in os.listdir('localisation')[:]:
	if (filename.count(overwriteLanguage) > 0):
		continue
	elif (filename.count(sourceLanguage) == 0 and deleteExtraLanguages):
		os.remove('localisation/' + filename)
		continue
	with open('localisation/' + filename, 'r', encoding="utf-8") as sourceFile:
		newFilename = filename.replace(sourceLanguage, overwriteLanguage)
		with open('localisation/' + newFilename, 'w+', encoding="utf-8") as targetFile:
			for line in sourceFile:
				targetFile.write(line.replace(sourceLanguage + ':', overwriteLanguage + ':'))
			targetFile.close()
			sourceFile.seek(0)
	os.remove('localisation/' + filename)
print(sourceLanguage + ' placed in ' + overwriteLanguage + ' loc files.')
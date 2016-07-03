#####################################################################
# copy_english.py
# By Tim Carrell (LamilLerran)
# Copies English into localization files for other languages
#####################################################################

#If you don't know how to get started using this script, start with:
#python copy_english.py --help
#from the command line of this directory.
#You will need to have python installed.

import os, sys, getopt

#default to exporting from English to all other languages and not overwriting pre-existing files
allLanguages = {'l_braz_por', 'l_english', 'l_french', 'l_german', 'l_polish', 'l_russian', 'l_spanish'}
sourceLanguage = 'l_english'
ignoreLanguages = set([])
overwrite = False

try:
	options, extraargs = getopt.getopt(sys.argv[1:], "hi:os:",["help","ignore=","overwrite","source="])
except getopt.GetoptError:
	print('Invalid argument syntax in ' + sys.argv[0])
	print('Valid arguments are -h, --help, -i, --ignore=, -o, --overwrite, -s, --source=')
	sys.exit(47)
for opt, val in options:
	if opt in ("-i", "--ignore"):
		ignoreLanguages = set(val.split(","))
		print('Ignoring the following languages:')
		print(ignoreLanguages)
	elif opt in ("-h", "--help"):
		print("-h, --help :")
		print("    See this help information.")
		print("-i, --ignore= :")
		print("    A comma-separated list of languages to not export to")
		print("    e.g. -i l_braz_por,l_french")
		print("-o, --overwrite :")
		print("    If this option is set, will overwrite all localisation files in")
		print("    non-ignored, non-source languages (even if they already exist).")
		print("-s, --source= :")
		print("    The language to export from. Default is l_english.")
		sys.exit(0)
	elif opt in ("-o", "--overwrite"):
		overwrite = True
		print('Overwriting existing files.')
	elif opt in ("-s", "--source"):
		sourceLanguage = val
		print('Setting source language to ' + val)
targetLanguages = allLanguages - ignoreLanguages - set([sourceLanguage])

for filename in os.listdir('localisation')[:]:
	sourceFile = open('localisation/' + filename, 'r')
	for target in targetLanguages:
		newFilename = filename.replace(sourceLanguage, target)
		if newFilename == filename: continue	#Only copy files that actually contained l_english
		if os.path.isfile('localisation/' + newFilename) and not overwrite: continue
		targetFile = open('localisation/' + newFilename, 'w+')
		for line in sourceFile:
			targetFile.write(line.replace(sourceLanguage + ':', target + ':'))
		targetFile.close()
		sourceFile.seek(0)
print(sourceLanguage + ' localisation export complete.')
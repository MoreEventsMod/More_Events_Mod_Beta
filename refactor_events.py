#####################################################################
# refactor_events.py
# By Tim Carrell (LamilLerran)
# Renames events to separate each event chain into its own file.
# Note that this *only* renames the events, it does not move them
# into new files or give the appropriate namespace
#####################################################################

#If you don't know how to get started using this script, start with:
#python refactor_events.py --help
#from the command line of this directory.
#You will need to have python installed.

import os, sys, getopt, re

#default to exporting from English to all other languages and not overwriting pre-existing files
#allLanguages = {'l_braz_por', 'l_english', 'l_french', 'l_german', 'l_polish', 'l_russian', 'l_spanish'}
#sourceLanguage = 'l_english'
#ignoreLanguages = set([])
#overwrite = False

try:
	#options, extraargs = getopt.getopt(sys.argv[1:], "hi:os:",["help","ignore=","overwrite","source="])
	options, extraargs = getopt.getopt(sys.argv[1:], "h",["help"])
except getopt.GetoptError:
	print('Invalid argument syntax in ' + sys.argv[0])
	#print('Valid arguments are -h, --help, -i, --ignore=, -o, --overwrite, -s, --source=')
	print('Valid arguments are -h, --help')
	sys.exit(47)
#for opt, val in options:
#	if opt in ("-i", "--ignore"):
#		ignoreLanguages = set(val.split(","))
#		print('Ignoring the following languages:')
#		print(ignoreLanguages)
#	elif opt in ("-h", "--help"):
#		print("-h, --help :")
#		print("    See this help information.")
#		print("-i, --ignore= :")
#		print("    A comma-separated list of languages to not export to")
#		print("    e.g. -i l_braz_por,l_french")
#		print("-o, --overwrite :")
#		print("    If this option is set, will overwrite all localisation files in")
#		print("    non-ignored, non-source languages (even if they already exist).")
#		print("-s, --source= :")
#		print("    The language to export from. Default is l_english.")
#		sys.exit(0)
#	elif opt in ("-o", "--overwrite"):
#		overwrite = True
#		print('Overwriting existing files.')
#	elif opt in ("-s", "--source"):
#		sourceLanguage = val
#		print('Setting source language to ' + val)
#targetLanguages = allLanguages - ignoreLanguages - set([sourceLanguage])

#for filename in os.listdir('localisation')[:]:
#	sourceFile = open('localisation/' + filename, 'r')
#	for target in targetLanguages:
#		newFilename = filename.replace(sourceLanguage, target)
#		if newFilename == filename: continue	#Only copy files that actually contained l_english
#		if os.path.isfile('localisation/' + newFilename) and not overwrite: continue
#		targetFile = open('localisation/' + newFilename, 'w+')
#		for line in sourceFile:
#			targetFile.write(line.replace(sourceLanguage + ':', target + ':'))
#		targetFile.close()
#		sourceFile.seek(0)
#print(sourceLanguage + ' localisation export complete.')

sourceNames = [
	"paul\.(?=[1-6][^0-9])",
	"paul\.(?=((1[0-9])|(2[01])|(3[0-6])))",
] #TODO
10,11,12,13,14,15,16,17,18,19,20,21,30,31,32,33,34,35,36
goalNames = [
	"star-survey.",
	"elusive-carcosa."
] #TODO
directories = [
	"events"
] #TODO

for src, goal in zip(sourceNames,goalNames):
	for dir in directories:
		for filename in os.listdir(dir)[:]:		#TODO: Will this search subdirectories?
			try:
				with open(dir + '/' + filename, 'r') as file, open(dir + '/' + filename + '-temp', 'w') as bufferfile:
					for line in file:
						linebuffer, count = re.subn(src, goal, line)
						if count != 0: print(count, " in ", line, " in ", filename)
						bufferfile.write(linebuffer)
						#bufferfile.write(re.sub(src, goal, line))
			except OSError:
				print("Error during file IO.")
				print("with '" + dir + '/' + filename + "' or '" + dir + '/' + filename + '-temp' + "'.")
				continue
			os.remove(dir + '/' + filename)
			os.rename(dir + '/' + filename + '-temp', dir + '/' + filename)
			
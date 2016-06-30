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

verbose = False

try:
	#options, extraargs = getopt.getopt(sys.argv[1:], "hi:os:",["help","ignore=","overwrite","source="])
	options, extraargs = getopt.getopt(sys.argv[1:], "hv",["help", "verbose"])
except getopt.GetoptError:
	print('Invalid argument syntax in ' + sys.argv[0])
	#print('Valid arguments are -h, --help, -i, --ignore=, -o, --overwrite, -s, --source=')
	print('Valid arguments are -h, --help, -v, --verbose')
	sys.exit(47)
for opt, val in options:
	if opt in ("-h", "--help"):
		print("help does not yet exist. Sorry :(")
		sys.exit(0)
	elif opt in ("-v", "--verbose"):
		verbose = True
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
	"ef_debug\.(?=[12])",
	"ef_temp\.(?=[1-4])",
	"mem_anomaly_event\.(?=[1-5][^0-9])",
	"mem_anomaly_event\.(?=7[^0-9])",
	"mem_anomaly_event\.(?=6[^0-9])",
	"mem_anomaly_event\.(?=10[2-3][^0-9])",
	"mem_anomaly_event\.(?=8[^0-9])",
	"mem_anomaly_event\.(?=10[0-1][^0-9])",
	"mem_anomaly_event\.(?=10[^0-9])",
	"mem_anomaly_event\.(?=1[1-2][^0-9])",
	"mem_anomaly_failure\.(?=[1-2][^0-9])",
	"mem_anomaly_failure\.(?=3[^0-9])",
	"mem_anomaly_failure\.(?=[5-6][^0-9])",
	"mem_anomaly_failure\.102[^0-9]",
	"mem_anomaly_failure\.(?=4[^0-9])",
	"mem_anomaly_failure\.100[^0-9]",
	"mem_anomaly_failure\.(?=10[^0-9])",
	"mem_anomaly_failure\.(?=11[^0-9])",
	"mem_dead_star_event\.(?=[1-3])",
	"mem_demon_ship_event\.(?=[1-9])",
	"mem_dimensional_rift_event\.(?=[1-2])",
	"mem_ll_misc_event\.(?=1[^0-9])",
	"mem_sciencecon_event\.(?=9[1-3][^0-9]|[1-2][0-9][0-9][^0-9]|3[0-7][0-9][^0-9]|380[^0-9])",
	"mem_sciencecon_event\.(?=[1-8][^0-9]|1[1-2][^0-9]|999[^0-9])",
	"spiritualists_pilgrimage\.(?=[1-9][^0-9]|1[0-9][^0-9]|2[0-3][^0-9])",
	"squid\.(?=[1-6][^0-9])",
	"squid\.(?=7[^0-9])",
	"squid\.(?=[8-9][^0-9])",
] #TODO
goalNames = [
	"mem-star-survey.",
	"mem-elusive-carcosa.",
	"mem-enterprise-fallen-debug.",
	"mem-enterprise-fallen.",
	"mem-black-hole.",
	"mem-dimensional-rift.",
	"mem-dead-star.",
	"mem-mysterious-pyramids.",
	"mem-lost-zoo.",
	"mem-poisoned-world.",
	"mem-asteroid-structure.",
	"mem-crashed-object.",
	"mem-brainworm.10",
	"mem-demon-ship.10",
	"mem-dimensional-rift.10",
	"mem-mysterious-pyramids.202",
	"mem-dead-star.",
	"mem-poisoned-world.200",
	"mem-asteroid-structure.",
	"mem-crashed-object.",
	"mem-dead-star.",
	"mem-demon-ship.",
	"mem-dimensional-rift.",
	"mem-lost-zoo.",
	"mem-science-convention.",
	"mem-science-convention.",
	"mem-spiritualists-pilgrimage.",
	"mem-eager-traders.",
	"mem-imperialist-intimidation.",
	"mem-music-tour.",
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
						linebuffer, subsMade = re.subn(src, goal, line)
						if (verbose and subsMade != 0): 
							print(subsMade, " substitutions in ", filename, " to line")
							print(line)
						bufferfile.write(linebuffer)
			except OSError:
				print("Error during file IO.")
				print("with '" + dir + '/' + filename + "' or '" + dir + '/' + filename + '-temp' + "'.")
				continue
			os.remove(dir + '/' + filename)
			os.rename(dir + '/' + filename + '-temp', dir + '/' + filename)
			
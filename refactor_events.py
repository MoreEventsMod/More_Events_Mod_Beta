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

verbose = False

try:
	options, extraargs = getopt.getopt(sys.argv[1:], "hv",["help", "verbose"])
except getopt.GetoptError:
	print('Invalid argument syntax in ' + sys.argv[0])
	print('Valid arguments are -h, --help, -v, --verbose')
	sys.exit(47)
for opt, val in options:
	if opt in ("-h", "--help"):
		print("-h, --help:")
		print("\tPrint this text and exit.")
		print("-v", "--verbose")
		print("\tPrint a message for each substitution made.")
		sys.exit(0)
	elif opt in ("-v", "--verbose"):
		verbose = True
		
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
]
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
]
directories = [
	"events",
	"localisation",
	"common/anomalies",
	"common/event_chains",
	"common/on_actions",
	"common/opinion_modifiers",
	"common/static_modifiers",
	"common/traits",
]

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
			
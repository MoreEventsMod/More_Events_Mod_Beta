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
		
sourceNames = [
	"paul\.(?=[1-6](?![0-9]))",
	"paul\.(?=((1[0-9])|(2[01])|(3[0-6])))",
	"ef_debug\.(?=[12])",
	"ef_temp\.(?=[1-4])",
	"mem_anomaly_event\.(?=[1-5](?![0-9]))",
	"mem_anomaly_event\.(?=7(?![0-9]))",
	"mem_anomaly_event\.(?=6(?![0-9]))",
	"mem_anomaly_event\.(?=10[2-3](?![0-9]))",
	"mem_anomaly_event\.(?=8(?![0-9]))",
	"mem_anomaly_event\.(?=10[0-1](?![0-9]))",
	"mem_anomaly_event\.(?=10(?![0-9]))",
	"mem_anomaly_event\.(?=1[1-2](?![0-9]))",
	"mem_anomaly_failure\.(?=[1-2](?![0-9]))",
	"mem_anomaly_failure\.(?=3(?![0-9]))",
	"mem_anomaly_failure\.(?=[5-6](?![0-9]))",
	"mem_anomaly_failure\.102(?![0-9])",
	"mem_anomaly_failure\.(?=4(?![0-9]))",
	"mem_anomaly_failure\.100(?![0-9])",
	"mem_anomaly_failure\.(?=10(?![0-9]))",
	"mem_anomaly_failure\.(?=11(?![0-9]))",
	"mem_dead_star_event\.(?=[1-3])",
	"mem_demon_ship_event\.(?=[1-9])",
	"mem_dimensional_rift_event\.(?=[1-2])",
	"mem_ll_misc_event\.(?=1(?![0-9]))",
	"mem_sciencecon_event\.(?=9[1-3](?![0-9])|[1-2][0-9][0-9](?![0-9])|3[0-7][0-9](?![0-9])|380(?![0-9]))",
	"mem_sciencecon_event\.(?=[1-8](?![0-9])|1[1-2](?![0-9])|999(?![0-9]))",
	"(?<!mem_)spiritualists_pilgrimage\.(?=[1-9](?![0-9])|1[0-9](?![0-9])|2[0-3](?![0-9]))",
	"squid\.(?=[1-6](?![0-9]))",
	"squid\.(?=7(?![0-9]))",
	"squid\.(?=[8-9](?![0-9]))",
	"(?<!_)mem_brainworm_event\.(?=[1-9])",
	"ef_temp_category",
	"key = mem_black_hole_1(?![_\.])",
	#"mem_demon_ship_category",
	#"mem_dimensional_rift_category",
	#"mem_mysterious_pyramids_category",
	#"mem_dead_star_category",
	#"mem_poisoned_world_category",
	"asteroid_structure_network",
	"(?<!_)crashed_object",
	
	"paul_star_chain",
	"paul_stars_surveyed",
	"paul_carcosa_hunt",
	"paul_sightings_checked",
	"paul_powerplant_tuning",
	"paul_star_pictures",
	"(?<!_)A_STAR_SURVEY",
	"(?<!_)K_STAR_SURVEY",
	"(?<!_)M_STAR_SURVEY",
	"(?<!_)RARE_STAR_SURVEY",
	"(?<!_)CHASE_CARCOSA",
	"(?<!_)CARCOSA_HUNT_",
	"(?<!_)CARCOSA_QUANTUM_COMPUTER",
	"(?<!_)EF_TEMP_PROJECT",
	#"MEM_BLACK_HOLE_1_PROJECT",
	#"MEM_DEMON_SHIP_PROJECT",
	#"MEM_DIMENSIONAL_RIFT_PROJECT",
	#"MEM_LOST_ZOO_PROJECT",	"paul_(?=star_pictures|powerplant_tuning|carcosa_ignore|carcosa_influence|carcosa_mineral|carcosa_physics|carcosa_upkeep|carcosa_sociology|carcosa_happy|carcosa_energy)",
	"(?<!_)boldly_going",
	"(?<!_)malicious_joy",
	"(?<!_)booming_economy",
	"(?<!_)busted_economy",
	"(?<!_|s)pleased_by_custom_event",
	"(?<!_)displeased_by_custom_event",
	"(?<!_)holy_order_established",
	"(?<!_)volunteer_surge",
	"(?<!_)united_front",
	"(?<!_)united_in_prayer",
	"(?<!_)foreign_(?=star_on_tour|star_denied_entry|rockstar_filth_banned|rockstar_peace_love)",
	"(?<!_)less_play_more_work",
	"(?<!_)strange_guests",
	"(?<!_)powering_abandoned_station",
	"(?<!_)supernova_celebration",
	"(?<!_)supernova_mourning",
	"(?<!_)trait_(?=redefined_productivity|redefined_happiness)",
	"paul_opinion_trustworthy",
	"(?<!_)opinion_(?=allowed_merchant_access|refused_merchant_access|mutual_scam|peaceful_trade|very_pleased_pilgrims|pleased_pilgrims|bad_hosts|assassins|accused_of_terrorism)",
	"(?<!_)opinion_mem_(?=sciencecon_fantastic_time|sciencecon_good_time|sciencecon_waste_of_time)",
	"opinion_mem_sciencecon_sciencetist_dead",
	"(?<!_)mem_sciencecon(?=\.[0-9])",
	"(?<!_)mem_opinion_sciencecon",
	
	"(?<!mem_)castle.dds",
	"(?<!mem_)pm_foreign_star.dds",
	"(?<!mem_)pm_Graph_Down.dds",
	"(?<!mem_)pm_Graph_Up.dds",
	"(?<!mem_)pm_holy_order.dds",
	"(?<!mem_)pm_united_front.dds",
	"(?<!mem_)pm_united_in_prayer.dds",
	"(?<!mem_)preacher.dds",
	"(?<!mem_)purple-light.dds",
	"(?<!mem_)work.dds",
	"trait_mem_redefined_happiness.dds",
	"trait_mem_redefined_productivity.dds",
	"(?<!mem_)rockstar_origin",
	"(?<!mem_)tour_location",
	"(?<!mem_)(?=(rock|dubstep|incomprehensible|rapper|festival|metal)flag)",
]

goalNames = [
	"mem_star_survey.",
	"mem_elusive_carcosa.",
	"mem_enterprise_fallen_debug.",
	"mem_enterprise_fallen.",
	"mem_black_hole_1.",
	"mem_dimensional_rift.",
	"mem_dead_star.",
	"mem_mysterious_pyramids.",
	"mem_lost_zoo.",
	"mem_poisoned_world.",
	"mem_asteroid_structure.",
	"mem_crashed_object.",
	"mem_brainworm.10",
	"mem_demon_ship.10",
	"mem_dimensional_rift.10",
	"mem_mysterious_pyramids.202",
	"mem_dead_star.",
	"mem_poisoned_world.200",
	"mem_asteroid_structure.",
	"mem_crashed_object.",
	"mem_dead_star.",
	"mem_demon_ship.",
	"mem_dimensional_rift.",
	"mem_lost_zoo.",
	"mem_science_convention.",
	"mem_science_convention.",
	"mem_spiritualists_pilgrimage.",
	"mem_eager_traders.",
	"mem_imperialist_intimidation.",
	"mem_music_tour.",
	"mem_brainworm.",
	"mem_enterprise_fallen_category",
	"key = mem_black_hole_1_category",
	#"mem_demon_ship_category",
	#"mem_dimensional_rift_category",
	#"mem_mysterious_pyramids_category",
	#"mem_dead_star_category",
	#"mem_poisoned_world_category",
	"mem_asteroid_computer_category",
	"mem_asteroid_structure_category",
	"mem_crashed_object_category",
	
	"mem_star_survey_chain",
	"mem_stars_surveyed",
	"mem_elusive_carcosa_hunt_chain",
	"mem_carcosa_sightings_checked",
	"mem_star_survey_powerplant_tuning",
	"mem_star_survey_star_pictures",
	"MEM_A_STAR_SURVEY",
	"MEM_K_STAR_SURVEY",
	"MEM_M_STAR_SURVEY",
	"MEM_RARE_STAR_SURVEY",
	"MEM_CHASE_CARCOSA",
	"MEM_CARCOSA_HUNT_",
	"MEM_CARCOSA_QUANTUM_COMPUTER",
	"MEM_ENTERPRISE_FALLEN_PROJECT",
	#"MEM_BLACK_HOLE_1_PROJECT",
	#"MEM_DEMON_SHIP_PROJECT",
	#"MEM_DIMENSIONAL_RIFT_PROJECT",
	#"MEM_LOST_ZOO_PROJECT",	"paul_(?=star_pictures|powerplant_tuning|carcosa_ignore|carcosa_influence|carcosa_mineral|carcosa_physics|carcosa_upkeep|carcosa_sociology|carcosa_happy|carcosa_energy)",
	"mem_boldly_going",
	"mem_malicious_joy",
	"mem_booming_economy",
	"mem_busted_economy",
	"mem_pleased_by_custom_event",
	"mem_displeased_by_custom_event",
	"mem_holy_order_established",
	"mem_volunteer_surge",
	"mem_united_front",
	"mem_united_in_prayer",
	"mem_foreign_",
	"mem_less_play_more_work",
	"mem_strange_guests",
	"mem_powering_abandoned_station",
	"mem_supernova_celebration",
	"mem_supernova_mourning",
	"trait_mem_",
	"mem_opinion_trustworthy",
	
	"mem_opinion_",
	"mem_opinion_",
	"mem_opinion_science_convention_scientist_dead",
	"mem_science_convention",
	"mem_opinion_science_convention",
	
	"mem_castle.dds",
	"mem_pm_foreign_star.dds",
	"mem_pm_Graph_Down.dds",
	"mem_pm_Graph_Up.dds",
	"mem_pm_holy_order.dds",
	"mem_pm_united_front.dds",
	"mem_pm_united_in_prayer.dds",
	"mem_preacher.dds",
	"mem_purple-light.dds",
	"mem_work.dds",
	"trait_mem_redefined_happiness.dds",
	"trait_mem_redefined_productivity.dds",
	"mem_rockstar_origin",
	"mem_tour_location",
	"mem_",
]
directories = [
	"events",
	"localisation",
	"common/special_projects",
	"common/anomalies",
	"common/event_chains",
	"common/on_actions",
	"common/opinion_modifiers",
	"common/static_modifiers",
	"common/traits",
]

try:
	options, extraargs = getopt.getopt(sys.argv[1:], "hvg:s:",["help", "verbose", "goal=", "source="])
except getopt.GetoptError:
	print('Invalid argument syntax in ' + sys.argv[0])
	print('Valid arguments are -h, --help, -v, --verbose')
	sys.exit(1)
print("Options: ", options)
try:
	for opt, val in options:
		if opt in ("-h", "--help"):
			print("-h, --help:")
			print("\tPrint this text and exit.")
			print("-v", "--verbose")
			print("\tPrint a message for each substitution made.")
			print("-g", "--goal=")
			print("\tSet text file for new names to use. Don't use without -s")
			print("-s", "--source=")
			print("\tSet text file for names to replace. Uses regex. Don't use without -g")
			sys.exit(0)
		elif opt in ("-v", "--verbose"):
			verbose = True
		elif opt in ("-s", "--source"):
			with open(val) as sFile:
				del sourceNames[:]
				sourceNames = [line.rstrip('\n') for line in sFile]
				print("Loading source names from " + opt)
		elif opt in ("-g", "--goal"):
			with open(val) as gFile:
				del goalNames[:]
				goalNames = [line.rstrip('\n') for line in gFile]
				print("Loading goal names from " + opt)
		else:
			print("Bad argument '", opt,"'; aborting.")
			sys.exit(2)
except: #quit on any error
	print("Error processing arguments; aborting")
	sys.exit(3)

if verbose:
	for dir in directories:
		for filename in os.listdir(dir)[:]:
			print(filename)

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
			
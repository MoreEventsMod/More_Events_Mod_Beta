import os

allLanguages = {'l_braz_por', 'l_english', 'l_french', 'l_german', 'l_polish', 'l_russian', 'l_spanish'}
sourceLanguage = 'l_english'
ignoreLanguages = set([])
overwrite = False

targetLanguages = allLanguages - ignoreLanguages - set([sourceLanguage])

for filename in os.listdir('localisation')[:]:
	sourceFile = open('localisation/' + filename, 'r')
	for target in targetLanguages:
		newFilename = filename.replace(sourceLanguage, target)
		if newFilename == filename: continue	#Only copy files that actually contained l_english
		if os.path.isfile(newFilename) and not overwrite: continue
		targetFile = open('localisation/' + newFilename, 'w+')
		for line in sourceFile:
			targetFile.write(line.replace(sourceLanguage + ':', target + ':'))
		targetFile.close()
		sourceFile.seek(0)
print(sourceLanguage + ' localisation export complete.')
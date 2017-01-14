
import os, sys

with open('pics-out.txt', 'w') as outFile:
	for filename in os.listdir('.')[:]:
		outFile.write('GFX_evt_' + filename.replace('.dds', '\n'))

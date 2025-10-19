#####################################################################
# copy_english.py
# By Tim Carrell (LamilLerran), expanded
# Copies English into localization files for other languages
# Will now also create missing directories/files if they don't exist
#####################################################################

import os, sys, getopt

# default to exporting from English to all other languages and not overwriting pre-existing files
allLanguages = {
    'l_braz_por', 'l_english', 'l_french', 'l_german', 'l_japanese',
    'l_korean', 'l_polish', 'l_russian', 'l_simp_chinese', 'l_spanish'
}
sourceLanguage = 'l_english'
ignoreLanguages = set([])
overwrite = True  # safer default

try:
    options, extraargs = getopt.getopt(sys.argv[1:], "hi:os:", ["help", "ignore=", "overwrite", "source="])
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

# Ensure base localisation directories exist
if not os.path.isdir('localisation/english'):
    print("Error: localisation/english directory not found.")
    sys.exit(1)

for filename in os.listdir('localisation/english'):
    sourceFile = open(os.path.join('localisation/english', filename), 'r', encoding="utf-8")
    for target in targetLanguages:
        newFilename = filename.replace(sourceLanguage, target)
        if newFilename == filename:
            continue  # Only copy files that actually contained l_english

        targetDir = os.path.join('localisation', target.replace("l_", ""))
        targetPath = os.path.join(targetDir, newFilename)

        # Create target directory if it doesn’t exist
        os.makedirs(targetDir, exist_ok=True)

        if os.path.isfile(targetPath) and not overwrite:
            continue  # skip if file exists and overwrite not requested

        with open(targetPath, 'w', encoding="utf-8") as targetFile:
            for line in sourceFile:
                targetFile.write(line.replace(sourceLanguage + ':', target + ':'))

        sourceFile.seek(0)  # rewind for next language

    sourceFile.close()

print(sourceLanguage + ' localisation export complete.')

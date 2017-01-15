#####################################################################
# event_creator.py
# By Tim Zerrell (LamilLerran)
# Builds simple events.
# Not really powerful enough for complex events, but works for
# simple events and can give a good base to build more complicated
# events from.
#####################################################################

from tkinter import *
from tkinter import ttk
import os, sys, re

root = Tk()
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)
root.title("MEM Event Creator for Stellaris")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(sticky="NSEW")
mainframe.grid_rowconfigure(1, weight=1)

eventTypeFrame = ttk.LabelFrame(mainframe, text="Event Type")
eventTypeFrame.grid(row=0,column=1)
eventType = StringVar()
eventTypeAnomalyRadio = ttk.Radiobutton(eventTypeFrame, text="Anomaly", variable=eventType, value="Anomaly").grid(row=1, column=0, sticky="W")
eventTypeMTTHRadio = ttk.Radiobutton(eventTypeFrame, text="MTTH", variable=eventType, value="MTTH", state="disabled").grid(row=2, column=0, sticky="W")
eventTypeDiplomaticRadio = ttk.Radiobutton(eventTypeFrame, text="Diplomatic", variable=eventType, value="Diplomatic", state="disabled").grid(row=3, column=0, sticky="W")
eventType.set("Anomaly")

internalIDFrame = ttk.Frame(mainframe)
internalIDFrame.grid(row=0,column=0)
internalID = StringVar()
ttk.Label(internalIDFrame, text="Internal ID:").grid(row=1,column=0)
internalIDEntry = ttk.Entry(internalIDFrame, width=20, textvariable=internalID)
internalIDEntry.grid(row=1,column=1)

anomalyCategoryFrame = ttk.LabelFrame(mainframe, text="Anomaly Category")
anomalyCategoryFrame.grid(row=1,column=0,sticky="NS")
anomalyCategoryFrame.grid_columnconfigure(0, weight=1)
anomalyCategoryFrame.grid_columnconfigure(1, weight=1)
anomalyCategoryFrame.grid_rowconfigure(7, weight=1)
anomalyCategoryKeyFrame = ttk.Frame(anomalyCategoryFrame)
anomalyCategoryKeyFrame.grid(row=0,column=0,columnspan=2,sticky="WE")
anomalyCategoryKeyFrame.grid_columnconfigure(1, weight=1)
anomalyCategoryKey = StringVar()
ttk.Label(anomalyCategoryKeyFrame, text="Category Key: ").grid(row=0,column=0,sticky="W")
anomalyCategoryKeyEntry = ttk.Entry(anomalyCategoryKeyFrame, width=30, textvariable=anomalyCategoryKey, state="disabled").grid(row=0, column=1, sticky="WE")
useCustomCategoryName = BooleanVar()
anomalyCategoryUseCustomNameCheck = ttk.Checkbutton(anomalyCategoryFrame, text="Use Custom Category Key", variable=useCustomCategoryName, onvalue=True, offvalue=False).grid(row=1,column=0,sticky="W")
useExistingCategory = BooleanVar()
anomalyCategoryUseExistingCategoryCheck = ttk.Checkbutton(anomalyCategoryFrame, text="Use Existing Category", variable=useExistingCategory, onvalue=True, offvalue=False, state="disabled").grid(row=2,column=0,sticky="W")

anomalyFailRateFrame = ttk.Frame(anomalyCategoryFrame)
anomalyFailRateFrame.grid(row=1,column=1,sticky="E")
anomalyFailRate = IntVar()
ttk.Label(anomalyFailRateFrame, text="Fail Rate:").grid(row=0,column=0,sticky="W")
anomalyFailRateEntry = ttk.Entry(anomalyFailRateFrame, width=3, textvariable=anomalyFailRate).grid(row=0,column=1,sticky="E")
ttk.Label(anomalyFailRateFrame, text="%").grid(row=0,column=2,sticky="W")
anomalyLevelFrame = ttk.Frame(anomalyCategoryFrame)
anomalyLevelFrame.grid(row=2,column=1,sticky="E")
anomalyLevel = IntVar()
ttk.Label(anomalyLevelFrame, text="Level:").grid(row=0,column=0,sticky="W")
anomalyLevelEntry = ttk.Entry(anomalyLevelFrame, width=3, textvariable=anomalyLevel).grid(row=0,column=1,sticky="E")

anomalyCategoryTitleFrame = ttk.Frame(anomalyCategoryFrame)
anomalyCategoryTitleFrame.grid_columnconfigure(1, weight=1)
anomalyCategoryTitleFrame.grid(row=3,column=0, columnspan=2, sticky="WE")
anomalyCategoryTitle = StringVar()
ttk.Label(anomalyCategoryTitleFrame, text="Title Text: ").grid(row=0,column=0,sticky="W")
anomalyCategoryTitleEntry = ttk.Entry(anomalyCategoryTitleFrame, width=25, textvariable=anomalyCategoryTitle).grid(row=0,column=1,sticky="WE")
anomalyCategoryImageIDFrame = ttk.Frame(anomalyCategoryFrame)
anomalyCategoryImageIDFrame.grid(row=5, column=0, columnspan=2, sticky="WE")
anomalyCategoryImageIDFrame.grid_columnconfigure(1, weight=1)
anomalyCategoryImageID = StringVar()
ttk.Label(anomalyCategoryImageIDFrame, text="Image ID: ").grid(row=0,column=0,sticky="W")
anomalyCategoryImageIDCombo = ttk.Combobox(anomalyCategoryImageIDFrame, textvariable=anomalyCategoryImageID)
anomalyCategoryImageIDCombo.grid(row=0,column=1,sticky="WE")
anomalyCategoryImageIDCombo['values'] = ('TODO', 'TODO 2')
with open('mem-utils/event-image-names.txt', 'r') as inFile:
	for line in inFile:
		anomalyCategoryImageIDCombo['values'] = anomalyCategoryImageIDCombo['values'] + tuple([line])
ttk.Label(anomalyCategoryFrame, text="Description Text:").grid(row=6,column=0,columnspan=2,sticky="W")
anomalyCategoryDesc = StringVar()
anomalyCategoryDescEntry = ttk.Entry(anomalyCategoryFrame, textvariable=anomalyCategoryDesc)
anomalyCategoryDescEntry.grid(row=7,column=0,columnspan=2,sticky="WENS")

anomalyValidPlanetTypesFrame = ttk.LabelFrame(anomalyCategoryFrame, text="Planet Types to Spawn on")
anomalyValidPlanetTypesFrame.grid(row=8, column=0, columnspan=2, sticky="W")
anomalyValidPlanetTypes = list()
anomalyValidPlanetChecks = list()
planetTypeInternalIDs = list()
#TODO
currRow = 0
currCol = 0
with open("mem-utils/planet-types-names.txt") as planetTypeFile:
	for line in planetTypeFile:
		splitLine = [x.strip() for x in line.split(',')]
		planetTypeInternalIDs.append(splitLine[0])
		anomalyValidPlanetTypes.append(BooleanVar())
		anomalyValidPlanetChecks.append(ttk.Checkbutton(anomalyValidPlanetTypesFrame, text=splitLine[1], variable=anomalyValidPlanetTypes[2*currRow+currCol], onvalue=True, offvalue=False).grid(row=currRow,column=currCol,sticky="W"))
		if (currCol == 0 or currCol == 1):
			currCol += 1
		else:
			currRow += 1
			currCol = 0

anomalySuccessEventFrame = ttk.LabelFrame(mainframe, text="Anomaly Success Event")
anomalySuccessEventFrame.grid(row=1,column=1,sticky="NS")
anomalySuccessEventFrame.grid_columnconfigure(0, weight=1)
anomalySuccessEventFrame.grid_columnconfigure(1, weight=1)
anomalySuccessEventIDFrame = ttk.Frame(anomalySuccessEventFrame)
anomalySuccessEventIDFrame.grid(row=0,column=0,columnspan=2,sticky="WE")
anomalySuccessEventIDFrame.grid_columnconfigure(1, weight=1)
anomalySuccessEventID = StringVar()
ttk.Label(anomalySuccessEventIDFrame, text="Event ID: ").grid(row=0,column=0,sticky="W")
anomalySuccessEventIDEntry = ttk.Entry(anomalySuccessEventIDFrame, width=30, textvariable=anomalySuccessEventID, state="disabled").grid(row=0, column=1, sticky="WE")
useCustomAnomalySuccessID = BooleanVar()
useCustomAnomalySuccessIDCheck = ttk.Checkbutton(anomalySuccessEventFrame, text="Use Custom Event ID", variable=useCustomAnomalySuccessID, onvalue=True, offvalue=False).grid(row=1,column=0,sticky="W")

anomalySuccessEventNameFrame = ttk.Frame(anomalySuccessEventFrame)
anomalySuccessEventNameFrame.grid(row=2,column=0)
ttk.Label(anomalySuccessEventNameFrame, text="Name: ").grid(row=0,column=0,sticky="W")
anomalySuccessEventName = StringVar()
anomalySuccessEventNameEntry = ttk.Entry(anomalySuccessEventNameFrame, width=30, textvariable=anomalySuccessEventName).grid(row=0, column=1, sticky="WE")

anomalySuccessImageIDFrame = ttk.Frame(anomalySuccessEventFrame)
anomalySuccessImageIDFrame.grid(row=4, column=0, columnspan=2, sticky="WE")
anomalySuccessImageIDFrame.grid_columnconfigure(1, weight=1)
anomalySuccessImageID = StringVar()
ttk.Label(anomalySuccessImageIDFrame, text="Image ID: ").grid(row=0,column=0,sticky="W")
anomalySuccessImageIDCombo = ttk.Combobox(anomalySuccessImageIDFrame, textvariable=anomalySuccessImageID)
anomalySuccessImageIDCombo.grid(row=0,column=1,sticky="WE")
anomalySuccessImageIDCombo['values'] = ('TODO', 'TODO 2')
with open('mem-utils/event-image-names.txt', 'r') as inFile:
	for line in inFile:
		anomalySuccessImageIDCombo['values'] = anomalySuccessImageIDCombo['values'] + tuple([line])
ttk.Label(anomalySuccessEventFrame, text="Description Text:").grid(row=5,column=0,columnspan=2,sticky="W")
anomalySuccessDesc = StringVar()
anomalySuccessDescEntry = ttk.Entry(anomalySuccessEventFrame, textvariable=anomalySuccessDesc)
anomalySuccessDescEntry.grid(row=6,column=0,columnspan=2,sticky="WENS")

anomalySuccessClearDeposit = BooleanVar()
anomalySuccessClearDepositCheck = ttk.Checkbutton(anomalySuccessEventFrame, text="Clear Orbital Deposit", variable=anomalySuccessClearDeposit, onvalue=True, offvalue=False).grid(row=7,column=0,sticky="W")

anomalySuccessOptionFrame = list()
anomalySuccessOptionText = list()
anomalySuccessOptionEntry = list()
anomalySuccessOptionCheck = list()
anomalySuccessOptionUsed = list()
for i in range(4):
	#TODO
	anomalySuccessOptionFrame.append(ttk.Frame(anomalySuccessEventFrame))
	anomalySuccessOptionFrame[i].grid(row=5+i, column=0, columnspan=2, sticky="WE")
	anomalySuccessOptionUsed.append(BooleanVar())
	anomalySuccessOptionCheck.append(ttk.Checkbutton(anomalySuccessOptionFrame[i],text=str(i+1)+":", variable=anomalySuccessOptionUsed, onvalue=True, offvalue=False).grid(row=0,column=0,sticky="W"))
	anomalySuccessOptionText.append(StringVar())
	anomalySuccessOptionEntry.append(ttk.Entry(anomalySuccessOptionFrame[i], textvariable=anomalySuccessOptionText))
	anomalySuccessOptionEntry[i].grid(row=0,column=1,sticky="WE")
			
root.mainloop()

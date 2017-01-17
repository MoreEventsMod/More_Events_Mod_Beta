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

class EventData:
	def __init__(self):
		pass
data = EventData()
data.internalID = StringVar()
data.eventType = StringVar()
data.anomalyCategoryKey = StringVar()

class LabelEntry:
	def __init__(self, parent, labeltext, *args,**kwargs):
		self.parent = parent
		frameKeywords = ["class", "colormap", "container", "height", "padx", "pady", "visual"]
		entryKeywords = kwargs.keys() - frameKeywords
		frameKeywords = kwargs.keys() & frameKeywords
		frameKWArgs = {key: kwargs[key] for key in frameKeywords}
		entryKWArgs = {key: kwargs[key] for key in entryKeywords}
		self.frame = ttk.Frame(parent, **frameKWArgs)
		self.frame.grid_columnconfigure(1, weight=1)
		self.label = ttk.Label(self.frame, text= labeltext)
		self.label.grid(row=0, column=0, sticky="W")
		self.entry = ttk.Entry(self.frame, **entryKWArgs)
		self.entry.grid(row=0, column=1, sticky="WE")
		
	def grid(self, **kwargs):
		self.frame.grid(**kwargs)
		
	def pack(self, **kwargs):
		self.frame.pack(**kwargs)
		
	def place(self, **kwargs):
		self.frame.place(**kwargs)
        
class EventTypeFrame(ttk.LabelFrame):
	def __init__(self, parent, *args, **kwargs):
		ttk.LabelFrame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.grid(row=0, column=1)
		global data
		self.anomalyRadio = ttk.Radiobutton(self, text="Anomaly", variable=data.eventType, value="Anomaly").grid(row=0, column=0, sticky="W")
		self.mtthRadio = ttk.Radiobutton(self, text="MTTH", variable=data.eventType, value="MTTH", state="disabled").grid(row=1, column=0, sticky="W")
		self.diplomaticRadio = ttk.Radiobutton(self, text="Diplomatic", variable=data.eventType, value="Diplomatic", state="disabled").grid(row=2, column=0, sticky="W")
		data.eventType.set("Anomaly")

#TODO: Authorial entry boxes in BasicsFrame

class BasicsFrame(ttk.Frame):
	def __init__(self, parent, *args, **kwargs):
		ttk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.grid(row=0, column=0, columnspan = 4, sticky = "NEW")
		self.grid_columnconfigure(0, weight=1)
		self.eventTypeFrame = EventTypeFrame(self, text="Event Type")
		self.eventTypeFrame.grid(row=0, column=1)
		global data
		self.internalIDLabelEntry = LabelEntry(self, labeltext="Internal ID: ", textvariable=data.internalID)
		self.internalIDLabelEntry.grid(row=0, column=0)
   
class AnomalyCategoryFrame(ttk.LabelFrame):
	def __init__(self, parent, *args, **kwargs):
		ttk.LabelFrame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.grid(row=1,column=0,sticky="NS")
		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=1)
		self.grid_columnconfigure(2,weight=1)
		self.grid_rowconfigure(7,weight=1)
		global data
		self.key = LabelEntry(self, labeltext="Category Key: ", width=30, textvariable=data.anomalyCategoryKey, state="disabled")
		self.key.grid(row=0,column=0,columnspan=2,sticky="WE")
	 
class MainFrame(ttk.Frame):
	def __init__(self, parent, *args, **kwargs):
		ttk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.grid(sticky="NSEW")
		self.basicsFrame = BasicsFrame(self)

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)
root.title("MEM Event Creator for Stellaris")
root.mainframe = MainFrame(root, padding="3 3 12 12")
root.mainframe.grid_rowconfigure(1, weight=1)

anomalyCategoryFrame = AnomalyCategoryFrame(root.mainframe, text="Anomaly Category")
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
		numCols = 3
		splitLine = [x.strip() for x in line.split(',')]
		planetTypeInternalIDs.append(splitLine[0])
		anomalyValidPlanetTypes.append(BooleanVar())
		anomalyValidPlanetChecks.append(ttk.Checkbutton(anomalyValidPlanetTypesFrame, text=splitLine[1], variable=anomalyValidPlanetTypes[numCols*currRow+currCol], onvalue=True, offvalue=False).grid(row=currRow,column=currCol,sticky="W"))
		currCol += 1
		if (currCol == numCols):
			currRow += 1
			currCol = 0

anomalySuccessEventFrame = ttk.LabelFrame(root.mainframe, text="Anomaly Success Event")
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

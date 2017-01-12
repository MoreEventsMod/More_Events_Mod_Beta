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

root = Tk()
root.title("MEM Event Creator for Stellaris")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid()

eventTypeFrame = ttk.LabelFrame(mainframe, text="Event Type")
eventTypeFrame.grid(row=1,column=1)
eventType = StringVar()
eventTypeAnomalyRadio = ttk.Radiobutton(eventTypeFrame, text="Anomaly", variable=eventType, value="Anomaly").grid(row=1, column=0, sticky="W")
eventTypeMTTHRadio = ttk.Radiobutton(eventTypeFrame, text="MTTH", variable=eventType, value="MTTH", state="disabled").grid(row=2, column=0, sticky="W")
eventTypeDiplomaticRadio = ttk.Radiobutton(eventTypeFrame, text="Diplomatic", variable=eventType, value="Diplomatic", state="disabled").grid(row=3, column=0, sticky="W")
eventType.set("Anomaly")

internalNameFrame = ttk.Frame(mainframe)
internalNameFrame.grid(row=1,column=0)
internalName = StringVar()
ttk.Label(internalNameFrame, text="Internal Name:").grid(row=1,column=0)
internalNameEntry = ttk.Entry(internalNameFrame, width=20, textvariable=internalName)
internalNameEntry.grid(row=1,column=1)

imageMenuFrame = ttk.Frame(mainframe)
imageMenuFrame.grid()
image = StringVar()

anomalyCategoryFrame = ttk.LabelFrame(mainframe, text="Anomaly Category")
anomalyCategoryFrame.grid()
anomalyCategoryName = StringVar()
anomalyCategoryNameEntry = ttk.Entry(anomalyCategoryFrame, width=25, textvariable=anomalyCategoryName, state="disabled").grid(row=1, column=1, sticky="W")
useCustomCategoryName = BooleanVar()
anomalyCategoryUseCustomNameCheck = ttk.Checkbutton(anomalyCategoryFrame, text="Use Custom Category Name", variable=useCustomCategoryName, onvalue=True, offvalue=False).grid(row=2,column=1,sticky="W")
useExistingCategory = BooleanVar()
anomalyCategoryUseExistingCategoryCheck = ttk.Checkbutton(anomalyCategoryFrame, text="Use Existing Category", variable=useExistingCategory, onvalue=True, offvalue=False, state="disabled").grid(row=3,column=1,sticky="W")

#anomalyCategoryNumericsFrame = ttk.Frame(anomalyCategoryFrame)
#anomalyCategoryNumericsFrame.grid(row=4,column=1)
anomalyFailRateFrame = ttk.Frame(anomalyCategoryFrame)
anomalyFailRateFrame.grid(row=4,column=1,sticky="W")
anomalyFailRate = IntVar()
ttk.Label(anomalyFailRateFrame, text="Fail Rate:").grid(row=0,column=0,sticky="W")
anomalyFailRateEntry = ttk.Entry(anomalyFailRateFrame, width=3, textvariable=anomalyFailRate).grid(row=0,column=1,sticky="E")
ttk.Label(anomalyFailRateFrame, text="%").grid(row=0,column=2,sticky="W")
anomalyLevelFrame = ttk.Frame(anomalyCategoryFrame)
anomalyLevelFrame.grid(row=4,column=1,sticky="E")
anomalyLevel = IntVar()
ttk.Label(anomalyLevelFrame, text="Level:").grid(row=0,column=0,sticky="W")
anomalyLevelEntry = ttk.Entry(anomalyLevelFrame, width=3, textvariable=anomalyLevel).grid(row=0,column=1,sticky="E")

root.mainloop()

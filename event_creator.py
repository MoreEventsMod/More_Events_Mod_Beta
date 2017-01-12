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
mainframe.pack(side="left")

eventTypeFrame = ttk.LabelFrame(mainframe, text="Event Type")
eventTypeFrame.pack()
eventType = StringVar()
eventTypeAnomalyRadio = ttk.Radiobutton(eventTypeFrame, text="Anomaly", variable=eventType, value="Anomaly").grid(row=1, column=1, sticky="W")
eventTypeMTTHRadio = ttk.Radiobutton(eventTypeFrame, text="MTTH", variable=eventType, value="MTTH", state="disabled").grid(row=2, column=1, sticky="W")
eventTypeDiplomaticRadio = ttk.Radiobutton(eventTypeFrame, text="Diplomatic", variable=eventType, value="Diplomatic", state="disabled").grid(row=3, column=1, sticky="W")
eventType.set("Anomaly")

internalNameFrame = ttk.Frame(mainframe)
internalNameFrame.pack(side="left")
internalName = StringVar()
ttk.Label(internalNameFrame, text="Internal Name:").pack(side="left")
internalNameEntry = ttk.Entry(internalNameFrame, width=20, textvariable=internalName)
internalNameEntry.pack()

imageMenuFrame = ttk.Frame(mainframe)
imageMenuFrame.pack(side="left")
image = StringVar()


root.mainloop()

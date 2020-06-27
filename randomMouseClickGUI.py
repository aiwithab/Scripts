import tkinter as tk

import win32api
import win32con


import random
import time
    
defaultTime = 2
defaultInitialXCoordinate = 20
defaultInitialYCoordinate = 40
defaultFinalXCoordinate = 200
defaultFinalYCoordinate = 400

def setSleepTime(userInputTime):
    print(f"time set to {userInputTime}")
    

def getTime():
    defaultTime = timeEntry.get()
    setSleepTime(defaultTime)

def getCoordinates():
    defaultInitialXCoordinate = initialXCoordinateEntry.get()
    defaultInitialYCoordinate = initialYCoordinateEntry.get()
    defaultFinalXCoordinate = finalXCoordinateEntry.get()
    defaultFinalYCoordinate = finalYCoordinateEntry.get()

    setMouseRectangleCoordinates(defaultInitialXCoordinate,defaultInitialYCoordinate,defaultFinalXCoordinate,defaultFinalYCoordinate)

def setMouseRectangleCoordinates(initialXCoordinate,initialYCoordinate,finalXCoordinate,finalYCoordinate,):
    print(f"cordinates set to {initialXCoordinate} {initialYCoordinate} {finalXCoordinate} {finalYCoordinate}")
   


def runMainScript():
    
    while True:

        win32api.SetCursorPos((random.randint(defaultInitialXCoordinate, defaultFinalXCoordinate), random.randint(defaultInitialYCoordinate, defaultFinalXCoordinate)))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, random.randint(1, 1000), random.randint(1, 1000), 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, random.randint(1, 1000), random.randint(1, 1000), 0, 0)
        time.sleep(defaultTime)

def stopMainScript():
    
    print('stopped!!!!')
    exit()


root = tk.Tk()
root.title('Random Mouse Click')
frame = tk.Frame(root)
frame.size()
frame.pack()

timeLabel = tk.Label(frame, text="Enter Sleep Time (in seconds):")
timeEntry = tk.Entry(frame)
timeLabel.pack()
timeEntry.pack()
timeButton = tk.Button(frame, 
                   text="SET SLEEP TIME", 
                   fg="blue",
                   command=getTime)
timeButton.pack()
timeSettedLabel = tk.Label(frame, text=f"Time is set to {defaultTime} seconds")
timeSettedLabel.pack()

# INITIAL COORDINATES
# X COORDINATE
initialXCoordinateLabel = tk.Label(frame, text="Enter initial X coordinate:")
initialXCoordinateEntry = tk.Entry(frame)
initialXCoordinateLabel.pack()
initialXCoordinateEntry.pack()
# Y COORDINATE
initialYCoordinateLabel = tk.Label(frame, text="Enter initial Y coordinate:")
initialYCoordinateEntry = tk.Entry(frame)
initialYCoordinateLabel.pack()
initialYCoordinateEntry.pack()
# FINAL COORDINATES
# X COORDINATE
finalXCoordinateLabel = tk.Label(frame, text="Enter final X coordinate:")
finalXCoordinateEntry = tk.Entry(frame)
finalXCoordinateLabel.pack()
finalXCoordinateEntry.pack()
# Y COORDINATE
finalYCoordinateLabel = tk.Label(frame, text="Enter final Y coordinate:")
finalYCoordinateEntry = tk.Entry(frame)
finalYCoordinateLabel.pack()
finalYCoordinateEntry.pack()
# BUTTON
coordinateButton = tk.Button(frame,fg='blue',
                   text="SET CORDINATES",
                   command=getCoordinates)
coordinateButton.pack()
coordinateSettedLabel = tk.Label(frame,text=f"Coordiantes are set to initial x = {defaultInitialXCoordinate} y = {defaultInitialYCoordinate} and final x = {defaultFinalXCoordinate} y = {defaultFinalYCoordinate}")
coordinateSettedLabel.pack()


startScriptButton = tk.Button(frame,fg='green',text="Start Script",command=runMainScript)
startScriptButton.pack()
stopScriptButton = tk.Button(frame,fg='red',text="Stop Script",command=stopMainScript)
stopScriptButton.pack()

root.mainloop()


import tkinter as tk
    
defaultTime = 2
defaultInitialXCoordinate = 20
defaultInitialYCoordinate = 40
defaultFinalXCoordinate = 200
defaultFinalYCoordinate = 400

def setSleepTime(userInputTime):
    print(f"time set to {userInputTime}")
    defaultTime = userInputTime


def setMouseRectangleCoordinates(initialXCoordinate,initialYCoordinate,finalXCoordinate,finalYCoordinate,):
    print(f"cordinates set to {initialXCoordinate} {initialYCoordinate} {finalXCoordinate} {finalYCoordinate}")
    defaultInitialXCoordinate = initialXCoordinate
    defaultInitialYCoordinate = initialYCoordinate
    defaultFinalXCoordinate = finalXCoordinate
    defaultFinalYCoordinate = finalYCoordinate

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
                   fg="red",
                   command=setSleepTime)
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
coordinateButton = tk.Button(frame,
                   text="SET CORDINATES",
                   command=setMouseRectangleCoordinates)
coordinateButton.pack()
coordinateSettedLabel = tk.Label(frame,text=f"Coordiantes are set to initial x = {defaultInitialXCoordinate} y = {defaultInitialYCoordinate} and final x = {defaultFinalXCoordinate} y = {defaultFinalYCoordinate}")
coordinateSettedLabel.pack()
root.mainloop()

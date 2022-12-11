"""
Author: Em McGuire
File Name: FinalProjectInTk.py
"""


import tkinter as tk
import random
import time
import json 

class TypingTest(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")

        #Create frame for text section
        self.textFrame = tk.Frame()
        self.textFrame.pack(pady=5)

        #Create label and text area within text section
        self.textLabel = tk.Label(master=self.textFrame, text="Press Start")
        self.userTextArea = tk.Text(master=self.textFrame, height=3)
        self.textLabel.pack(pady=5)
        self.userTextArea.pack(pady=5, padx=30)

        #Create frame for button section
        self.buttonFrame = tk.Frame()
        self.buttonFrame.pack(pady=5, fill="y")

        #Create buttons within button section
        self.startButton = tk.Button(master=self.buttonFrame, text="Start", width=7, height=1,
                                bg="gray", fg="black", command=self.start)
        self.endButton = tk.Button(master=self.buttonFrame, text="End", width=7, height=1,
                              bg="gray", fg="black", command=self.end)
        self.resetButton = tk.Button(master=self.buttonFrame, text="Reset", width=7, height=1,
                                bg="gray", fg="black", command=self.reset)

        self.startButton.pack(side="left", padx=20)
        self.endButton.pack(side="left", padx=20)
        self.resetButton.pack(side="left", padx=20)

        #Create frame for outputs section
        self.outputFrame = tk.Frame()
        self.outputFrame.pack(pady=5)

        #Create label within outputs section
        self.userTextLabel = tk.Label(text="")
        self.wpmLabel = tk.Label(text="WPM: -")
        self.accuracyLabel = tk.Label(text="Accuracy: -")
        self.awpmLabel = tk.Label(text="AWPM: -")
        self.userTextLabel.pack(pady=5)
        self.wpmLabel.pack(pady=5)
        self.accuracyLabel.pack(pady=5)
        self.awpmLabel.pack(pady=5)

        #Set running to false initially
        self.isRunning = False
        #Bind keypresses to text area
        self.userTextArea.bind("<Return>", self.endOnEnter)
        self.userTextArea.bind("<Key>", self.updateOnKeypress)

    def start(self):
        """resets all fields, starts a timer and displays text to be typed"""
        self.reset()
        self.keysPressed = 0
        #Starts program running
        self.isRunning = True
        #Starts timer
        self.seconds = time.time()
        #Opens file
        file = open("1415fp.json")
        #Converts to dictionary
        DICTIONARY = json.load(file)
        file.close()
        #Chooses random item
        i = str(random.randint(1, 6))
        self.correctString = DICTIONARY[i]
        #Creates a list out of the dictionary item string
        self.listOfChars = []
        for char in DICTIONARY[i]:
            self.listOfChars.append(char)
        #Displays dictionary string
        self.textLabel.config(text=self.correctString)

    def end(self):
        """ends timer, sets running to false and displays outputs"""
        if(self.isRunning):
            #Stop timer
            self.timerSeconds = round(time.time() - self.seconds, 2)
            self.userTextArea.config(state="disabled")
            #Set running to false
            self.isRunning = False
            #Run methods to calculate and display results
            self.checkText()
            self.calculateResults()

    def endOnEnter(self, event):
        """runs the end method if user presses the Enter key"""
        self.end()
    
    def reset(self):
        """resets the program by clearing all fields and setting running to false"""
        #Set running to false
        self.isRunning = False
        #Reset/clear labels and text areas
        self.textLabel.config(text="Type a file name and press Start")
        self.userTextArea.config(state="normal")
        self.userTextArea.delete("1.0", "end")
        self.wpmLabel.config(text="WPM: -")
        self.accuracyLabel.config(text="Accuracy: -")
        self.awpmLabel.config(text="AWPM: -")
        self.userTextLabel.config(text="")

    def checkText(self):
        """checks user inputs"""
        #get text from text area
        self.userText = self.userTextArea.get("1.0", "end")[:-1]
        #Append each character to list
        self.userTextList = []
        for char in self.userText:
            self.userTextList.append(char)
        self.correctChars = 0
        self.incorrectChars = 0
        self.count = 0
        #Check for correct/incorrect characters in user's text
        if self.keysPressed >= 2:
            for char in self.userTextList:
                if char == self.listOfChars[self.count]:
                    self.correctChars += 1
                    self.count += 1
                else:
                    self.incorrectChars += 1
                    self.count += 1

    def checkLength(self):
        """checks the length of user text and runs end if length matches 
        the length of the correct string"""
        if self.count == len(self.listOfChars):
            self.end()

    def updateOnKeypress(self, event):
        """runs methods to update outputs on each keypress"""
        self.keysPressed += 1
        if self.isRunning:
            self.checkText()
            self.checkLength()
            self.userTextLabel.config(text=self.userText)

    def calculateResults(self):
        """calculates and then displays outputs in label fields"""
        #Calculate wpm and accuracy
        cps = float(len(self.userText)) / self.timerSeconds
        wpm = round((cps * 60)/5, 2)
        accuracyPercent = round(self.correctChars/len(self.listOfChars), 2) * 100
        awpm = round(wpm * accuracyPercent /100, 2)
        #Display outputs 
        if self.correctChars == len(self.listOfChars):
            self.userTextLabel.config(text=self.userText, fg="green")
        else:
            self.userTextLabel.config(text=self.userText, fg="red")
        self.wpmLabel.config(text= "WPM: " + str(wpm))
        self.accuracyLabel.config(text="Accuracy: " + str(accuracyPercent) + "%")
        self.awpmLabel.config(text= "AWPM: " + str(awpm))

def main():
    TypingTest().mainloop()

if __name__ == "__main__":
    main()
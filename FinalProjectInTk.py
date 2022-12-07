"""
Author: Em McGuire
File name: FinalProjectInTk.py

"""

import tkinter as tk
import random
import time
import json 

class TypingTest(tk.Tk):
    
    def __init__(self):
        super().__init__()

        #Create frame for file section
        self.fileFrame = tk.Frame()
        self.fileFrame.pack()

        #Create label and entry for file within fileFrame
        self.fileLabel = tk.Label(master=self.fileFrame, text="File Name: ")
        self.fileEntry = tk.Entry(master=self.fileFrame, fg="black", bg="white", width=40)
        self.fileLabel.pack()
        self.fileEntry.pack()

        #Create frame for text section
        self.textFrame = tk.Frame()
        self.textFrame.pack()

        #Create label and text area within text section
        self.textLabel = tk.Label(master=self.textFrame, text="Paragraph")
        self.userTextArea = tk.Text(master=self.textFrame, height=3, width=70)
        self.textLabel.pack()
        self.userTextArea.pack()

        #Create frame for button section
        self.buttonFrame = tk.Frame()
        self.buttonFrame.pack()

        #Create buttons within button section
        self.startButton = tk.Button(master=self.buttonFrame, text="Start", width=7, height=1,
                                bg="gray", fg="black", command=self.start)
        self.endButton = tk.Button(master=self.buttonFrame, text="End", width=7, height=1,
                              bg="gray", fg="black", command=self.end)
        self.resetButton = tk.Button(master=self.buttonFrame, text="Reset", width=7, height=1,
                                bg="gray", fg="black", command=self.reset)

        self.startButton.pack()
        self.endButton.pack()
        self.resetButton.pack()

        #Create frame for outputs section
        self.outputFrame = tk.Frame()
        self.outputFrame.pack()

        #Create label within outputs section
        self.outputLabel = tk.Label(text="test")
        self.outputLabel.pack()

        self.isRunning = False

    def start(self):
        """starts timer and displays text"""
        self.isRunning = True
        self.seconds = time.time()
        file = open(self.fileEntry.get())
        DICTIONARY = json.load(file)
        file.close()
        i = str(random.randint(1, 4))
        self.correctString = DICTIONARY[i]
        self.listOfChars = []
        for char in DICTIONARY[i]:
            self.listOfChars.append(char)
        self.textLabel.config(text=self.correctString)

    def end(self):
        """ends timer and runs method to calculate outputs"""
        if(self.isRunning):
            self.timerSeconds = round(time.time() - self.seconds, 2)
            self.checkText()
            self.calculateOutputs()
            self.isRunning = False
    
    def reset(self):
        """resets the program"""
        self.isRunning = False
        self.textLabel.config(text="Type a file name and press Start")
        self.userTextArea.delete("1.0", "end")
        self.outputLabel.config(text="differenttest")

    def checkText(self):
        """checks user inputs"""
        if(self.isRunning):
            self.userText = self.userTextArea.get("1.0", "end")
            self.userText = self.userText[:-1]
            self.userTextList = []
            self.correctChars = 0
            self.incorrectChars = 0
            count = 0
            for char in self.userText:
                self.userTextList.append(char)
            for char in self.userTextList:
                if char == self.listOfChars[count]:
                    self.correctChars += 1
                    count += 1
                else:
                    self.incorrectChars += 1
                    count += 1
        self.outputLabel.config(text = self.userText)

    def calculateOutputs(self):
        """displays outputs based on inputs"""
        userWordList = []
        for word in self.userText.split(" "):
            userWordList.append(word)
        wps = float(len(userWordList)) / self.timerSeconds
        cps = float(len(self.userText)) / self.timerSeconds
        wpm = round(wps * 60, 2)
        cpm = round(cps * 60, 2)
        self.outputLabel.config(text= "It took you " + str(self.timerSeconds) + " seconds to type the paragraph.\nWPM = " + str(wpm) + "\nCPM = " + str(cpm))

def main():
    TypingTest().mainloop()

if __name__ == "__main__":
    main()
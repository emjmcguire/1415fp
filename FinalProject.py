"""
Author: Em McGuire
File name: FinalProject.py

"""

from breezypythongui import EasyFrame
import threading
import random
import time

#Dictionary for testing
DICTIONARY = {1:"paragraph one", 2:"paragraph two", 3:"paragraph three",
              4:"paragraph four", 5:"paragraph five", 6:"paragraph six"}

class TypingTest(EasyFrame):
   
    def __init__(self):
        #Initialize the window
        EasyFrame.__init__(self, title = "Typing Speed Test")
        self.setSize(500, 500)
        
        #create labels and buttons
        self.fileName = self.addTextField(text="", row=0, column = 1, sticky="NW")

        self.displayLabel = self.addLabel(text="Paragraph to display", row=1,
                                          column=1)
        self.typingArea = self.addTextArea(text="", row=2, column=0,
                                           columnspan=3)
        
        self.startButton = self.addButton(row=4, column=1, text="Start", command = self.start)
        self.saveButton = self.addButton(row=4, column=0, text="End", command=self.end)
        self.resetButton = self.addButton(row=4, column=2, text="Reset", command=self.reset)

        self.outputLabel = self.addLabel(text="outputs", row=5, column=1)

    def start(self):
        """starts timer and displays text"""
        self.isRunning = True
        self.seconds = time.time()
        i = random.randint(1, 6)
        self.correctString = DICTIONARY[i]
        self.displayLabel["text"] = self.correctString

    def end(self):
        """ends timer and runs method to calculate outputs"""
        if(self.isRunning):
            self.isRunning = False
            self.timerSeconds = time.time() - self.seconds

    def reset(self):
        """resets the program"""
        self.isRunning = False
        self.typingArea.setText("")
        self.outputLabel["text"] = ""


def main():
    TypingTest().mainloop()

        
if __name__ == "__main__":
    main()

"""
Author: Em McGuire
File name: FinalProjectInTk.py

"""

import tkinter as tk

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
                                bg="gray", fg="black")
        self.endButton = tk.Button(master=self.buttonFrame, text="End", width=7, height=1,
                              bg="gray", fg="black")
        self.resetButton = tk.Button(master=self.buttonFrame, text="Reset", width=7, height=1,
                                bg="gray", fg="black")

        self.startButton.pack()
        self.endButton.pack()
        self.resetButton.pack()

def main():
    TypingTest().mainloop()

if __name__ == "__main__":
    main()
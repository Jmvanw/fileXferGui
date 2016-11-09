#!/usr/bin/python3
import tkinter as tk
from tkinter import *
import csv
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from newFileXfer import copyOver

#newFileXfer(src, des)

class Feedback:

    def askdirectory(self):
        """Returns a selected directoryname."""
        return filedialog.askdirectory(title="Select A Folder", mustexist=1)
        

    def __init__(self, master):

        master.title('THIS IS THE TITLE')
        #master.resizable(False, False)
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        ttk.Label(self.frame_header, text = 'THIS IS THE DIRECTIONS TEXT').grid(row = 0, column = 0)
        

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Source:').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Destination:').grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Execute:').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'sw')
        

        self.entry_source = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_destination = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))

        self.entry_source.grid(row = 0, column = 1, padx = 5)
        self.entry_destination.grid(row = 1, column = 1, padx = 5)        

       
        ttk.Button(self.frame_content, text = 'Choose Folder',
                   command = self.askdirectory).grid(row = 0, column = 2, padx = 5, pady = 5, sticky = 'e')
        
        ttk.Button(self.frame_content, text = 'Choose Folder',
                   command = self.askdirectory).grid(row = 1, column = 2, padx = 5, pady = 5, sticky = 'w')

##        ttk.Button(self.frame_content, text = 'Choose Folder',
##                   command = self.copyOver).grid(row = 2, column = 2, padx = 5, pady = 5, sticky = 'w')
        
        
        #ttk.Button(self.frame_content, text =

    


            
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()

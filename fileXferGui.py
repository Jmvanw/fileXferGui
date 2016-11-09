#!/usr/bin/python3
import tkinter as tk
from tkinter import *
import csv
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from newFileXfer import copyOver
from tkinter import messagebox




class Feedback:

    

    def __init__(self, master):

        master.title('End of Day File Transfer')
        master.resizable(False, False)
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        ttk.Label(self.frame_header, text = 'Choose folders and then click run.').grid(row = 0, column = 0)

        
        self.src_entry = StringVar()
        
        self.des_entry = StringVar()


        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Source:').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Destination:').grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Execute:').grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'sw')
        

        self.entry_source = ttk.Entry(self.frame_content, textvariable=self.src_entry, width = 24, font = ('Arial', 10))
        self.entry_destination = ttk.Entry(self.frame_content, textvariable=self.des_entry, width = 24, font = ('Arial', 10))

        self.entry_source.grid(row = 0, column = 1, padx = 5)
        self.entry_destination.grid(row = 1, column = 1, padx = 5)        

       
        ttk.Button(self.frame_content, text = 'Choose Folder',
                   command = self.getSrc).grid(row = 0, column = 2, padx = 5, pady = 5, sticky = 'e')
        
        ttk.Button(self.frame_content, text = 'Choose Folder',
                   command = self.getDes).grid(row = 1, column = 2, padx = 5, pady = 5, sticky = 'w')

        ttk.Button(self.frame_content, text = 'Run',
                   command = self.xfer).grid(row = 2, column = 2, padx = 5, pady = 5, sticky = 'w')
        

    def getSrc (self):
        src = askdirectory()
        self.src_entry.set(src)

    def getDes (self):
        des = askdirectory()
        self.des_entry.set(des)

    def xfer(self):
        src = self.src_entry.get() + '/'
        des = self.des_entry.get() + '/'
        copyOver(src, des)

        messagebox.showinfo('File Transfer', 'New files were transferred.')

            
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()

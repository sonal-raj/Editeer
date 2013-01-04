#! /usr/bin/python
import Tkinter
from Tkinter import *
import tkFileDialog, tkMessageBox
import os
class OpenEdit:
   
    def __init__(self):
 
        # Root Frame widget
        self.root = Tk()
 
        # Adding Menubar in the widget
        menubar = Menu(self.root)
 
        # File menu,for open,save,save as and quit       
        filemenu = Menu(menubar, tearoff=0)                    # Setting tearoff=0 so that the submenu starts from the first position
        filemenu.add_command(label="New", command=self.new)
        filemenu.add_command(label="Open", command=self.open)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Save as", command=self.save_as)
        filemenu.add_separator()                               # Adding a separator in the submenu
        filemenu.add_command(label="Quit", command=self.root.destroy) # Calling destroy to quit the root widget

        menubar.add_cascade(label="File", menu=filemenu)       # Creating File menu and attaching it to the submenus


  #Edit menu including Cut, Copy and Paste 
	editmenu = Menu(menubar, tearoff=0)
	editmenu.add_command(label="Cut", command=self.cut)
	editmenu.add_command(label="copy", command=self.copy)
	editmenu.add_command(label="Paste", command=self.paste)
        menubar.add_cascade(label="Edit", menu=editmenu)


	# About menu for show about us and help
        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="About", command=self.about)
        aboutmenu.add_command(label="Help", command=self.help)
        menubar.add_cascade(label="About", menu=aboutmenu)

        # Returning defined setting for widget
        self.root.config(menu=menubar)

        

  

        #Setting up the title of the widget
        self.root.title("Untitled - Editeer")
        
        # Adding Text Widget in the GUI
        self.text = Text(self.root, bg = "white")
 
        # This line allows it to be resized       
        self.text.pack(expand=YES, fill=BOTH)
 
	#Starting event handling from the widget
        self.root.mainloop()       
 

	#Defining new method
    def new(self):
        self.root.title("Untitled - Editeer")
        self.file = None			# Absence of file
        self.text.delete(1.0,END)		# clearing the text widgets contents 



	#Defining open method
    def open(self):

        # Asking to chose a file to open.and setting the chosen file name to 'self.file'.
        self.file = tkFileDialog.askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.file == "": # If no file chosen.
            
            self.file = None # Absence of file.
        else:
            
            #set the root window title as obtained by 'tkFileDialog.askopenfilename' method.

            self.root.title(os.path.basename(self.file) + " - Editeer") # Returning the basename of 'self.file'

            self.text.delete(1.0,END)         # Clearing the text widget contents.

            file = open(self.file,"r")        # Opening 'self.file' in read mode. By returning a file object in read mode with open() method.

            self.text.insert(1.0,file.read()) # Inserting the file object content into text widget obtained by open() method. 

            file.close()		      # closing the file object.



	#Defining save method
    def save(self):
        
            file = open(self.file, 'w')          # Opening the 'self.file' into file object with open() method.
            textoutput = self.text.get(0.0, END) # Reading the text widget into textoutput
            file.write(textoutput)               # Writing the textoutput on the file
      
            file.close()			 # Closing the file


	#Defining save_as method
    def save_as(self):
        
 
            # Getting a filename to save the file.
            self.file = tkFileDialog.asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
       
            file = open(self.file, 'w')           # Opening the 'self.file' into file object with open() method.
            textoutput = self.text.get(0.0, END)  # Reading the text widget into textoutput
            file.write(textoutput)                # Writing the textoutput on the file

            file.close()     			  # Closing the file

            self.root.title(os.path.basename(self.file) + " - Editeer") # Setting the title of the root widget.



	#Defining cut method
    def cut(self):
        self.text.event_generate("<<Cut>>")

	#Defining copy method
    def copy(self):
        self.text.event_generate("<<Copy>>")

	#Defining paste method
    def paste(self):
        self.text.event_generate("<<Paste>>")

	#Defining about method
    def about(self):
    
    tkMessageBox.showinfo("Editeer","Created by: Sonal Raj\nCybernetiks Inc.")

	#Defining help method
    def help(self):
        tkMessageBox.showinfo("Help","This is help")

    
 
#Starting the instance of the class OpenEdit
OpenEdit()

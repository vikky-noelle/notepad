import tkinter
import os
from tkinter import scrolledtext
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:

    #variables
    __root = Tk()

    #default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisMenuBar = Menu(__root)
    popup = Menu(__root, tearoff=0)
    textPad = scrolledtext.ScrolledText(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __file = None

            
    def __init__(self,**kwargs):
        #initialization

        #set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        #set the window text
        self.__root.title("Untitled - Notepad")

        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.textPad.grid(sticky=N+E+S+W)

        self.popup.add_command(label="Cut",command=self.__cut)
        self.popup.add_command(label="Copy",command=self.__copy)
        self.popup.add_command(label="Paste",command=self.__paste)

        self.textPad.bind("<Button-3>", self.do_popup)
        
        self.__thisFileMenu.add_command(label="New",command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save",command=self.__saveFile)
        self.__thisFileMenu.add_command(label="SaveAs",command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut",command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy",command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste",command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit",menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="About Notepad",command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)
        

       
    def do_popup(self, event):
        # display the popup menu
        try:
            self.popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            # make sure to release the grab
            self.popup.grab_release()
    
        
    def __quitApplication(self):
        self.__root.destroy()
        #exit()

   

    def __showAbout(self):
        showinfo("Notepad","Created by: vikrant attri with the programs given in class")

    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            #try to open the file
            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.textPad.delete(1.0,END)

            file = open(self.__file,"r")

            self.textPad.insert(1.0,file.read())

            file.close()

        
    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.textPad.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.textPad.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.textPad.get(1.0,END))
            file.close()

    def __cut(self):
        self.textPad.event_generate("<<Cut>>")

    def __copy(self):
        self.textPad.event_generate("<<Copy>>")

    def __paste(self):
        self.textPad.event_generate("<<Paste>>")

    def run(self):
        #run main application
        self.__root.mainloop()




#run main application
notepad = Notepad(width=600,height=400)
notepad.run()




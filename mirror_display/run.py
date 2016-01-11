# -*- coding: utf-8 -*-

__author__ = 'laixintao'

from Tkinter import *
from ScrolledText import *

windows = Tk()
windows.title('mirror')
windows.geometry('400x600')

input_frame = Frame(windows)
input_button = Button(input_frame,text='open')
input_frame.pack()
input_button.pack()

text = ScrolledText(heigh=10)
text.pack()
text.insert(END, "first entry")
text.insert(END, "second entry")

mainloop()
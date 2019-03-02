#! python
# -*- coding: utf-8 -*-

"""
# GUI
"""
# import tkinter
# top = tkinter.Tk()
# t = tkinter.Text()
# t.pack()
# top.mainloop()

from parse import HtmlParser
hp = HtmlParser()
hp.parse("../html/1.html")

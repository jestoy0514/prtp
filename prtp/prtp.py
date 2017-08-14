#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# prtp.py - A simple module for printing in Tkinter using PyWin32.
# Copyright (c) 2017 - Jesus Vedasto Olazo - <jessie@jestoy.frihost.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

import time
import win32api
import win32print

__version__ = '1.0'


class PrintToPrinter(tk.Frame):

    def __init__(self, master=None, **kwargs):
        """ Initialize the graphical user interface. """
        tk.Frame.__init__(self, master)
        self.master.geometry('250x130')
        self.pack(expand=True, fill='both')
        self.file_name = kwargs['filename']
        self.master.title('Print - '+self.file_name)
        self.cur_printer = None
        self.setupUI()

    def setupUI(self):
        """ This is the graphical user interface """
        printers = self.loadPrinters()
        self.val_var = tk.StringVar()
        # This set the default selection in combobox.
        self.val_var.set(printers[0])
        # This set the current printer selected.
        self.cur_printer = printers[0]
        # Get the default printer and save it for restoration purposes.
        self.default_printer = win32print.GetDefaultPrinter()
        self.title_lbl = tk.Label(self, text="Print to Printer",
                                  font=('Times', 13, 'bold'), fg='blue')
        self.title_lbl.pack(fill='x', padx=10, pady=10)
        self.combo = ttk.Combobox(self, textvariable=self.val_var,
                                  values=printers)
        self.combo.pack(fill='x', padx=10, pady=10)
        self.combo.bind("<<ComboboxSelected>>", self.selectPrinter)

        self.print_btn = ttk.Button(self, text='Print',
                                    command=self.printFile)
        self.print_btn.pack(side='right', padx=10, pady=10)
        self.cancel_btn = ttk.Button(self, text='Cancel',
                                     command=self.closeApp)
        self.cancel_btn.pack(side='right', padx=10, pady=10)

    def selectPrinter(self, event):
        """ This function change the current selected printer. """
        self.cur_printer = event.widget.get()

    def loadPrinters(self):
        """ This function create a list of available printers. """
        data = win32print.EnumPrinters(6)
        printer_list = []

        for row in data:
            printer_list.append(row[2])

        return printer_list

    def printFile(self):
        """ This function will try to print the document. """
        win32print.SetDefaultPrinter(self.cur_printer)
        myprinter = self.cur_printer
        file_name = self.file_name
        win32api.ShellExecute(0, "print", file_name, '"%s"' % myprinter, ".", 0)
        self.closeApp()

    def closeApp(self):
        # Added a 1 second sleep time due to directly setting the default
        # printer back to default will cause the printer not print in the
        # previously selected printer.
        time.sleep(1)
        # Set back the default printer.
        win32print.SetDefaultPrinter(self.default_printer)
        # Close the grahical user interface.
        self.master.destroy()
        

if __name__ == '__main__':

    message = "Print a file to printer using Tkinter and PyWin32."

    with open('testing.txt', 'w') as mf:
        mf.write(message)
    
    win = PrintToPrinter(filename='testing.txt')
    win.mainloop()

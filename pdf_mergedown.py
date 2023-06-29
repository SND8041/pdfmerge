import tkinter as tk
import tkinter.filedialog
import tkinter.filedialog
import os
from tkinter import ttk
from tkinter.ttk import Label
from PyPDF2 import PdfMerger

window = tk.Tk()
window.geometry("700x350")

#Adding a label on the main window
label= Label(window,text="Bismillah, meaning in the name of God, the Most Gracious, the Most Merciful",font=('Georgia 10'))
label10=Label(window,text="A free PDF files merging utility.\nClick the button to select files for merging",font=('Georgia 13'))

label.pack(pady=11)
label10.pack(pady=11)

lstPdfs=[]          #this will contain a list of pdf files

def selectfile():
    currdir=os.getcwd()
    tempfilename = tkinter.filedialog.askopenfilenames(filetypes=[("pdf files", "*.pdf")],parent=window,initialdir=currdir,title='please select files')
    if len(tempfilename) > 0:
        print("You choose ", window.splitlist(tempfilename))
    global lstPdfs
    lstPdfs = window.splitlist(tempfilename)
    if len(lstPdfs) > 1:
        mergerObj = PdfMerger()
        print("The number of files selected is ", len(lstPdfs))
        for apdf in lstPdfs:
            mergerObj.append(apdf)
        mergerObj.write('final_out.pdf')
        mergerObj.close()
    else:
        label2 = Label(window, text="You must select at least two file bhai sahab!", font=('Georgia 13'))
        label2.pack(pady=11)

ttk.Button(window, text="Browse", command=selectfile).pack(pady=20)
label11=Label(window,text="PDF merging utility for free. Copyright @ Syed Nasir Danial (snasir.danial@outlook.com)",font=('Georgia 8'))
label11.pack(pady=11)

window.mainloop()


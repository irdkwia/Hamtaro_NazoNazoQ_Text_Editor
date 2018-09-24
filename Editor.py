from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Treeview, Style

content = ""

fen = Tk()
fen.geometry("450x600")
fen.title("Nazo Nazo Q Editor")
fen.resizable(width=True, height=True)

Label(text = "Tree", font="arial 10").pack(side=TOP, fill=X)

FrameChk = Frame()
FrameChk.pack(side=BOTTOM, fill=X)

FrameBtn = Frame()
FrameBtn.pack(side=BOTTOM, fill=X)

EntryVal = Entry(font="arial 10")
EntryVal.pack(side=BOTTOM, fill=BOTH, expand = 1)

Label(text = "Modify object", font="arial 10").pack(side=BOTTOM, fill=X)

ScrollY = Scrollbar(orient=VERTICAL)
ScrollY.pack(side=RIGHT, fill=Y)

FrameList = Frame()
FrameList.pack(fill=BOTH)

StyleTree = Style()
StyleTree.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 10))
StyleTree.configure("mystyle.Treeview.Heading", font=('Arial', 10))
StyleTree.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
TreeVal = Treeview(height = 50, selectmode="browse", style="mystyle.Treeview")
TreeVal.pack(side=TOP, fill=BOTH, expand = 1)
TreeVal.bind('<<TreeviewSelect>>', onSelect)

ButtonAdd = Button(FrameBtn, text="Edit", command=Change, font="arial 10")
ButtonAdd.pack(side=LEFT, fill=BOTH, expand = 1)
ButtonOpen = Button(FrameBtn, text="Open", command=Open, font="arial 10")
ButtonOpen.pack(side=LEFT, fill=BOTH, expand = 1)
ButtonSave = Button(FrameBtn, text="Save", command=Save, font="arial 10")
ButtonSave.pack(side=LEFT, fill=BOTH, expand = 1)
ChkDebug = Checkbutton(FrameChk, text="Debug Mode", command=checkDbg, font="arial 10", bd=0)
ChkDebug.pack(side=LEFT, fill=BOTH, expand = 1)
Debug = False

ScrollY.config(command=TreeVal.yview)
TreeVal.config(yscrollcommand=ScrollY.set)

fen.mainloop()

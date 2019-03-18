import builtins
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Treeview, Style
from Scripts.TKClass import *

sys.setrecursionlimit(30)

#Search もどる

builtins.content = ""

builtins.fen = Tk()
fen.geometry("450x600")
fen.title("Nazo Nazo Q Editor")
fen.resizable(width=True, height=True)

Label(text = "Tree", font="arial 10").pack(side=TOP, fill=X)

builtins.FrameChk = Frame()
FrameChk.pack(side=BOTTOM, fill=X)

builtins.FrameBtnSearch = Frame()
FrameBtnSearch.pack(side=BOTTOM, fill=X)

builtins.EntrySearch = Entry(font="arial 10")
EntrySearch.pack(side=BOTTOM, fill=BOTH, expand = 1)

Label(text = "Search", font="arial 10").pack(side=BOTTOM, fill=X)

builtins.FrameBtn = Frame()
FrameBtn.pack(side=BOTTOM, fill=X)

builtins.EntryVal = Entry(font="arial 10")
EntryVal.pack(side=BOTTOM, fill=BOTH, expand = 1)

Label(text = "Modify object", font="arial 10").pack(side=BOTTOM, fill=X)

builtins.ScrollY = Scrollbar(orient=VERTICAL)
ScrollY.pack(side=RIGHT, fill=Y)

builtins.FrameList = Frame()
FrameList.pack(fill=BOTH)

builtins.StyleTree = Style()
StyleTree.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 10))
StyleTree.configure("mystyle.Treeview.Heading", font=('Arial', 10))
StyleTree.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
builtins.TreeVal = Treeview(height = 50, selectmode="browse", style="mystyle.Treeview")
TreeVal.pack(side=TOP, fill=BOTH, expand = 1)
TreeVal.bind('<<TreeviewSelect>>', onSelect)

builtins.ButtonAdd = Button(FrameBtn, text="Edit", command=Change, font="arial 10")
ButtonAdd.pack(side=LEFT, fill=BOTH, expand = 1)
builtins.ButtonOpen = Button(FrameBtn, text="Open", command=Open, font="arial 10")
ButtonOpen.pack(side=LEFT, fill=BOTH, expand = 1)
builtins.ButtonSave = Button(FrameBtn, text="Save", command=Save, font="arial 10")
ButtonSave.pack(side=LEFT, fill=BOTH, expand = 1)
builtins.ChkDebug = Checkbutton(FrameChk, text="Debug Mode", command=checkDbg, font="arial 10", bd=0)
ChkDebug.pack(side=LEFT, fill=BOTH, expand = 1)
builtins.Debug = False

builtins.ButtonSearch = Button(FrameBtnSearch, text="Previous", command=SearchCmdPrev, font="arial 10")
ButtonSearch.pack(side=LEFT, fill=BOTH, expand = 1)
builtins.ButtonSearch = Button(FrameBtnSearch, text="Next", command=SearchCmdNext, font="arial 10")
ButtonSearch.pack(side=LEFT, fill=BOTH, expand = 1)

ScrollY.config(command=TreeVal.yview)
TreeVal.config(yscrollcommand=ScrollY.set)

fen.mainloop()

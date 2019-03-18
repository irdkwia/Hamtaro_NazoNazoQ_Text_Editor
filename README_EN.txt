-------------------------------------------------------------
                         Introduction
-------------------------------------------------------------
Before starting, I want to apologize for my bad english.
If you can understand well french, you can see the
"README_FR.txt" file for documentation in french.

This program can be used to edit text in 
"Tottoko Hamtaro : Nazo Nazo Q" nintendo DS game.
It can only edit text, and not pictures that contain text.

To use it, you need to know how to pack/unpack nds files.
If you don't, search through the net "nds unpack" and find
a software to unpack/pack nds roms.

Place the unpacked files in a folder named X (replace X by
any other name.)
This program can only edit files unpacked.

After unpacking files, replace file
"X/data/Font/StatFontSet.dat" by the one in "Font".
The new file contains characters that are not present in
the original file.

Now, you can start to edit files.
-------------------------------------------------------------
                         How to use it
-------------------------------------------------------------
-Run "Program/Editor.exe"
-Once loaded, you need to open a file (see below for a list
of important files) by clicking on the "Open" button.
-If it goes well, you will see a treeview with numbers
(indexes) and/or lines of text.
-Browse the treeview to select some text to edit, and make
changes by typing them in the entry at the bottom. Don't 
forget to click on the "Edit" button to save changes in the
line before selecting another, otherwise changes are lost.
-Don't forget to save your modified file.

Note : If activated, the "Debug" Check button force
the program to rebuild the treeview after each edit.
This is very slow, but you can check if the changes are made
correctly.
For more information, please check file "Doc/Examples.pdf".
Also, there is a small video in Doc of various tests that
works.
-------------------------------------------------------------
                      Special Characters
-------------------------------------------------------------
Lines of text may contain some special character. All
of these characters are pointed out by the fact that
they are between pipe characters ("|").
Here is a list of special characters : 

|NL| : New Line.

|Blue|, |Red| or |Black| : They are used to change the
color of the following text.

|Start:XX| : Notify about a start of a textbox, but it is not
always present. XX Represents a number between 0 and 255.

|End:XX| : Notify about an end of a textbox, but it is not
always present. XX Represents a number between 0 and 255.

|Pause:XX| : Used to mark a pause in a dialogue, before
it continues automatically.
XX Represents a number between 0 and 255. It defines the
amount of time (in frames) the dialogue will pause before
it continues.

|Next:XX| : Notify about a new textbox.
XX Represents a number between 0 and 255.

NB : If you want to add a textbox (to add more text), you
can insert "|End:0||Next:0|" (followed by "|Start:0|" if
necessary) between "|Start:1|" and "|End:1|" (if exists in
a line of text which ends the previous textbox, notify about
a new textbox and starts it.

|nXX| : Other special characters, and should not be removed.
XX Represents a number between 0 and 255.

|xXX| : Other special characters, and should not be removed.
Some can change the color, or the size of the text.
XX Represents a number between 0 and 255.

|cXX| : Special symbols.
XX Represents a number between 0 and 255.

Note : NEVER use |n254| and |n255|.

-------------------------------------------------------------
                        List of files
-------------------------------------------------------------
This is a list of files where there are some text that
could be modified. Keep in mind that I can forgot other files
that contains text, but from what I saw there are more
than 90% of the text within this game (including
Riddles and Cutscenes).

-X/data/QMsg/QMsgDat.dat (where riddles are located.)
-X/data/FEvent/FEvData_AS.dat
-X/data/FEvent/FEvData_HN.dat
-X/data/FEvent/FEvData_MM.dat
-X/data/FEvent/FEvData_NH.dat
-X/data/FEvent/FEvData_YM.dat
-X/data/Furniture/FurnitureName.dat
-X/data/Furniture/FurnitureSetName.dat
-X/data/House/HouseHamFurnMsg.dat
-X/data/House/HouseHamTouchMsg.dat
-X/data/House/HouseSysMsg.dat
-X/data/MMsg/MSysMsg.dat
-X/data/WMsg/WSysMsg.dat
-X/data/QEvent/NandeQEvMesData.dat
-X/data/QEvent/SorahamQEvMesData.dat
-X/data/UserList/UserList.dat
-X/data/UserList/AreaName.dat

Some info about the files : 

-data/QMsg/QMsgDat.dat
Lines of text at index 0 are lines used
in the riddles' selection menu (Book).
Lines of text at index 1 are rank names.
Index 3 to the end contains riddles.
Each riddle index has 6 lines : 
-The question
-The first answer (always the correct answer)
-The second answer
-The third answer
-The hint
-The explanation of the answer

-data/FEvent/*
All of these files have the same structure.
They contain a repetition of the following pattern : 
-One or more lines of random symbols (probably data
for animations).
-One line with a sub index 0 which contains text.

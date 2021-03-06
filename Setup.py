import cx_Freeze

#Code used to freeze python code into an executable.

executables = [cx_Freeze.Executable("Editor.py", base = "Win32GUI")]

cx_Freeze.setup(
    name="NZNZQ Editor",
    version="2.0",
    options={"build_exe": {"includes":["tkinter"],
                           "include_files":["Scripts"]}},
    executables = executables

    )

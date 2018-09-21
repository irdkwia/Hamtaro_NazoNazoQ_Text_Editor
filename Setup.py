import cx_Freeze

executables = [cx_Freeze.Executable("Editor.py"), base="Win32GUI"]

cx_Freeze.setup(
    name="NZNZQ Editor",
    version="1.0",
    options={"build_exe": {"includes":["tkinter"],
                           "include_files":["ModClass.py"]}},
    executables = executables

    )

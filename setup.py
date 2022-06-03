from cx_Freeze import setup, Executable

base = None

executables = [Executable("Scorpion.py", base=base)]

packages = ["idna"]

options = {
    'build_exe': {
        'packages':packages,
    },
}
setup(
    name = "SCORPION",
    options = options,
    version = "0.2",
    description = '',
    executables = executables
)

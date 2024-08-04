import PyInstaller.__main__
from os import path, getcwd

main_dir = getcwd()
path_to_main = str(main_dir + r"\main.py")

print(path_to_main)


def install():
    PyInstaller.__main__.run([
        path_to_main,
        "--onefile",
        "--console",
        "--icon=" + main_dir + r"\assets\logo.ico",
        r"--name=RoR Save Editor",
        "--specpath=" + main_dir + r"\dist",
        "--distpath=" + main_dir + r"\dist",
        "--workpath=" + main_dir + r"\dist"
    ])

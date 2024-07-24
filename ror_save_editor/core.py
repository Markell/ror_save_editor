import json
import os.path
import shutil
import time
from rich.console import Console
import tkinter as tk
from tkinter import filedialog

console = Console()


def check_savefile(save_path):
    if not os.path.isfile(save_path) or os.path.isfile('save.json'):
        console.print("⚠️ Save file not found", style="#FFA500")
        print(r'Your save file should be located at: '
              r'C:\Program Files (x86)\Steam\userdata\[Number]\1337520\remote\'')
        console.input("Move the program to the directory with the save file"
                      " or press [bold]Enter[/bold] to select it manually")

        root = tk.Tk()
        root.withdraw()
        save_path = filedialog.askopenfilename()
        if not save_path or "save.json" not in save_path:
            exit()

    return save_path


def check_backup(save_path):
    if not os.path.isfile("save_backup.json"):
        shutil.copy(save_path, "save_backup.json")
        console.print("⚠️ Backup file created, "
                      "rename it and replace the original safe if something went wrong", style="#FFA500")
        time.sleep(5)


def open_save_file(save_path):
    global data
    global flags

    with open(save_path, 'r', encoding="utf-8") as savefile:  # Opens the json file
        data = json.load(savefile)  # Reads the file as json
    flags = data["flags"]  # Grabs the "flags" list from the json


def format_to_json(name, dictionary):
    name = dictionary[name]

    return f'challenge_unlock_{name}_completed'


def get_pc_param(pc_name, names_dict, params_dict):
    pc_parameters = {}
    for key, value in params_dict.items():
        if names_dict[pc_name] in value:
            pc_parameters[key] = value

    return pc_parameters


def get_unlocked_param(params_dict):
    unlocked_parameters = {}

    for param in params_dict:
        formated_param = format_to_json(param, params_dict)

        if formated_param in flags:
            unlocked_parameters[param] = list(params_dict).index(param)

    return unlocked_parameters


def edit_save_file(slected_params, unlocked_params, params_dict):
    if slected_params:
        for param in slected_params:
            if param not in unlocked_params.keys():
                flags.append(format_to_json(param, params_dict))

        for param in unlocked_params.keys():
            if param not in slected_params:
                flags.remove(format_to_json(param, params_dict))


def write_to_save_file(save_path):
    with open(save_path, "w", encoding="utf-8") as mod_savefile:
        json.dump(data, mod_savefile, separators=(',', ':'))

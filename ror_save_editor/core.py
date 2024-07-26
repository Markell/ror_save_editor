import json
import os.path
import shutil
import time
from rich.console import Console
import tkinter as tk
from tkinter import filedialog

console = Console()


def check_savefile(save_path):
    """
    Check save file is exist, if not - call tkinter file picker
    :param save_path: path to save file
    :return: existing save file path
    """
    if not os.path.isfile(save_path) or os.path.isfile('save.json'):
        console.print("⚠️ Save file not found", style="#FFA500")
        print(r'Your save file should be located at: '
              r'C:\Program Files (x86)\Steam\userdata\[Number]\1337520\remote\'')
        console.input("Move the program to the directory with the save file"
                      " or press [bold]Enter[/bold] to select it manually")

        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        save_path = filedialog.askopenfilename()
        root.destroy()
        if not save_path or "save.json" not in save_path:
            exit()

    return save_path


def check_backup(save_path):
    """
    Check backup of the save file is exist, if not - create new one
    :param save_path: path to save file
    """
    if not os.path.isfile("save_backup.json"):
        shutil.copy(save_path, "save_backup.json")

        console.print("⚠️ Backup file created, "
                      "rename it and replace the original safe if something went wrong", style="#FFA500")
        time.sleep(5)


def open_save_file(save_path):
    """
    Open save file
    :param save_path: path to save file
    """
    global data  # All save file text
    global flags # List with necessary parameters

    with open(save_path, 'r', encoding="utf-8") as savefile:  # Opens the json file
        data = json.load(savefile)  # Reads the file as json
    flags = data["flags"]  # Grabs the "flags" list from the json


def format_to_json(name, dictionary):
    """
    Format income data to json format
    :param name: name of the character, skill e.t.c
    :param dictionary: array with scharaters, skills e.t.c
    :return: prepared string for save file
    """
    name = dictionary[name]  # Get character name, skill name, ... from dictionary

    return f'challenge_unlock_{name}_completed'


def get_pc_param(pc_name, names_dict, params_dict):
    """
    Get parameters for certain character
    :param pc_name: charater name
    :param names_dict: dictonary with all character names
    :param params_dict: dictionary wirh all parameters
    :return: parameters for certain character
    """
    pc_parameters = {}

    # Go through all parameters in the array
    # and get the character parameters
    for key, value in params_dict.items():
        if names_dict[pc_name] in value:
            pc_parameters[key] = value

    return pc_parameters


def get_unlocked_param(params_dict):
    """
    Get unlocked parameters for certain character
    :param params_dict: dictionary with all character parameters
    :return: dictionary wirh unlocked character parameters
    """
    unlocked_parameters = {}

    # Go through all parameters in the dictionary
    # and compare it with parameters in save file
    for param in params_dict:
        formated_param = format_to_json(param, params_dict)  # Get formated porameter for save file

        # If paramter founded, store it to dictionary
        if formated_param in flags:
            unlocked_parameters[param] = list(params_dict).index(param)

    return unlocked_parameters


def edit_save_file(slected_params, unlocked_params, params_dict):
    """
    Add changes to save file
    :param slected_params: selected menu items
    :param unlocked_params: unlocked character parameters
    :param params_dict: dictionary with all character parameters
    """
    if slected_params:  # Pass if there are no items selected (esc pressed)
        for param in slected_params:
            if param not in unlocked_params.keys():
                flags.append(format_to_json(param, params_dict))

        for param in unlocked_params.keys():
            if param not in slected_params:
                flags.remove(format_to_json(param, params_dict))


def write_to_save_file(save_path):
    """
    Write changes to save file
    :param save_path: path to save file
    """
    with open(save_path, "w", encoding="utf-8") as mod_savefile:
        json.dump(data, mod_savefile, separators=(',', ':'))
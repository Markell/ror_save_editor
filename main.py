import json
from beaupy import select, select_multiple
from rich.console import Console

console = Console()

file_path = '0_localsave.json'
with open(file_path, 'r', encoding="utf-8") as savefile:  # Opens the json file
    data = json.load(savefile)  # Reads the file as json
flags = data["flags"]  # Grabs the "flags" list from the json


# def format_to_json(name, dictionary):
#     name = dictionary[name]
#
#     return f'challenge_unlock_{name}_completed'
#
#
# def get_pc_param(pc_name, names_dict, params_dict):
#     pc_parameters = {}
#     for key, value in params_dict.items():
#         if names_dict[pc_name] in value:
#             pc_parameters[key] = value
#
#     return pc_parameters
#
#
# def get_unlocked_param(params_dict):
#     unlocked_parameters = {}
#
#     for param in params_dict:
#         formated_param = format_to_json(param, params_dict)
#
#         if formated_param in flags:
#             unlocked_parameters[param] = list(params_dict).index(param)
#
#     return unlocked_parameters
#
#
# def modify_save_file(slected_params, unlocked_params, params_dict):
#     for param in slected_params:
#         if param not in unlocked_params.keys():
#             flags.append(format_to_json(param, params_dict))
#
#     for param in unlocked_params.keys():
#         if param not in slected_params:
#             flags.remove(format_to_json(param, params_dict))
#
#
# def write_to_save_file():
#     with open(file_path, "w", encoding="utf-8") as mod_savefile:
#         json.dump(data, mod_savefile, separators=(',', ':'))


# "Your save file should be located at: C:\Program Files (x86)\Steam\userdata\[Number]\632360\remote\UserProfiles"
def manage_characters():
    characters = {
        "Acrid": 'acrid',
        "Artificer": 'arti',
        "Bandit": 'bandit',
        "Loader": 'loader',
        "Han-D": 'hand',
        "Mercenary": 'mercenary',
        "Pilot": 'pilot',
        "Sniper": 'sniper',
        "Enforcer": 'enforcer',
        "Drifter": 'drifter',
        "Engineer": 'engineer',
        "Chef": 'chef',
        "Miner": 'miner'
    }

    unlocked_char = {}

    # Creates the formating for the json of the characters
    def format_name(name):
        name = name in characters
        return f'challenge_unlock_{name}_completed'

    # Check to see what is unlocked and what is not
    def check_char_name():
        for name in characters:
            form_name = format_name(name)

            if form_name in flags:
                unlocked_char[name] = list(characters).index(name)

    check_char_name()

    console.print("Manage game characters")
    # Choose multiple options from a list
    char_list = select_multiple(list(characters.keys()), tick_style='green', cursor_style='green',
                                ticked_indices=list(unlocked_char.values()))

    for char_name in char_list:
        if char_name not in unlocked_char.keys():
            flags.append(format_name(char_name))

    for char_name in unlocked_char.keys():
        if char_name not in char_list:
            flags.remove(format_name(char_name))

    print(char_list)

    with open(file_path, "w", encoding="utf-8") as mod_savefile:
        json.dump(data, mod_savefile, separators=(',', ':'))


def manage_skills():
    skills = {
        "Corrosive Wounds": 'acrid_z2',
        "Toxic Bubble": 'acrid_x2',
        "Dissolving Ambush": 'acrid_c2',
        "Pulse Spear": 'arti_x2',
        "Tectonic Surge": 'arti_c2',
        "Localized Sun": 'arti_z2',
        "Whip": 'bandit_z2',
        "Flashbang": 'bandit_c2',
        "Standoff": 'bandit_v2',
        "Bullet Punch": 'loader_z2',
        "Short Circuit": 'loader_x2',
        "S260 Conduit": 'loader_v2',
        "DRONE - BLAST": 'hand_x2',
        "DISASSEMBLE": 'hand_x3',
        "DRONE - SPEED": 'hand_v2',
        "Focused Strike": 'mercenary_x2',
        "Skyward Assault": 'mercenary_c2',
        "After-Image": 'mercenary_v2',
        "Rapid Fire": 'pilot_z2',
        "Aerial Support": 'pilot_c2',
        "Aerobatics": 'pilot_v2',
        "Improvise": 'sniper_z2',
        "Heavy Recoil": 'sniper_x2',
        "Quickscope": 'sniper_c2',
        "Shrapnel Grenade": 'enforcer_z2',
        "Shield Tackle": 'enforcer_x2',
        "Disperse": 'enforcer_c2',
        "Tornado Slam": 'drifter_z2',
        "Scrap Cube": 'drifter_x2',
        "Recycle": 'drifter_c2',
        "V.0.2 Prototype Laser Turret": 'engi_x2',
        "Mortar Barrage": 'engi_c2',
        "Shockwave Mine": 'engi_v2',
        "OIL JAR": 'chef_z2',
        "SLICE": 'chef_c2',
        "COOK": 'chef_v2',
        "Drill Dash": 'miner_z2',
        "Throwing Axe": 'miner_x2',
        "Burnout": 'miner_c2'
    }

    characters = {
        "Acrid": 'acrid',
        "Artificer": 'arti',
        "Bandit": 'bandit',
        "Loader": 'loader',
        "Han-D": 'hand',
        "Mercenary": 'mercenary',
        "Pilot": 'pilot',
        "Sniper": 'sniper',
        "Enforcer": 'enforcer',
        "Drifter": 'drifter',
        "Engineer": 'engi',
        "Chef": 'chef',
        "Miner": 'miner'
    }

    def get_pc_skills(pc_name):
        pc_skills = {}
        for key, value in skills.items():
            if characters[pc_name] in value:
                pc_skills[key] = value

        return pc_skills

    def get_unlocked_skills(pc_skills):
        unlocked_skills = {}

        for skill in pc_skills:
            formated_skill = format_to_json(skill, pc_skills)

            if formated_skill in flags:
                unlocked_skills[skill] = list(pc_skills).index(skill)

        return unlocked_skills

    # Choose one item from a list
    char_choice = select(list(characters.keys()), cursor="🢧", cursor_style="green")

    all_pc_skills = get_pc_skills(char_choice)
    unlocked_pc_skills = get_unlocked_skills(all_pc_skills)

    skills_list = select_multiple(list(all_pc_skills.keys()), tick_style='green', cursor_style='green',
                                  ticked_indices=list(unlocked_pc_skills.values()))

    for pc_skill in skills_list:
        if pc_skill not in unlocked_pc_skills.keys():
            flags.append(format_to_json(pc_skill, all_pc_skills))

    for pc_skill in unlocked_pc_skills.keys():
        if pc_skill not in skills_list:
            flags.remove(format_to_json(pc_skill, all_pc_skills))

    with open(file_path, "w", encoding="utf-8") as mod_savefile:
        json.dump(data, mod_savefile, separators=(',', ':'))


logo = """


                                @@@@@@@@@@@       #
                             @@@@@@@@@@@@@@@@@  &@ #    ,@*
                           @@@@@@@@@@@@@@@@@@@@@         (@
                          @@@@@@@@@@@@@@@@@@@@@@@,       (
                         ,@@@@@@@@@@                    @
                         ,@@@@@@@@@@@@@             #@#
                          @@@@@@@@@               *@
                        @@@@@@@@@@@@            @@
                       @@    @@@@@@@@@@@%@@@@@@    @@ @@@
                      @@         @@@@@@@@@@@      @@@@@@@@
                     .,              @@@         @ @@@@@@
                      @@    *  @@            (& @* @@@@@@%
                                                @@@@@@@

"""
logo_text = r"""
   ___  _     __          ___  ___       _        ___      __
  / _ \(_)__ / /__  ___  / _/ / _ \___ _(_)__    / _ \___ / /___ _________  ___
 / , _/ (_-</  '_/ / _ \/ _/ / , _/ _ `/ / _ \  / , _/ -_) __/ // / __/ _ \(_-<
/_/|_/_/___/_/\_\  \___/_/  /_/|_|\_,_/_/_//_/ /_/|_|\__/\__/\_,_/_/ /_//_/___/
          / __/__ __  _____ / _(_) /__   ___ ___/ (_) /____  ____
         _\ \/ _ `/ |/ / -_) _/ / / -_) / -_) _  / / __/ _ \/ __/
        /___/\_,_/|___/\__/_//_/_/\__/  \__/\_,_/_/\__/\___/_/
v1.0
"""


def main_menu():
    console.print(logo_text)

    # Confirm a dialog
    options = [
        "Unlock Characters",
        "Unlock Abilities",
        "Unlock Skins",
        "Unlock Artifacts",
        "Exit",
    ]
    # Choose one item from a list
    choice = select(options, cursor="🢧", cursor_style="green")

    return choice


menu_choice = True
while menu_choice:
    console.clear()
    menu_choice = main_menu()

    if menu_choice == "Unlock Characters":
        console.clear()
        # manage_characters()
    elif menu_choice == "Unlock Abilities":
        console.clear()
        manage_skills()
    elif menu_choice == "Exit":
        console.clear()
        break

console.clear()
print(logo)
input("                            Press Enter to continue...")

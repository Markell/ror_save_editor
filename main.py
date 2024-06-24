import json
from beaupy import select, select_multiple
from rich.console import Console

console = Console()

file_path = '0_localsave.json'
with open(file_path, 'r', encoding="utf-8") as savefile:  # Opens the json file
    data = json.load(savefile)  # Reads the file as json
flags = data["flags"]  # Grabs the "flags" list from the json


# "Your save file should be located at: C:\Program Files (x86)\Steam\userdata\[Number]\632360\remote\UserProfiles"
def manage_characters():
    characters = {
        "Acrid": 'acrid',
        "Arti": 'arti',
        "Bandit": 'bandit',
        "Loader": 'loader',
        "Hand": 'hand',
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
        name = characters.get(name)
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


def manage_abilities():
    print("hello")


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
    print(logo_text)

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
        manage_characters()
    elif menu_choice == "Unlock Abilities":
        console.clear()
        manage_abilities()
    elif menu_choice == "Exit":
        console.clear()
        break
console.clear()
print(logo)
input("                            Press Enter to continue...")

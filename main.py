import json
from beaupy import select, select_multiple
from rich.console import Console

console = Console()

path = '0_localsave.json'
with open(path, 'r') as infile:  # Opens the json file
    jsn = json.load(infile)  # Reads the file as json
flags = jsn["flags"]  # Grabs the "flags" list from the json

# "Your save file should be located at: C:\Program Files (x86)\Steam\userdata\[Number]\632360\remote\UserProfiles"


def manage_characters():
    unlocked_char_index = []
    unlocked_char_value = []
    characters = ['acrid', 'arti', 'bandit', 'loader', 'hand', 'mercenary', 'pilot', 'sniper', 'enforcer', 'drifter',
                  'engineer', 'chef', 'miner', 'robomando']

    new_characters = {
        'acrid': "Acrid",
        'arti': "Arti",
        'bandit': "Bandit",
        'loader': "Loader",
        'hand': "Hand",
        'mercenary': "Mercenary",
        'pilot': "Pilot",
        'sniper': "Sniper",
        'enforcer': "Enforcer",
        'drifter': "Drifter",
        'engineer': "Engineer",
        'chef': "Chef",
        'miner': "Miner"
    }

    # Creates the formating for the json of the characters
    def format_name(character):
        return f'challenge_unlock_{character}_completed'

    # Check to see what is unlocked and what is not
    def check_char_name():
        for name in characters:
            form_name = format_name(name)

            if form_name in flags:
                unlocked_char_index.append(characters.index(name))
                unlocked_char_value.append(name)

    check_char_name()

    console.print("Manage game characters")

    # Choose multiple options from a list
    char_to_edit = select_multiple(characters, tick_style='green', cursor_style='green',
                                   ticked_indices=unlocked_char_index)

    if char_to_edit:  # Check if selection is not empty (esc key pressed)
        for char_name in char_to_edit:
            if char_name not in unlocked_char_value:
                flags.append(format_name(char_name))

        for char_name in unlocked_char_value:
            if char_name not in char_to_edit:
                flags.remove(format_name(char_name))

        json_data = json.dumps(jsn, separators=(',', ':'))
        open(path, 'w').write(json_data)

        # Remove spaces that are not there in the save file before
        with_spaces = open(path, 'r').read()
        without_spaces = with_spaces.replace(' ', '')
        open(path, 'w').write(without_spaces)


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

import json
from beaupy import select, select_multiple
from rich.console import Console

console = Console()

file_path = '0_localsave.json'
with open(file_path, 'r', encoding="utf-8") as savefile:  # Opens the json file
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
    for param in slected_params:
        if param not in unlocked_params.keys():
            flags.append(format_to_json(param, params_dict))

    for param in unlocked_params.keys():
        if param not in slected_params:
            flags.remove(format_to_json(param, params_dict))


def write_to_save_file():
    with open(file_path, "w", encoding="utf-8") as mod_savefile:
        json.dump(data, mod_savefile, separators=(',', ':'))


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
characters = {"Acrid": 'acrid', "Artificer": 'arti', "Bandit": 'bandit', "Loader": 'loader', "Han-D": 'hand',
              "Mercenary": 'mercenary', "Pilot": 'pilot', "Sniper": 'sniper', "Enforcer": 'enforcer',
              "Drifter": 'drifter', "Engineer": 'engineer', "Chef": 'chef', "Miner": 'miner'
              }
s_characters = {"Acrid": 'acrid', "Artificer": 'arti', "Bandit": 'bandit', "Loader": 'loader', "Han-D": 'hand',
                "Mercenary": 'mercenary', "Pilot": 'pilot', "Sniper": 'sniper', "Enforcer": 'enforcer',
                "Drifter": 'drifter', "Engineer": 'engi', "Chef": 'chef', "Miner": 'miner'
                }

skills = {"Corrosive Wounds": 'acrid_z2', "Toxic Bubble": 'acrid_x2', "Dissolving Ambush": 'acrid_c2',
          "Pulse Spear": 'arti_x2', "Tectonic Surge": 'arti_c2', "Localized Sun": 'arti_z2',
          "Whip": 'bandit_z2', "Flashbang": 'bandit_c2', "Standoff": 'bandit_v2',
          "Bullet Punch": 'loader_z2', "Short Circuit": 'loader_x2', "S260 Conduit": 'loader_v2',
          "DRONE - BLAST": 'hand_x2', "DISASSEMBLE": 'hand_x3', "DRONE - SPEED": 'hand_v2',
          "Focused Strike": 'mercenary_x2', "Skyward Assault": 'mercenary_c2', "After-Image": 'mercenary_v2',
          "Rapid Fire": 'pilot_z2', "Aerial Support": 'pilot_c2', "Aerobatics": 'pilot_v2',
          "Improvise": 'sniper_z2', "Heavy Recoil": 'sniper_x2', "Quickscope": 'sniper_c2',
          "Shrapnel Grenade": 'enforcer_z2', "Shield Tackle": 'enforcer_x2', "Disperse": 'enforcer_c2',
          "Tornado Slam": 'drifter_z2', "Scrap Cube": 'drifter_x2', "Recycle": 'drifter_c2',
          "V.0.2 Prototype Laser Turret": 'engi_x2', "Mortar Barrage": 'engi_c2', "Shockwave Mine": 'engi_v2',
          "OIL JAR": 'chef_z2', "SLICE": 'chef_c2', "COOK": 'chef_v2',
          "Drill Dash": 'miner_z2', "Throwing Axe": 'miner_x2', "Burnout": 'miner_c2'
          }

skins = {"Acrid Prism Skin": 'acrid_skin_s', "Acrid Last Providence Trial Skin": 'acrid_skin_p',
         "Artificer Prism Skin": 'arti_skin_s', "Artificer Last Providence Trial Skin": 'arti_skin_p',
         "Bandit Prism Skin": 'bandit_skin_s', "Bandit Last Providence Trial Skin": 'bandit_skin_p',
         "Loader Prism Skin": 'loader_skin_s', "Loader Last Providence Trial Skin": 'loader_skin_p',
         "Hand-D Trial Skin": 'hand_skin_a', "Hand-D Last Providence Trial Skin": 'hand_skin_p',
         "Mercenary Prism Skin": 'mercenary_skin_s', "Mercenary Last Providence Trial Skin": 'mercenary__skin_p',
         "Pilot Trial Skin": 'pilot_skin_a', "Pilot Last Providence Trial Skin": 'pilot_skin_p',
         "Sniper Trial Skin": 'sniper_skin_a', "Sniper Last Providence Trial Skin": 'sniper_skin_p',
         "Enforcer Trial Skin": 'enforcer_skin_a', "Enforcer Prism Skin": 'enforcer_skin_s',
         "Enforcer Last Providence Trial Skin": 'enforcer_skin_p',
         "Drifter Prism Skin": 'drifter_skin_s', "Drifter Last Providence Trial Skin": 'drifter_skin_p',
         "Engineer Last Providence Trial Skin": 'engineer_skin_p',
         "Chef Prism Skin": 'chef_skin_s', "Chef Last Providence Trial Skin": 'chef_skin_p',
         "Miner Trial Skin": 'miner_skin_a', "Miner Last Providence Trial Skin": 'miner_skin_p'
         }

artifacts = {"Honor": 'artifact_honor', "Kin": 'artifact_kin', "Distortion": 'artifact_distortion',
             "Spite": 'artifact_spite', "Glass": 'artifact_glass', "Enigma": 'artifact_enigma',
             "Sacrifice": 'artifact_sacrifice', "Command": 'artifact_command', "Spirit": 'artifact_spirit',
             "Origin": 'artifact_origin', "Mountain": 'artifact_mountain', "Dissonance": 'artifact_dissonance',
             "Temporary": 'artifact_temporary', "Cognation": 'artifact_cognation'
             }


# "Your save file should be located at: C:\Program Files (x86)\Steam\userdata\[Number]\632360\remote\UserProfiles"
def modify_characters():
    unlocked_pc = get_unlocked_param(characters)

    console.print("Manage game characters")
    # Choose multiple options from a list
    slelected_pc = select_multiple(list(characters.keys()), tick_style='green', cursor_style='green',
                                   ticked_indices=list(unlocked_pc.values()))

    edit_save_file(slelected_pc, unlocked_pc, characters)

    write_to_save_file()


def modify_skills():
    console.print("Choose a character to unlock abilities ([bold]esc[/bold] to return)")
    selected_pc = select(list(s_characters.keys()), cursor="🢧", cursor_style="green")
    while selected_pc:
        all_pc_skills = get_pc_param(selected_pc, s_characters, skills)
        unlocked_pc_skills = get_unlocked_param(all_pc_skills)

        console.clear()
        # console.print(logo_text)
        console.print(selected_pc, "abilities ([bold]esc[/bold] to return)")
        selected_skills = select_multiple(list(all_pc_skills.keys()), tick_style='green', cursor_style='green',
                                          ticked_indices=list(unlocked_pc_skills.values()))

        edit_save_file(selected_skills, unlocked_pc_skills, all_pc_skills)
        write_to_save_file()

        console.clear()
        # console.print(logo_text)
        console.print("Choose a character to unlock abilities ([bold]esc[/bold] to return)")
        selected_pc = select(list(s_characters.keys()), cursor="🢧", cursor_style="green",
                             cursor_index=list(s_characters.keys()).index(selected_pc))


def modify_skins():
    console.clear()
    console.print("Choose a character to unlock skins ([bold]esc[/bold] to return)")
    selected_pc = select(list(characters.keys()), cursor="🢧", cursor_style="green")
    while selected_pc:
        all_pc_skins = get_pc_param(selected_pc, characters, skins)
        unlocked_pc_skins = get_unlocked_param(all_pc_skins)

        console.clear()
        # console.print(logo_text)
        console.print(selected_pc, "skins ([bold]esc[/bold] to return)")
        selected_skins = select_multiple(list(all_pc_skins.keys()), tick_style='green', cursor_style='green',
                                         ticked_indices=list(unlocked_pc_skins.values()))

        edit_save_file(selected_skins, unlocked_pc_skins, all_pc_skins)

        write_to_save_file()

        console.clear()
        # console.print(logo_text)
        console.print("Choose a character to unlock skins ([bold]esc[/bold] to return)")
        selected_pc = select(list(characters.keys()), cursor="🢧", cursor_style="green",
                             cursor_index=list(characters.keys()).index(selected_pc))


def modify_artifacts():
    unlocked_artifacts = get_unlocked_param(artifacts)

    console.print("Manage game artifacts")
    # Choose multiple options from a list
    slelected_artifacts = select_multiple(list(artifacts.keys()), tick_style='green', cursor_style='green',
                                          ticked_indices=list(unlocked_artifacts.values()))

    edit_save_file(slelected_artifacts, unlocked_artifacts, artifacts)

    write_to_save_file()


logo_img = """


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


def main_menu():
    console.print(logo_text)

    # Confirm a dialog
    options = ["Unlock Characters", "Unlock Abilities", "Unlock Skins", "Unlock Artifacts", "Exit"]
    # Choose one item from a list
    choice = select(options, cursor="🢧", cursor_style="green")

    return choice


menu_choice = True
while menu_choice:
    console.clear()
    menu_choice = main_menu()

    if menu_choice == "Unlock Characters":
        console.clear()
        modify_characters()
    elif menu_choice == "Unlock Abilities":
        console.clear()
        modify_skills()
    elif menu_choice == "Unlock Skins":
        console.clear()
        modify_skins()
    elif menu_choice == "Unlock Artifacts":
        console.clear()
        modify_artifacts()
    elif menu_choice == "Exit":
        console.clear()
        break

console.clear()
console.print(logo_img)
console.input("                            Press [bold]Enter[/bold] to continue...")

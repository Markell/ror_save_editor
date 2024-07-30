import sys

from beaupy import select, select_multiple
from rich.console import Console
from . import core
import os
import fnmatch
from beaupy import DefaultKeys

logo_game = r"""
   ___  _     __          ___  ___       _        ___      __
  / _ \(_)__ / /__  ___  / _/ / _ \___ _(_)__    / _ \___ / /___ _________  ___
 / , _/ (_-</  '_/ / _ \/ _/ / , _/ _ `/ / _ \  / , _/ -_) __/ // / __/ _ \(_-<
/_/|_/_/___/_/\_\  \___/_/  /_/|_|\_,_/_/_//_/ /_/|_|\__/\__/\_,_/_/ /_//_/___/"""
logo_editor = r"""
          / __/__ __  _____ / _(_) /__   ___ ___/ (_) /____  ____
         _\ \/ _ `/ |/ / -_) _/ / / -_) / -_) _  / / __/ _ \/ __/
        /___/\_,_/|___/\__/_//_/_/\__/  \__/\_,_/_/\__/\___/_/
v1.0
"""
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

console = Console()
# Try to find in current dir save file by part of it name otherwise call file picker
savefile = core.check_savefile(fnmatch.filter(os.listdir('.'), '*save.json'))


def int_savefile():
    """
    Check save backup and open save file
    """
    core.check_backup(savefile)
    core.open_save_file(savefile)


def modify_characters():
    """
    Manage unlockable characters
    """
    unlocked_pc = core.get_unlocked_param(characters)

    console.print("Manage game characters ([bold]esc[/bold] to return)", style="#d68438")
    slelected_pc = select_multiple(list(characters.keys()), tick_style='green', cursor_style='green',
                                   ticked_indices=list(unlocked_pc.values()))

    core.edit_save_file(slelected_pc, unlocked_pc, characters)
    core.write_to_save_file(savefile)


def modify_skills():
    """
    Manage unlockable skils for each character
    """
    console.print("Choose a character to unlock abilities ([bold]esc[/bold] to return)", style="#d68438")
    selected_pc = select(list(s_characters.keys()), cursor="🢧", cursor_style="green")

    while selected_pc:
        all_pc_skills = core.get_pc_param(selected_pc, s_characters, skills)
        unlocked_pc_skills = core.get_unlocked_param(all_pc_skills)

        console.clear()
        console.print(logo_game, highlight=False, style="#d68438", end='')
        console.print(logo_editor, highlight=False, style="#4bb39a")
        console.print(selected_pc, "abilities ([bold]esc[/bold] to return)", style="#d68438")

        selected_skills = select_multiple(list(all_pc_skills.keys()), tick_style='green', cursor_style='green',
                                          ticked_indices=list(unlocked_pc_skills.values()))

        core.edit_save_file(selected_skills, unlocked_pc_skills, all_pc_skills)
        core.write_to_save_file(savefile)

        console.clear()
        console.print(logo_game, highlight=False, style="#d68438", end='')
        console.print(logo_editor, highlight=False, style="#4bb39a")
        console.print("Choose a character to unlock abilities ([bold]esc[/bold] to return)", style="#d68438")

        selected_pc = select(list(s_characters.keys()), cursor="🢧", cursor_style="green",
                             cursor_index=list(s_characters.keys()).index(selected_pc))


def modify_skins():
    """
    Manage unlockable skins for each character
    """
    console.clear()
    console.print(logo_game, highlight=False, style="#d68438", end='')
    console.print(logo_editor, highlight=False, style="#4bb39a")
    console.print("Choose a character to unlock skins ([bold]esc[/bold] to return)", style="#d68438")

    selected_pc = ['Acrid']
    selected_pc = select(list(characters.keys()), cursor="🢧", cursor_style="green")

    while selected_pc:
        all_pc_skins = core.get_pc_param(selected_pc, characters, skins)
        unlocked_pc_skins = core.get_unlocked_param(all_pc_skins)

        console.clear()
        console.print(logo_game, highlight=False, style="#d68438", end='')
        console.print(logo_editor, highlight=False, style="#4bb39a")

        console.print(selected_pc, "skins ([bold]esc[/bold] to return)", style="#d68438")

        selected_skins = select_multiple(list(all_pc_skins.keys()), tick_style='green', cursor_style='green',
                                         ticked_indices=list(unlocked_pc_skins.values()))

        core.edit_save_file(selected_skins, unlocked_pc_skins, all_pc_skins)
        core.write_to_save_file(savefile)

        console.clear()
        console.print(logo_game, highlight=False, style="#d68438", end='')
        console.print(logo_editor, highlight=False, style="#4bb39a")
        console.print("Choose a character to unlock skins ([bold]esc[/bold] to return)", style="#d68438")

        selected_pc = select(list(characters.keys()), cursor="🢧", cursor_style="green",
                             cursor_index=list(characters.keys()).index(selected_pc))


def modify_artifacts():
    """
    Manage unlockable artifacts
    """
    unlocked_artifacts = core.get_unlocked_param(artifacts)

    console.print("Manage game artifacts ([bold]esc[/bold] to return)", style="#d68438")
    slelected_artifacts = select_multiple(list(artifacts.keys()), tick_style='green', cursor_style='green',
                                          ticked_indices=list(unlocked_artifacts.values()))

    core.edit_save_file(slelected_artifacts, unlocked_artifacts, artifacts)
    core.write_to_save_file(savefile)


def main_menu(selected_item):
    """
    Main menu options selection
    :param selected_item: current cursor position
    """
    console.print(logo_game, highlight=False, style="#d68438", end='')
    console.print(logo_editor, highlight=False, style="#4bb39a")

    options = ["Unlock Characters", "Unlock Abilities", "Unlock Skins", "Unlock Artifacts", "Exit"]
    choice = select(options, cursor="🢧", cursor_style="green", cursor_index=options.index(selected_item))

    return choice

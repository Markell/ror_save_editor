import ror_save_editor as editor
from ror_save_editor.core import check_backup, check_savefile, open_save_file
from rich.console import Console

console = Console()


def run():
    save_file = check_savefile('0_localsave.json')
    check_backup(save_file)
    open_save_file(save_file)

    menu_choice = "Unlock Characters"  # Initial cursor position
    while menu_choice:
        console.clear()
        menu_choice = editor.main_menu(menu_choice)

        if menu_choice == "Unlock Characters":
            editor.modify_characters(save_file)
        elif menu_choice == "Unlock Abilities":
            editor.modify_skills(save_file)
        elif menu_choice == "Unlock Skins":
            editor.modify_skins(save_file)
        elif menu_choice == "Unlock Artifacts":
            editor.modify_artifacts(save_file)
        elif menu_choice == "Exit":
            console.clear()
            break

    console.clear()
    console.print(editor.logo_img, highlight=False, style="#ffd557")
    console.input("                            Press [bold]Enter[/bold] to continue...")


# Run the function if this is the main file executed
if __name__ == "__main__":
    run()

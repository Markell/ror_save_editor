import ror_save_editor as editor
from rich.console import Console

console = Console()


def run():
    editor.int_savefile()
    menu_choice = "Unlock Characters"  # Initial cursor position
    while menu_choice:
        console.clear()
        menu_choice = editor.main_menu(menu_choice)

        if menu_choice == "Unlock Characters":
            editor.modify_characters()
        elif menu_choice == "Unlock Abilities":
            editor.modify_skills()
        elif menu_choice == "Unlock Skins":
            editor.modify_skins()
        elif menu_choice == "Unlock Artifacts":
            editor.modify_artifacts()
        elif menu_choice == "Exit":
            console.clear()
            break

    console.clear()
    console.print(editor.logo_img, highlight=False, style="#ffd557")
    console.print("                                  See You Space Cowboy...")
    console.input("                            Press [bold]Enter[/bold] to continue...")


# Run the function if this is the main file executed
if __name__ == "__main__":
    run()

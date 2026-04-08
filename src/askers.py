from typing  import Literal
from pathlib import Path
from tkinter import filedialog
import os



def ask_removal_style() -> Literal[
        "normal_deleting",
        "normal_deleting_recursive",
        "cautious_deleting",
        "cautious_deleting_recursive",
        "exit"]:
    returns_dict = {
        "n":  "normal_deleting",
        "nr": "normal_deleting_recursive",
        "c":  "cautious_deleting",
        "cr": "cautious_deleting_recursive",
        "e":  "exit"}

    while True:
        print("Normal deleting means deleting all DS_Store files and ones starting with '._'\n"
              "Cautious deleting means deleting all DS_Store files and only AppleDouble files \n"
              "that have a corresponding file in current directory.\n\n"
              "Choose deleting option:\n"
              "n  - Normal deleting\n"
              "nr - Normal deleting (recursive)\n"
              "c  - Cautious deleting\n"
              "cr - Cautious deleting (recursive)\n"
              "e  - Exit\n"
              ">> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Invalid input\n\n")


def ask_path_filedialog(start_path: Path) -> Path | None:
    og_path = Path.cwd()
    os.chdir(start_path)

    selected_path = ""
    message = "Choose audio directory"
    selected_path = filedialog.askdirectory(title=message)

    if selected_path == "":
        return
    selected_path = Path(selected_path)

    os.chdir(og_path)
    return selected_path

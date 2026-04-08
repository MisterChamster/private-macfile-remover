from typing  import Literal
from pathlib import Path
from tkinter import filedialog



def ask_removal_style() -> Literal[""]:
    return ""


def ask_path_filedialog() -> Path | None:
    selected_path = ""
    message = "Choose audio directory"
    selected_path = filedialog.askdirectory(title=message)

    if selected_path == "":
        return
    selected_path = Path(selected_path)

    return selected_path

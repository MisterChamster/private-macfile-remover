from pathlib import Path

import src.askers as askers
from src.dir_remover import DirRemover



proj_path = Path(__file__).resolve().parent.parent.parent

def main_loop() -> None:
    while True:
        removal_style = askers.ask_removal_style()
        if removal_style == "exit":
            return

        removal_path = askers.ask_path_filedialog(proj_path)
        if removal_path is None:
            return
        else:
            removal_path = Path(removal_path)

        if removal_style == "normal_deleting":
            DirRemover.remove_macfiles_dir(removal_path)
            DirRemover.print_and_reset_all_kb()
        elif removal_style == "normal_deleting_recursive":
            DirRemover.remove_macfiles_recur(removal_path)
            DirRemover.print_and_reset_all_kb()
        elif removal_style == "cautious_deleting":
            DirRemover.cautious_remove_macfiles_dir(removal_path)
            DirRemover.print_and_reset_all_kb()
        elif removal_style == "cautious_deleting_recursive":
            DirRemover.cautious_remove_macfiles_recur(removal_path)
            DirRemover.print_and_reset_all_kb()

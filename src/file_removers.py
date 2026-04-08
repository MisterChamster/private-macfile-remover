from pathlib import Path
import os

import src.utils as utils



def remove_macfiles_dir(dir_path: Path) -> None:
    files_paths = utils.get_files_from_dir(dir_path)
    for node_path in files_paths:
        if utils.is_file_macfile(node_path):
            os.remove(node_path)


def cautious_remove_macfiles_dir(dir_path: Path) -> None:
    return

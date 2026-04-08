from pathlib import Path
import os

import src.utils as utils



def remove_macfiles_dir(dir_path: Path) -> None:
    files_paths = utils.get_files_from_dir(dir_path)
    for node_path in files_paths:
        if utils.is_file_macfile(node_path):
            os.remove(node_path)


def remove_dsstore_dir(dir_path: Path) -> None:
    files_paths = utils.get_files_from_dir(dir_path)
    for node_path in files_paths:
        if utils.is_file_dsstore(node_path):
            os.remove(node_path)


def cautious_remove_macfiles_dir(dir_path: Path) -> None:
    macfiles_paths = utils.get_macfile_paths_dir(dir_path)
    not_macfiles_paths = utils.get_not_macfile_paths_dir(dir_path)
    remove_dsstore_dir(macfiles_paths)

    return

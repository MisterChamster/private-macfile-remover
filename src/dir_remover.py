from pathlib import Path
import os

import src.utils as utils


class DirRemover():
    del_counter = 0


    @staticmethod
    def remove_macfiles_dir(dir_path: Path) -> None:
        files_paths = utils.get_files_from_dir(dir_path)
        for node_path in files_paths:
            if utils.is_file_macfile(node_path):
                os.remove(node_path)
                DirRemover.del_counter += 1


    @staticmethod
    def __remove_dsstore_dir(dir_path: Path) -> None:
        files_paths = utils.get_files_from_dir(dir_path)
        for node_path in files_paths:
            if utils.is_file_dsstore(node_path):
                os.remove(node_path)
                DirRemover.del_counter += 1


    @staticmethod
    def cautious_remove_macfiles_dir(dir_path: Path) -> None:
        macfiles_paths = utils.get_macfile_paths_dir(dir_path)
        DirRemover.__remove_dsstore_dir(macfiles_paths)
        paths_to_remove = []

        for macfile_path in macfiles_paths:
            cleared_name = macfile_path.name[2:]
            path_to_check = dir_path / cleared_name

            if path_to_check.exists():
                paths_to_remove.append(macfile_path)

        for macfile_path in paths_to_remove:
            os.remove(macfile_path)
            DirRemover.del_counter += 1


    @staticmethod
    def remove_macfiles_recur(dir_path: Path) -> None:
        print(f"Visiting: {dir_path}")
        DirRemover.remove_macfiles_dir(dir_path)

        dirs_paths = utils.get_dirs_from_dir(dir_path)
        for dir_path in dirs_paths:
            DirRemover.remove_macfiles_recur(dir_path)


    @staticmethod
    def cautious_remove_macfiles_recur(dir_path: Path) -> None:
        print(f"Visiting: {dir_path}")
        DirRemover.cautious_remove_macfiles_dir(dir_path)

        dirs_paths = utils.get_dirs_from_dir(dir_path)
        for dir_path in dirs_paths:
            DirRemover.cautious_remove_macfiles_recur(dir_path)

    @staticmethod
    def get_and_reset_del_count() -> int:
        temp = DirRemover.del_counter
        DirRemover.del_counter = 0
        return temp

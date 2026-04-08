from pathlib import Path

import src.utils as utils
import src.file_removers as removers



class Recurrer():
    @staticmethod
    def remove_macfiles_recur(dir_path: Path) -> None:
        print(f"Visiting: {dir_path}")
        removers.remove_macfiles_dir(dir_path)

        dirs_paths = utils.get_dirs_from_dir(dir_path)
        for dir_path in dirs_paths:
            Recurrer.remove_macfiles_recur(dir_path)


    @staticmethod
    def cautious_remove_macfiles_recur(dir_path: Path) -> None:
        print(f"Visiting: {dir_path}")
        removers.cautious_remove_macfiles_dir(dir_path)

        dirs_paths = utils.get_dirs_from_dir(dir_path)
        for dir_path in dirs_paths:
            Recurrer.cautious_remove_macfiles_recur(dir_path)

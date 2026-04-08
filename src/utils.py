from pathlib import Path



def is_file_macfile(filepath: Path) -> bool:
    filename = filepath.name
    return is_filename_macfile(filename)


def is_filename_macfile(filename: str) -> bool:
    if filename.startswith("DS_Store"):
        return True
    if filename.startswith("._"):
        return True
    return False


def get_files_from_dir(dir_path: Path) -> list[Path]:
    files_paths = []

    for node_path in dir_path.iterdir():
        if node_path.is_file():
            files_paths.append(node_path)
    return files_paths


def get_dirs_from_dir(dir_path: Path) -> list[Path]:
    dirs_paths = []

    for node_path in dir_path.iterdir():
        if node_path.is_dir():
            dirs_paths.append(node_path)
    return dirs_paths


def get_macfile_paths_dir(dir_path: Path) -> list[Path]:
    files_paths = get_files_from_dir(dir_path)

    for node_path in files_paths:
        pass


def get_not_macfile_paths_dir(dir_path: Path) -> list[Path]:
    files_paths = get_files_from_dir(dir_path)

    for node_path in files_paths:
        pass

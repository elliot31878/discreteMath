

import os
from typing import List


class DirManager:

    def __init__(self):
        super(DirManager, self).__init__()

        self.current_directory = os.getcwd()

    @property
    def current_dir(self):
        return self.current_directory

    def get_all_directory(self, path, level: int = 0):
        list_dirs: List = list()

        main_dir = path.rstrip(os.path.sep)
        assert os.path.isdir(main_dir)

        main_dir_level = main_dir.count(os.path.sep)
        for root, dirs, _ in os.walk(main_dir):
            list_dirs = [item for item in dirs if not item == "__pycache__"]
            num_sep_this = root.count(os.path.sep)
            if main_dir_level + level <= num_sep_this:
                del dirs[:]
        list_dirs.sort(reverse=True)

        return list_dirs

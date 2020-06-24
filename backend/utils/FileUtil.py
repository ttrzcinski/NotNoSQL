import os
import fnmatch
from pathlib import Path


class FileUtil:
    """ Set of tools to operate with files. """

    @staticmethod
    def file_exists(file_path) -> bool:
        """ Checks, if pointed file exists. """
        checked_file = Path(file_path)
        return checked_file.is_file() and checked_file.exists()

    @staticmethod
    def load_file(file_path: str) -> dict:
        """ Reads Key-Value pairs from pointed file. """
        # Check, if file even exists
        if not FileUtil.file_exists(file_path):
            print('Couldn\'t find file ' + file_path)
            return None

        # Read key-pairs from file
        result = {}
        with open(file_path) as read_file:
            for line in read_file:
                # Omit comments and empty lines
                if line.startswith('#') or len(line.split()) == 0:
                    continue
                # Parse line into key-value
                name, var = line.partition("=")[::2]
                result[name.strip()] = var
        print('Read whole file ' + file_path + ' into ' + str(len(result)) + ' entries.')
        return result

    @staticmethod
    def list_fies(dir_path: str, pattern='*') -> list:
        """ Lists files within directory matching given pattern (or all, if pattern not given). """
        # Fix pattern
        if len(pattern.strip()) == 0:
            pattern = '*'
        # Check dir_path
        if dir_path is None or len(dir_path) == 0:
            print('Directory path was not given.')
            return None
        # Check entered params
        the_dir = Path(dir_path)
        if not the_dir.is_dir():
            print('Not a directory path - ' + dir_path)
            return None
        return fnmatch.filter(os.listdir(the_dir), pattern)

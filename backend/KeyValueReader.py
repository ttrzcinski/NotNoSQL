from backend.utils.FileUtil import FileUtil


class KeyValueReader:
    """ Reads pointed file and keeps read data in key-values. """

    # Kept Key-Value pairs
    __pairs = {}

    def __init__(self, file_name, parent_directory='backend'):
        """ Creates new instance of Key-Value parser with loading wanted file. """
        self.__pairs = FileUtil.load_file(parent_directory + '/resources/' + file_name)

    def exists_key(self, key):
        """ Checks, if wanted key exists in the parsed file. """
        return True if key in self.__pairs else False

    def value_of(self, key):
        """ Passed read value matching pointed key. """
        fixed_key = key.strip().upper()
        return self.__pairs[fixed_key].strip() if len(self.__pairs) > 0 and self.exists_key(fixed_key) else None

import os


class Utils:
    @staticmethod
    def folder_init(dirpath):
        if not os.path.isdir(dirpath):
            os.mkdir(dirpath)

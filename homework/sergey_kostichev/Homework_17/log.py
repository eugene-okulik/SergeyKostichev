import os


class Log:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_name(self):
        return os.path.basename(self.file_path)

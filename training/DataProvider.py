import os
class DataProvider:
    pass


class FolderDataProvider:
    def __init__(self, folder_path):
        self.files = list(os.listdir(folder_path))

    def get_random(self,idx):
        pass

import os
import numpy as np

class DataProviderFactory:
    @staticmethod
    def get_generator(name):
        if name == 'cifar':
            return CifarDataProvider()


class CifarDataProvider:
    def __init__(self):
        self.dataset = None
        self.img_shape = (32,32,3)

    def download_dataset(self):
        from keras.datasets import cifar10
        (x_train, y_train), (x_test, y_test) = cifar10.load_data()
        x_train = x_train[y_train.flatten() == 3]
        x_test = x_test[y_test.flatten() == 3]
        self.dataset = np.concatenate((x_train, x_test))



class FolderDataProvider:
    def __init__(self, folder_path):
        self.files = list(os.listdir(folder_path))

    def get_random(self,idx):
        pass

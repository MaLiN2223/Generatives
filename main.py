import logging
from numpy.random import seed

seed(0)
from tensorflow import set_random_seed

set_random_seed(0)
import h5py
from training.DataProvider import DataProviderFactory
from keras.optimizers import Adam
from models.generators import vgg_generator
from models.discriminators import vgg_discriminator
from training import Trainer
from utils.Utils import save_imgs, prepare_directories
prepare_directories()

logging.basicConfig(filename='app.log', filemode='w', format='[%(asctime)s] %(message)s')
logging.info('Starting...')


SIZE = 32
channels = 3
img_shape = (SIZE, SIZE, channels)
latent_dim = 256

generator = vgg_generator(latent_dim, channels)
disc = vgg_discriminator(img_shape)

data_provider = DataProviderFactory.get_generator('cifar')

configuration = {
    'optimizer' : Adam(0.0002, 0.5),
    'discriminator' : disc,
    'generator' : generator,
    'latent_dim' : latent_dim,
    'data_provider':  data_provider
}
trainer = Trainer.from_configuration(configuration)
trainer.train(epochs=100001, batch_size=64, save_interval=25, interval_function=save_imgs, notebook_mode = True)

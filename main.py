import logging
from numpy.random import seed

seed(0)
from tensorflow import set_random_seed

set_random_seed(0)
import h5py

logging.basicConfig(filename='app.log', filemode='w', format='[%(asctime)s] %(message)s')

logging.info('Starting...')
from models.generators import mnist_generator
from models.discriminators import mnist_discriminator
from training import Trainer

SIZE = 64 
channels = 1
img_shape = (SIZE, SIZE, channels)
latent_dim = 2
dataset = h5py.File('data.hdf5', 'r')
data = dataset['ints'][:]
#data = data.reshape(-1, img_shape[0], img_shape[1], img_shape[2])
dataset.close()

generator = mnist_generator(latent_dim, channels)
disc = mnist_discriminator(img_shape)
trainer = Trainer(data, generator, disc, latent_dim, img_shape)
trainer.multithreaded = False
trainer.train(epochs=100001, batch_size=64, save_interval=25)

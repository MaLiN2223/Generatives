import numpy as np
import tensorflow as tf
from keras import backend as K
from keras.models import Model
from keras.layers import Input
from utils import Timer, Logger
import matplotlib.pyplot as plt

logger = Logger.get_logger()
stat_logger = logger.get_statistics_logger()
tf_session = K.get_session()  # this creates a new session since one doesn't exist already.
tf_graph = tf.get_default_graph()


class TrainingConfiguration:
    def __init__(self):
        self.config = {
            'optimizer' : Adam(0.0002, 0.5),
            'discriminator' : None,
            'generator' : None,
            'latent_dim' : 100,
            'data_provider':  None
        }

class Trainer:

    @staticmethod
    def from_configuration(configuration):
        trainer = Trainer()
        trainer.latent_dim = configuration['latent_dim']
        trainer.data_provider = configuration['data_provider']
        trainer.optimizer = configuration['optimizer']
        trainer.discriminator = configuration['discriminator']
        trainer.generator = configuration['generator']

        trainer.compile()
        return trainer

    def compile(self):
        if self.data_provider is None:
            raise Error('Data provider cannot be none')
        self.data_provider.download_dataset()
        self.data = self.data_provider.dataset
        self.img_shape = self.data_provider.img_shape

        self.discriminator.compile(loss='binary_crossentropy', optimizer=self.optimizer, metrics=['binary_accuracy'])
        self.discriminator.trainable = False

        z = Input(shape=(self.latent_dim,))
        img = self.generator(z)
        valid = self.discriminator(img)
        self.combined = Model(inputs=z, outputs=valid)
        self.combined.compile(loss='binary_crossentropy', optimizer=self.optimizer, metrics=['binary_accuracy'])

    def train(self, epochs, batch_size=128, save_interval=50, interval_function=None, notebook_mode=True):
        if notebook_mode:
            from tqdm import tqdm_notebook as tqdm
        else:
            from tqdm import tqdm

        X_train = self.data

        # Adversarial ground truths
        valid = np.ones((batch_size, 1))
        fake = np.zeros((batch_size, 1))

        timer = Timer()
        time_sum = 0
        print('Training starts')
        for epoch in tqdm(range(epochs)):
            timer.reset()
            # Select random images
            idx = np.mod(np.random.randint(0, X_train.shape[0], batch_size),1000)
            imgs = X_train[idx].reshape(-1,  self.img_shape[0],  self.img_shape[1],  self.img_shape[2])
            imgs = imgs.astype(np.float32) / 255.0 # scale 0 to 1

            noise = np.random.normal(0, 1, (batch_size, self.latent_dim))
            gen_imgs = self.generator.predict(noise)

            d_loss_real = self.discriminator.train_on_batch(imgs, valid)
            d_loss_fake = self.discriminator.train_on_batch(gen_imgs, fake)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
            g_loss = self.combined.train_on_batch(noise, valid)
            time = timer.get_elapsed_time()
            time_sum += time

            #stat_logger.info("%d [%f %.2f%%] [%f] [%f]" % (epoch, d_loss[0], 100 * d_loss[1], g_loss, time))
            if epoch % save_interval == 0:
                if interval_function is not None:
                    interval_function(self, epoch, self.latent_dim, notebook_mode)
                stat_logger.info('%.2f' % (time_sum))
                time_sum = 0

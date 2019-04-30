import numpy as np
import tensorflow as tf
from keras import backend as K
from keras.optimizers import Adam
from keras.models import Model
from keras.layers import Input

from utils import Timer, Logger
import matplotlib.pyplot as plt

logger = Logger.get_logger()
stat_logger = logger.get_statistics_logger()
tf_session = K.get_session()  # this creates a new session since one doesn't exist already.
tf_graph = tf.get_default_graph()


class Trainer:
    def __init__(self, data, generator, discriminator, latent_dim, img_shape):
        # Input shape
        self.img_shape = img_shape
        self.latent_dim = latent_dim
        self.data = data
        optimizer = Adam(0.0002, 0.5)

        self.discriminator = discriminator
        self.generator = generator
        with tf_session.as_default():
            with tf_graph.as_default():
                # Build and compile the discriminator
                self.discriminator.compile(loss='binary_crossentropy',
                                           optimizer=optimizer,
                                           metrics=['accuracy'])

                # The generator takes noise as input and generates imgs
                z = Input(shape=(self.latent_dim,))
                img = self.generator(z)

                # For the combined model we will only train the generator
                self.discriminator.trainable = False

                # The discriminator takes generated images as input and determines validity
                valid = self.discriminator(img)

                # The combined model  (stacked generator and discriminator)
                # Trains the generator to fool the discriminator
                self.combined = Model(z, valid)
                self.combined.compile(loss='binary_crossentropy', optimizer=optimizer)

    def train(self, epochs, batch_size=128, save_interval=50):
        X_train = self.data

        # Adversarial ground truths
        valid = np.ones((batch_size, 1))
        fake = np.zeros((batch_size, 1))

        timer = Timer()
        time_sum = 0
        print('Training starts')
        for epoch in range(epochs):
            timer.reset()
            # Select a random half of images
            idx = np.random.randint(0, X_train.shape[0], batch_size)
            imgs = X_train[idx].reshape(-1,  self.img_shape[0],  self.img_shape[1],  self.img_shape[2]) 
            imgs = imgs / 127.5 - 1.
            # Sample noise and generate a batch of new images
            noise = np.random.normal(0, 1, (batch_size, self.latent_dim))
            gen_imgs = self.generator.predict(noise)

            # Train the discriminator (real classified as ones and generated as zeros)
            d_loss_real = self.discriminator.train_on_batch(imgs, valid)
            d_loss_fake = self.discriminator.train_on_batch(gen_imgs, fake)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            # ---------------------
            #  Train Generator
            # ---------------------

            # Train the generator (wants discriminator to mistake images as real)
            g_loss = self.combined.train_on_batch(noise, valid)
            time = timer.get_elapsed_time()
            time_sum += time
            # Plot the progress
            stat_logger.info("%d [%f %.2f%%] [%f] [%f]" % (epoch, d_loss[0], 100 * d_loss[1], g_loss, time))
            # If at save interval => save generated image samples
            if epoch % save_interval == 0:
                self.save_imgs(epoch)
                stat_logger.info('%.2f' % (time_sum))
                time_sum = 0

    def save_imgs(self, epoch):
        r, c = 5, 5
        noise = np.random.normal(0, 1, (r * c, self.latent_dim))
        gen_imgs = self.generator.predict(noise)

        # Rescale images 0 - 1
        gen_imgs = 0.5 * gen_imgs + 0.5

        fig, axs = plt.subplots(r, c)
        cnt = 0
        for i in range(r):
            for j in range(c):
                axs[i, j].imshow(gen_imgs[cnt, :,:,0], cmap='gray')
                axs[i, j].axis('off')
                cnt += 1
        fig.savefig("outputs/output_%d.png" % epoch)
        plt.close()
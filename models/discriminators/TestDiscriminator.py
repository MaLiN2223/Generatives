from keras.models import Sequential, Model
from keras.layers import Dense, Input, Activation, BatchNormalization, Conv2D, Reshape
from keras.layers import UpSampling2D, LeakyReLU, Flatten
from utils.Logger import Logger
from keras import initializers
logger = Logger.get_logger()

def test_discriminator(img_shape):
    # imagem shape 32x32x3
    init = initializers.RandomNormal(stddev=0.02)

    # Discriminator network
    discriminator = Sequential()

    # Conv 1: 16x16x64
    discriminator.add(Conv2D(64, kernel_size=5, strides=2, padding='same',
                             input_shape=(img_shape), kernel_initializer=init))
    discriminator.add(LeakyReLU(0.2))

    # Conv 2:
    discriminator.add(Conv2D(128, kernel_size=5, strides=2, padding='same'))
    discriminator.add(BatchNormalization())
    discriminator.add(LeakyReLU(0.2))

    # Conv 3:
    discriminator.add(Conv2D(256, kernel_size=5, strides=2, padding='same'))
    discriminator.add(BatchNormalization())
    discriminator.add(LeakyReLU(0.2))

    # Conv 3:
    discriminator.add(Conv2D(512, kernel_size=5, strides=2, padding='same'))
    discriminator.add(BatchNormalization())
    discriminator.add(LeakyReLU(0.2))

    # FC
    discriminator.add(Flatten())

    # Output
    discriminator.add(Dense(1, activation='sigmoid'))
    return discriminator

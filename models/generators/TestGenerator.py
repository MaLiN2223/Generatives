from keras.models import Sequential, Model
from keras.layers import Dense, Input, Activation, BatchNormalization, Conv2D, Reshape
from keras.layers import UpSampling2D, LeakyReLU, Conv2DTranspose
from utils.Logger import Logger
from keras import initializers
logger = Logger.get_logger()

def test_generator(latent_dim, channels):
    init = initializers.RandomNormal(stddev=0.02)

    # Generator network
    generator = Sequential()

    # FC: 2x2x512
    generator.add(Dense(2*2*512, input_shape=(latent_dim,), kernel_initializer=init))
    generator.add(Reshape((2, 2, 512)))
    generator.add(BatchNormalization())
    generator.add(LeakyReLU(0.2))

    # # Conv 1: 4x4x256
    generator.add(Conv2DTranspose(256, kernel_size=5, strides=2, padding='same'))
    generator.add(BatchNormalization())
    generator.add(LeakyReLU(0.2))

    # Conv 2: 8x8x128
    generator.add(Conv2DTranspose(128, kernel_size=5, strides=2, padding='same'))
    generator.add(BatchNormalization())
    generator.add(LeakyReLU(0.2))

    # Conv 3: 16x16x64
    generator.add(Conv2DTranspose(64, kernel_size=5, strides=2, padding='same'))
    generator.add(BatchNormalization())
    generator.add(LeakyReLU(0.2))

    # Conv 4: 32x32x3
    generator.add(Conv2DTranspose(3, kernel_size=5, strides=2, padding='same',
                                  activation='tanh'))
    return generator

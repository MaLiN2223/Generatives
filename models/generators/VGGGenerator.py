from keras.models import Sequential, Model
from keras.layers import Dense, Input, Activation, BatchNormalization, Conv2D, Reshape
from keras.layers import UpSampling2D
from utils.Logger import Logger
logger = Logger.get_logger()


def vgg_generator(latent_dim, channels): 
    model = Sequential()
    depth = 8
    model.add(Dense(128 * depth * depth, activation="relu", input_dim=latent_dim))
    model.add(Reshape((depth, depth, 128)))
    model.add(UpSampling2D())
    model.add(Conv2D(128, kernel_size=3, padding="same"))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Activation("relu"))
    model.add(UpSampling2D())
    model.add(Conv2D(64, kernel_size=3, padding="same"))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Activation("relu"))
    model.add(Conv2D(32, kernel_size=3, padding="same"))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Activation("relu"))
    model.add(Conv2D(channels, kernel_size=3, padding="same"))
    model.add(Activation("tanh"))

    model.summary()

    noise = Input(shape=(latent_dim,))
    img = model(noise)
    model.summary(print_fn=logger.info)

    return Model(noise, img)

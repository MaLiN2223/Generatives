from keras.models import Sequential, Model
from keras.layers import Dense, Input,  BatchNormalization, Conv2D,Flatten, LeakyReLU, Dropout

from keras.layers import ZeroPadding2D
from keras.applications.vgg19 import VGG19
from utils.Logger import Logger
logger = Logger.get_logger()

def vgg_discriminator(img_shape, train_vgg = False): 
    model = VGG19(weights='imagenet',include_top=False,input_shape=img_shape)
    top_model = Sequential()
    top_model.add(BatchNormalization(momentum=0.8))
    top_model.add(LeakyReLU(alpha=0.2))
    top_model.add(Dropout(0.25))
    top_model.add(Flatten())
    top_model.add(Dense(1, activation='sigmoid'))
    model = Model(inputs= model.input, outputs= top_model(model.output))
    model.summary()

    if not train_vgg:
        for layer in model.layers[:-6]:
            layer.trainable = False
    return model

from keras.models import Sequential, Model
from keras.layers import Dense, Input,  BatchNormalization, Conv2D,Flatten, LeakyReLU, Dropout

from keras.layers import ZeroPadding2D
from keras.applications.vgg16 import VGG16
logger = Logger.get_logger()

def discriminator(img_shape, train_vgg = False):
    model = VGG19(weights="imagenet",include_top=False,input_shape=(128,128,3))
    model.layers[-1].outbound_nodes = []
    model.outputs = [model.layers[-1].output]
    x = model.layers[-1].output
    x = BatchNormalization(momentum=0.8)(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Dropout(0.25)(x)
    x = Flatten()(x)
    x = Dense(1, activation='sigmoid')(x)
    a = Model(model.input, x)
    a.summary()
    if not train_vgg:
        for layer in a.layers[:-6]:
            layer.trainable = False
    return model

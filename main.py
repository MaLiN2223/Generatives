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

def save_imgs(self, epoch):
    r, c = 2, 2
    noise = np.random.normal(0, 1, (r * c, latent_dim))
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
    fig.savefig(f"outputs/output_{str(epoch).zfill(5)}.png")
    plt.close()

generator = mnist_generator(latent_dim, channels)
disc = mnist_discriminator(img_shape)
trainer = Trainer(data, generator, disc, latent_dim, img_shape)
trainer.multithreaded = False
trainer.train(epochs=100001, batch_size=64, save_interval=25, interval_function=save_imgs)

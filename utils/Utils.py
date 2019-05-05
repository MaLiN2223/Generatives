import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def save_imgs(self, epoch, latent_dim=None, notebook_mode = True):
    if latent_dim is None:
        raise Error('Latent dim cannot be None')
    r, c = 2, 2
    noise = np.random.normal(0, 1, (r * c, latent_dim))
    gen_imgs = self.generator.predict(noise)

    #Rescale images 0 - 1
    gen_imgs = gen_imgs*255
    fig, axs = plt.subplots(r, c)
    cnt = 0
    for i in range(r):
        for j in range(c):
            axs[i, j].imshow(gen_imgs[cnt].astype(np.uint8))
            axs[i, j].axis('off')
            cnt += 1
    group = f"outputs/output_{str(epoch).zfill(5)}.png"
    fig.savefig(group)
    plt.close()
    img = Image.fromarray(gen_imgs[0],'RGB')
    single = f"outputs_single/image_{str(epoch).zfill(5)}.png"
    img.save(single)


def prepare_directories():

    if not os.path.exists('logs'):
        os.mkdir('logs')
    if not os.path.exists('outputs'):
        os.mkdir('outputs')
    if not os.path.exists('outputs_single'):
        os.mkdir('outputs_single')

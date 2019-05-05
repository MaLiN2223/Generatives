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
    # Rescale images 0 - 1
    gen_imgs = 0.5 * gen_imgs + 0.5

    fig, axs = plt.subplots(r, c)
    cnt = 0
    for i in range(r):
        for j in range(c):
            axs[i, j].imshow(gen_imgs[cnt, :,:,0], cmap='gray')
            axs[i, j].axis('off')
            cnt += 1
    group = f"outputs/output_{str(epoch).zfill(5)}.png"
    fig.savefig(group)
    plt.close()
    img = Image.fromarray(gen_imgs[0,:,:,0]*255).convert("L")
    single = f"outputs_single/image_{str(epoch).zfill(5)}.png"
    img.save(single)
    print('sadsads')
    if notebook_mode and epoch % 500 == 0:
      from GooglenotebookUtils import upload_to_gdrive
      upload_to_gdrive()


def prepare_directories():

    if not os.path.exists('logs'):
        os.mkdir('logs')
    if not os.path.exists('outputs'):
        os.mkdir('outputs')
    if not os.path.exists('outputs_single'):
        os.mkdir('outputs_single')

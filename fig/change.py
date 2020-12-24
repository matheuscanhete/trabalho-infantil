import numpy as np
from PIL import Image

img = Image.open("logouf.png")
vetor = np.array(img)

vetor[vetor != 0] = 255

img = Image.fromarray(vetor)
img.save("logouf.png")

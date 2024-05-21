import sys
import numpy as np
from PIL import Image
from pathlib import Path

RESULT_PATH = 'test_2.txt'

im = Image.open(sys.argv[1]).convert('RGB')

newsize = (16, 16)
im1 = im.resize(newsize)

data = np.array(im1)

for i, line in enumerate(data):
    if i % 2 != 0:
        line[:] = line [::-1]
    # for j in line:
    #     print(j, end=" ")
    # print("\n")
with open(RESULT_PATH, 'w') as file:
    file.write("[")
    for row in data:
        for pixel in row:
            file.write("[")
            file.write(str(pixel[0])+", "+str(pixel[1])+", "+str(pixel[2]))
            file.write("],")
    file.write("]")
im1 = Image.fromarray(data) 
im1.save(Path(sys.argv[1]).stem + "_converted.bmp")
# im1.show()

import numpy as np


if __name__ =='__main__':
    f = open('mnist/t10k-images.idx3-ubyte','rb')
    magicnum = ord(f.read(4))
    print(magicnum)
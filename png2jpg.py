import cv2
import os,sys
def png2jpg(src,dst):
    lst = os.listdir(src)
    for e in lst:
        if e.endswith('.png'):
            img = cv2.imread(os.path.join(src,e),1)
            cv2.imwrite(os.path.join(dst,e[:-3]+'jpg'),img)

if __name__ == '__main__':
    png2jpg('618_GAN1/samples','618_GAN1')
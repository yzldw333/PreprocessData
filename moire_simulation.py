import cv2
import numpy as np
if __name__ == '__main__':
    img = np.ones([500,500,3],np.uint8)
    img = cv2.imread(r'E:\code\PreprocessData\data_v7_update\618_mnist_hardmine_class0\227.jpg',1)
    newimg = np.zeros([500,500,3],np.uint8)
    alpha = 0.6 # lens pitch
    p = 1 # pixel pitch
    rotate = 0
    minx=500
    miny=500
    maxx=0
    maxy=0
    for n in range(500):
        for m in range(500):
            nn = alpha*n*1.0/p
            mm = alpha*m*1.0/p
            rotate_matrix = np.array([[np.cos(rotate),-np.sin(rotate)],[np.sin(rotate),np.cos(rotate)]])
            mm-=128
            nn-=128
            d = np.array([[mm],[nn]])
            d = np.dot(rotate_matrix,d)
            dnn = nn-int(nn)
            d = d.ravel()
            mm = d[0]+128
            nn = d[1]+128
            if nn<256and nn>=0 and mm<256 and mm>=0:
                #newimg[m,n,:] = img[int(mm),int(nn),:]
                newimg[m,n,int(dnn*3)] = img[int(mm),int(nn),int(dnn*3)]
                if m<miny:
                    miny=m
                if m>maxy:
                    maxy=m
                if n<minx:
                    minx=n
                if n>minx:
                    maxx=n
    newimg = newimg[miny:maxy+1,minx:maxx+1,:]
    newimg = cv2.resize(newimg,(256,256))

    cv2.imshow('src',img)
    cv2.imshow('t',newimg)
    cv2.waitKey()

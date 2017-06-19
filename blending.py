import os
import cv2
import numpy as np


if __name__ == '__main__':
    imgroot = r'E:\data\618data\0516_618video\src'
    imglst = os.listdir(imgroot)
    bgroot = r'E:\code\PreprocessData\618_data_v5\data\query_img_class2'
    bglst = os.listdir(bgroot)
    outdir = r'E:\data\618data\0516_618video\src\blending'
    if os.path.exists(outdir)==False:
        os.mkdir(outdir)
    index = 0
    for e in imglst:
        a = cv2.imread(os.path.join(imgroot,e))
        try:
            b = cv2.imread(os.path.join(bgroot,bglst[np.random.randint(len(bglst))]),1)
            width = int((np.random.rand()*0.5+0.5)*a.shape[1])
            height = int((np.random.rand()*0.5+0.5)*a.shape[0])
            startx = np.random.randint(0,a.shape[1]-width)
            starty = np.random.randint(0,a.shape[0]-height)
            b = b[starty:starty+height,startx:startx+width,:]
            b = cv2.resize(b,(256,256))
        except Exception as e:
            continue
        a = cv2.resize(a,(256,256))
        alpha = np.random.randint(40,60)/100.0
        c = cv2.addWeighted(a, alpha, b, np.random.randint(40,int((1-alpha)*100))/100.0, np.random.randint(-20,20))
        outpath = os.path.join(outdir,str(index)+'.jpg')
        while os.path.exists(outpath):
            index+=1
            outpath = os.path.join(outpath,str(index)+'.jpg')
        cv2.imwrite(outpath,c)
        index+=1
        #cv2.imshow('t', c)
        #cv2.waitKey()

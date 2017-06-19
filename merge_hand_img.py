import cv2
import os
import numpy as np
mnistroot = r'E:\data\618data\mnist\new'

lst = os.listdir(os.path.join(mnistroot,'ori_images'))
map_0 = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for e in lst:
    map_0[int(e[0])]+=1

lst = os.listdir(os.path.join(mnistroot,'ori_images_64'))
map_64 = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for e in lst:
    map_64[int(e[0])]+=1

lst = os.listdir(os.path.join(mnistroot,'ori_images_128'))
map_128 = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for e in lst:
    map_128[int(e[0])]+=1

_map=[map_0,map_64,map_128]

def generateNum(num):
    type = np.random.randint(0,3)
    if type==0:
        baseroot= r'E:\data\618data\mnist\new\ori_images'
    if type==1:
        baseroot = r'E:\data\618data\mnist\new\ori_images_64'
    if type==2:
        baseroot = r'E:\data\618data\mnist\new\ori_images_128'
    name = str(num)+'_'+str(np.random.randint(0,_map[type][num]))+'.png'
    img = cv2.imread(os.path.join(baseroot,name))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('test',img)
    #cv2.waitKey()
    srcimg = img
    cols = np.max(img,0)
    left = 0
    right = 320
    for i in range(320):
        if cols[i]>0:
            left=i
            break
    for i in range(319,0,-1):
        if cols[i]>0:
            right=i
            break
    print(left,right)
    img = srcimg[:,left:right]
    size = right-left
    #cv2.imshow('test', img)
    #cv2.waitKey()
    return (img,size)

if __name__ == '__main__':
    generateroot = 'mnist_hand'
    for i in range(11000):
        img6,size6 = generateNum(6)
        img1,size1 = generateNum(1)
        img8,size8 = generateNum(8)
        sep1 = int(size1/4.0)
        sep8 = int(size8/4.0)
        totalsize = size6+sep1+size1+sep8+size8
        newimg = np.zeros([320,totalsize],np.uint8)
        newimg[:,:size6]=img6
        newimg[:,size6+sep1:size6+sep1+size1]=img1
        newimg[:,size6+sep1+size1+sep8:size6+sep1+size1+sep8+size8]=img8
        newimg = cv2.cvtColor(newimg,cv2.COLOR_GRAY2BGRA)
        newimg[newimg[:, :, 0] == 0, 3] = 0
        newimg[newimg[:, :, 0] > 0, 0] = np.random.randint(0,255)
        newimg[newimg[:, :, 1] > 0, 1] = np.random.randint(0, 255)
        newimg[newimg[:, :, 2] > 0, 2] = np.random.randint(0, 255)
        outpath = os.path.join(generateroot,str(i)+'.png')
        cv2.imwrite(outpath,newimg)
        # cv2.imshow('test',newimg)
        # cv2.waitKey()







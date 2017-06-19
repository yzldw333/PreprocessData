import cv2
import numpy as np
import os,sys
def random_sample(img):
    sp = img.shape
    width = int(np.random.rand()*sp[1]/2)
    height = int(np.random.rand()*sp[0]/2)
    left = int(np.random.rand()*(sp[1]-width-1))
    top = int(np.random.rand()*(sp[0]-height-1))
    img = img[top:top+height,left:left+width,:]
    return img

def merge(img,bg,center_size,output_size):
    img = cv2.resize(img,center_size,interpolation=cv2.INTER_AREA)
    radius = int(np.sqrt(((img.shape[0] / 2.0) ** 2 + (img.shape[1] / 2.0) ** 2)))
    new_img = np.zeros([radius * 2, radius * 2, 4], np.uint8)
    new_img[radius - img.shape[0] / 2:radius - img.shape[0] / 2 + img.shape[0],
    radius - img.shape[1] / 2:radius - img.shape[1] / 2 + img.shape[1], :] = img
    M = cv2.getRotationMatrix2D((radius, radius), np.random.randint(-50, 50), 1)
    tst_img = cv2.warpAffine(new_img, M, (radius * 2, radius * 2))
    img = tst_img
    # cv2.imshow('t',tst_img)
    # cv2.waitKey()
    if np.random.rand() < 0.5:
        bg = cv2.resize(bg, (output_size[0], int(output_size[1] * (np.random.rand() * 2 + 1))),
                        interpolation=cv2.INTER_AREA)
        y = bg.shape[0]
        bg = bg[(y - output_size[1]) / 2:(y + output_size[1] / 2), :, :]
    else:
        bg = cv2.resize(bg, (int(output_size[0] * (np.random.rand() * 2 + 1)), output_size[1]),
                        interpolation=cv2.INTER_AREA)
        y = bg.shape[1]
        bg = bg[:, (y - output_size[0]) / 2:(y + output_size[0]) / 2, :]
    bg = cv2.resize(bg,output_size,interpolation=cv2.INTER_AREA)

    h_bg,w_bg,c_bg = bg.shape
    h_img,w_img,c_img = img.shape

    left = int(np.random.rand()*(w_bg-w_img-30))+15
    top = int(np.random.rand()*(h_bg-h_img-30))+15
    for i in range(h_img):
        for j in range(w_img):
            a = top+i
            b = left+j
            if a>=output_size[0] or b>=output_size[1]:
                continue
            if img[i,j,-1] != 0:
                bg[a,b,:] = img[i,j,:-1]*(img[i,j,-1]/255.0)
    return bg

def read_merge(imgpath,bgpath,des_size):
    img = cv2.imread(imgpath,-1)
    bg = cv2.imread(bgpath,1)
    bg = random_sample(bg)
    height = np.random.randint(int(des_size*0.15), int(des_size*0.37))
    width = int((np.random.rand()*2 + 0.8) * height)
    if width > des_size:
        width = des_size
    output = merge(img, bg, (width, height), (des_size, des_size))
    return output
if __name__ == '__main__':
    #if len(sys.argv)!=5:
    #    print('Please enter like this: python merge_neg.py pngDir bgimgDir outputDir dstSize')
    #    sys.exit(0)
    # imgDir = sys.argv[1]
    # bgDir = sys.argv[2]
    # outputDir = sys.argv[3]
    # dst_size = int(sys.argv[4])

    imgDir = r'neg_img'
    bgDir = 'mix_bg'
    outputDir = r'freetype_small_scale/618non_freetype_ss_class1'
    dst_size=256
    imglst = os.listdir(imgDir)
    bglst = os.listdir(bgDir)
    hasbg = np.zeros([len(bglst)],dtype=int)
    generated = 0 
    if os.path.exists(outputDir)==False:
        os.mkdir(outputDir)
    for e in imglst:
        imgpath = os.path.join(imgDir,e)
        p = False
        while(p==False):
            try:
                bgindex = int(np.random.rand() * len(bglst))
                bgpath = os.path.join(bgDir,bglst[bgindex])
                out = read_merge(imgpath,bgpath,dst_size)
                p = True
            except Exception as err:
                print(bgpath+" error!")
        outDir = os.path.join(outputDir,str(generated)+'.jpg')
        cv2.imwrite(outDir,out)
        generated = generated+1
        print(generated)
        #only bg
        # p=False
        # while (p == False):
        #     try:
        #         bgindex = int(np.random.rand() * len(bglst))
        #         # if(hasbg[bgindex]==1):
        #         #     continue
        #         bgpath = os.path.join(bgDir, bglst[bgindex])
        #         bg = cv2.imread(bgpath)
        #         bg = random_sample(bg)
        #         out = cv2.resize(bg, (dst_size,dst_size), interpolation=cv2.INTER_AREA)
        #         p = True
        #         hasbg[bgindex]=1
        #     except Exception as err:
        #         print(bgpath + " error!")
        #outDir = os.path.join(outputDir,str(generated) + '.jpg')
        #cv2.imwrite(outDir, out)
        #generated = generated + 1


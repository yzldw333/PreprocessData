import cv2
import os,sys
import numpy as np

def Resize_Move(src_dir,dst_dir,dstSize):
    srclst = os.listdir(src_dir)
    index = 0
    if os.path.exists(dst_dir) == False:
        os.mkdir(dst_dir)
    for f in srclst:
        path = os.path.join(src_dir,f)
        if os.path.isdir(path) == False:
            try:
                img = cv2.imdecode(np.fromfile(path, dtype=np.uint8),1)
            except Exception as e:
                print(path+' error')
                continue
            #img = cv2.imread(path)
            if img is not None:
                print(img.shape)
                rate0 = img.shape[0]*1.0 /img.shape[1]
                rate1 = img.shape[1]*1.0 /img.shape[0]
                #if rate0>=2 or rate1>=2:
                #    continue
                sp = img.shape
                img = cv2.resize(img, (dstSize,int(dstSize * 1.0 / sp[1] * sp[0])), cv2.INTER_AREA)
                out_path = os.path.join(dst_dir, str(index) + '.jpg')
                while os.path.exists(out_path):
                    index += 1
                    out_path = os.path.join(dst_dir, str(index) + '.jpg')
                #img = cv2.resize(img,(dstSize,dstSize),interpolation=cv2.INTER_AREA)
                cv2.imwrite(out_path,img)
                index+=1

def rotate(path):
    img = cv2.imread(path)
    rows, cols,channels = img.shape

    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 1.1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('1',dst)
    cv2.waitKey()

if __name__ == '__main__':
    #Resize_Move(sys.argv[1],sys.argv[2],sys.argv[3])
    # root = 'advertisement_query'
    # lst = os.listdir(root)
    # for e in lst:
    #     if os.path.isdir(os.path.join(root,e)):
    #         Resize_Move(os.path.join(root,e),'advertisement_query_class2',480)
    #     print(e+' Done!')
    Resize_Move(r'E:\data\618data\0608video\extract_frames',r'E:\code\PreprocessData\data_v7_update\618_photo_2_class0',480)
    #rotate(r'E:\code\PreprocessData\618_data_v5\data\618_freetype_class0\0.jpg')
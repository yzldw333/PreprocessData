import os
import json
import cv2
import urllib

if __name__ == '__main__':
    outdir = 'E:/code/618/0517'
    if os.path.exists(outdir)==False:
        os.mkdir(outdir)
    flabel = open(r'E:\code\PreprocessData\bdpcv_236_20170517.txt')
    labellst = [json.loads(line) for line in flabel]
    length = len(labellst)
    for i in range(length):
        try:
            label = labellst[i][0]
            label = json.loads(label)
        except Exception as e:
            continue
        x1 = int(label['x'])
        y1 = int(label['y'])
        imgname = label['imgName']
        width = int(label['width'])
        height = int(label['height'])
        urlpath = 'https://img12.360buyimg.com/img/'+imgname
        name = imgname.split('/')[-1]
        downloadpath = os.path.join(outdir,name)
        urllib.urlretrieve(urlpath,downloadpath)
        x2 = x1+width
        y2 = y1+height
        img = cv2.imread(downloadpath,1)
        img = cv2.resize(img,(600,600))
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),3)
        print(img.shape)
        cv2.imshow('t',img)
        cv2.waitKey()
        newpath = os.path.join(outdir,'new_'+name)
        #cv2.imwrite(newpath,img)


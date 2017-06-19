import os
import json
import cv2

if __name__ == '__main__':
    outdir = 'E:/code/618/618logo2'
    index = 0
    imgroot = r'E:\code\618\618logoraw'
    #fimg = open(r'E:\code\618\618logoraw\618_object.txt')
    flabel = open(r'E:\code\618\618logoraw\bdpcv_221_20170511.txt')
    #print(fimg.readline())
    #jlst = [json.loads(line) for line in fimg]
    labellst = [json.loads(line) for line in flabel]
    length = len(labellst)
    for i in range(length):
        #print(jlst[i][u'imageName'])
        #print(labellst[i][0])
        try:
            label = labellst[i][0]
        except Exception as e:
            continue
        x1 = int(label['x'])
        y1 = int(label['y'])
        imgname = label['\"imgName\"']
        width = int(label['width'])
        height = int(label['height'])
        x2 = x1+width
        y2 = y1+height

        ratio = (x2-x1)*1.0/(y2-y1)

        #level1
        expand_y = (y2-y1)*1.8
        expand_x = (y2-y1)*1.8
        x1 = int(x1-expand_x)
        x2 = int(x2+expand_x)
        y1 = int(y1-expand_y)
        y2 = int(y2+expand_y)

        imgpath = os.path.join(imgroot,imgname)
        img = cv2.imread(imgpath,1)
        if x1<0:
            x1=0
        if y1<0:
            y1=0
        if x2>img.shape[1]:
            x2 = img.shape[1]
        if y2>img.shape[0]:
            y2 = img.shape[0]
        img = img[y1:y2,x1:x2,:]
        outpath = outdir+'/'+str(index)+'.jpg'
        while os.path.exists(outpath):
            index+=1
            outpath = outdir + '/' + str(index) + '.jpg'
        cv2.imwrite(outpath,img)
        index+=1



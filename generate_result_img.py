import os
import cv2
if __name__ == '__main__':
    imgroot = 'E:/code/618/618_res50_eval/test-img/badcase'
    result = 'E:/code/618/618_res50_eval/test-img/badcase_result.txt'
    lst = open(result)
    for e in lst:
        imgname = e.split()[0]
        label = e.split()[1]
        src = imgroot+'/'+imgname



        des = imgroot+'/'+label+'_'+imgname

        img = cv2.imread(des, -1)
        img = cv2.resize(img, (300,int(300.0/img.shape[1]*img.shape[0])))
        cv2.imshow('t', img)
        cv2.waitKey()

        cmd = 'mv \"%s\" \"%s\"'%(src,des)
        os.system(cmd)
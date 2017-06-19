import os,sys

if __name__=='__main__':
    f = open('val_shuf.txt','r')
    fw = open('photo_val_shuf.txt','w')
    for line in f:
        if 'photo' in line:
            fw.write(line)
    fw.close()
import os
import csv

if __name__ == '__main__':
    imgroot = r'E:\code\618\fengce\fengceimg'
    csvfile = r'E:\code\618\fengce\log.csv'
    fw = open(csvfile,'wb')
    writer = csv.writer(fw)
    lst = os.listdir(imgroot)
    writer.writerow(['Log1','Log2','predict label','true label'])
    for e in lst:
        f = open(r'E:\code\618\fengce\618sao-log.txt')
        logstr1 = None
        logstr2 = None
        label = None
        for line in f:
            if line.find(e[2:])!=-1 and line.find('main.cpp')!=-1:
                logstr1 = line
            if line.find(e[2:])!=-1 and line.find('recognize_handler')!= -1:
                label = line.split(' ')[-2]
                logstr2 = line
            if label is not None and logstr1 is not None and logstr2 is not None:
                break
        if label is not None and logstr1 is not None and logstr2 is not None:
            writer.writerow([logstr1,logstr2,label,e[2:]])
    fw.close()

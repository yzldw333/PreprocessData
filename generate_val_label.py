import os,sys

if __name__ == '__main__':
    root = r'E:\code\618\618_res50_eval\Evaluation-Set'
    #f = open(os.path.join(root,'all_eval.txt'),'w')
    lst = os.listdir(root)
    for d in lst:
        subpath = os.path.join(root, d)
        if os.path.isdir(subpath):
            label = 0
            if d.endswith('0'):
                label=0
            if d.endswith('1'):
                label=1
            if d.endswith('2'):
                label=2
            if d.endswith('3'):
                label=3
            sublst = os.listdir(subpath)
            f = open(os.path.join(root,d+'.txt'),'w')
            for e in sublst:
                imgpath = d+'/'+e
                f.write(imgpath+' '+str(label)+'\n')
    f.close()

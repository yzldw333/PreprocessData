import os
import random
if __name__ == "__main__":
    imgroot = r'E:\code\618\online_log_norect\non618\false'
    outputdir = r'E:\code\618\fengce\false_non618'
    lst = os.listdir(imgroot)
    lst = random.sample(lst,int(30*(0.02802)))
    for e in lst:
        srcpath = os.path.join(imgroot,e)
        outpath = os.path.join(outputdir,e)
        cmd = "copy "+srcpath+" "+outpath
        os.system(cmd)

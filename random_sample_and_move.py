import random
import os
if __name__ == '__main__':
    pathlst = []
    lst = os.listdir(r'E:\code\PreprocessData\618_data_v4\data\query_img_class2')
    for e in lst:
        pathlst.append(os.path.join(r'E:\code\PreprocessData\618_data_v4\data\query_img_class2',e))
    samples = random.sample(pathlst,700)
    index = 0
    dstdir = r'E:\data\618data\618_evaluation_data\query'
    for e in samples:
        cmd = 'mv \"'+ e + '\" \"'+os.path.join(dstdir,str(index)+'.jpg')+'\"'
        os.system(cmd)
        index+=1


import os,sys
import random
import platform

def sample_img(dire,outlist=[]):
    lst = os.listdir(dire)
    for e in lst:
        path = os.path.join(dire,e)
        if os.path.isdir(path):
            sample_img(path,outlist)
        else:
            if path.endswith('jpg') or path.endswith('png'):
                outlist.append(path)

if __name__=='__main__':
    sysstr = platform.system()
    if len(sys.argv) != 4:
        print('Please enter like this: python random_sample_img_in_dir.py gen_dir out_dir total_num\n \
              gen_dir: source directory.\n \
              out_dir: output directory.\n \
              total_num: number of samples')
    gen_dir = sys.argv[1]
    out_dir = sys.argv[2]
    sample_num = int(sys.argv[3])
    outlist = []
    sample_img(gen_dir,outlist)
    length = len(outlist)
    print(length)
    if length<sample_num:
        print('Img insufficient(img num < sample num)')
    outlist = random.shuffle(outlist)
    outlist = outlist[:sample_num]
    for path in outlist:
        fileName = None
        if path.find('\\')!=-1:
            fileName = path.split('\\')[-1]
        if path.find('/')!=-1:
            fileName = path.split('/')[-1]
        if os.path.exists(out_dir)==False:
            os.mkdir(out_dir)
        dst_path = os.path.join(out_dir,fileName)
        if sysstr == 'Windows':
            cmd = "copy \""+path+"\" \""+dst_path+"\""
        elif sysstr == 'Linux':
            cmd = "cp \"" + path + "\" \"" + dst_path + "\""
        os.system(cmd)
    print('Done!')

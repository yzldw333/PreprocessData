import os
import sys
import random
def generateLabel(dataroot,_dir_label_map,outfile_path,random_shuf=False):
    ll = []
    for key in _dir_label_map:
        lst = os.listdir(os.path.join(dataroot,key))
        for c in lst:
            path = key+'/'+c
            if path.endswith('.jpg') or path.endswith('.bmp'):
                ll.append('%s %d\n'%(path,_dir_label_map[key]))
    random.shuffle(ll)
    f = open(outfile_path,'w')
    for e in ll:
        f.write(e)
    f.close()

if __name__ == '__main__':
    generateLabel('data_v7_update',{'618_photo_class0':0},'618_photo_class0.txt')
    generateLabel('data_v7_update',{'non618_photo_class1': 1}, 'non618_photo_class1.txt')
    generateLabel('data_v7_update', {'618_photo_2_class0': 0}, '618_photo_2_class0.txt')
    generateLabel('data_v7_update', {'non618_photo_2_class1': 1}, 'non618_photo_2_class1.txt')
    generateLabel('data_v7_update',{'advertisement_query_class2': 2}, 'advertisement_query_class2.txt')
    generateLabel('data_v7_update',{'hardnegative_query_class2': 2}, 'hardnegative_query_class2.txt')
    generateLabel('618_data_v5/data', {'query_img_class2': 2}, 'query_img_class2.txt')
    generateLabel('data_v7_update',{'618_mnist_hardmine_class0':0},'618_mnist_hardmine_class0.txt')
    generateLabel('data_v7_update', {'non618_mnist_hardmine_class1': 1}, 'non618_mnist_hardmine_class1.txt')
    generateLabel('data_v7_update', {'hardnegative_query_2_class2': 2}, 'hardnegative_query_2_class2.txt')
    generateLabel('data_v7_update', {'hardnegative_query_3_class2': 2}, 'hardnegative_query_3_class2.txt')


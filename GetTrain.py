import os,sys
import string


def load(imageinfo='val.txt',filename='',val_number=0,train_number=25000,min_number=25000):
    
    fread = open(imageinfo)
    indexset={}
    fw = open('gen_train'+filename+'.txt','w')
    fw_val = open('gen_val'+filename+'.txt','w')
    idx2images={}
    idx2num={}
    count = 0
    for line in fread:
        vec = line.strip().split()
        if len(vec) != 2:
            continue
        sku = vec[0]
        count += 1
        img = vec[0]+" "+str(count)
        idx = int(vec[1])
        result = "%s %d\n"%(sku,idx)
        if idx not in idx2num:
            idx2num[idx] = 1
        else:
            idx2num[idx] += 1
        if idx2num[idx] <= val_number:
            fw_val.write(result) 
            continue
        if idx in idx2images:
            images = idx2images[idx]
            images[img]=result
            idx2images[idx] = images
        else:
            images={}
            images[img] = result
            idx2images[idx]=images
    for idx in idx2images:
        count = 0
        images = idx2images[idx]
        while(count < min_number - val_number):
            for sku in images:
                result = images[sku]
                count += 1
                if count > train_number - val_number:
                    break
                fw.write(result)
def main():
    # photo_lst = os.listdir('618_photo_class0')
    # f = open('618_photo_class0.txt','w')
    # for e in photo_lst:
    #     f.write('618_photo_class0/'+e+' '+'0'+'\n')
    # f.close()
    # load('hardnegative_query_class2.txt','_hard_query_class2',0,450000,450000)
    # load('non618_photo_class1.txt','_non618_photo_class1',0,400000,400000)
    # load('618_photo_class0.txt', '_618_photo_class0',0,400000,400000)
    #
    # load('non618_photo_2_class1.txt', '_non618_photo_2_class1', 0, 100000, 100000)
    # load('618_photo_2_class0.txt', '_618_photo_2_class0', 0, 100000, 100000)
    #
    # load('advertisement_query_class2.txt', '_adv_query_class2',0,150000,150000)
    # load('query_img_class2.txt', '_query_img_class2', 0, 400000, 400000)
    # load('618_mnist_hardmine_class0.txt','_618_mnist_hard_class0',0,70000,70000)
    # load('non618_mnist_hardmine_class1.txt','_non618_mnist_hard_class1',0,70000,70000)

    # load('hardnegative_query_class2.txt', '_hard_query_class2', 0, 160000, 160000)
    # load('hardnegative_query_2_class2.txt', '_hard_query_2_class2', 0, 40000, 40000)
    # load('non618_photo_class1.txt', '_non618_photo_class1', 0, 480000, 480000)
    # load('618_photo_class0.txt', '_618_photo_class0', 0, 460000, 460000)
    #
    # load('non618_photo_2_class1.txt', '_non618_photo_2_class1', 0, 20000, 20000)
    # load('618_photo_2_class0.txt', '_618_photo_2_class0', 0, 40000, 40000)
    #
    # load('advertisement_query_class2.txt', '_adv_query_class2', 0, 100000, 100000)
    # #load('query_img_class2.txt', '_query_img_class2', 0, 400000, 400000)
    # load('618_mnist_hardmine_class0.txt', '_618_mnist_hard_class0', 0, 70000, 70000)
    # load('non618_mnist_hardmine_class1.txt', '_non618_mnist_hard_class1', 0, 70000, 70000)

    load('hardnegative_query_class2.txt', '_hard_query_class2', 0, 130000, 130000)
    load('hardnegative_query_2_class2.txt', '_hard_query_2_class2', 0, 40000, 40000)
    load('hardnegative_query_3_class2.txt', '_hard_query_3_class2', 0, 30000, 30000)
    load('non618_photo_class1.txt', '_non618_photo_class1', 0, 455000, 455000)
    load('618_photo_class0.txt', '_618_photo_class0', 0, 425000, 425000)

    load('non618_photo_2_class1.txt', '_non618_photo_2_class1', 0, 45000, 45000)
    load('618_photo_2_class0.txt', '_618_photo_2_class0', 0, 75000, 75000)

    load('advertisement_query_class2.txt', '_adv_query_class2', 0, 100000, 100000)
    # load('query_img_class2.txt', '_query_img_class2', 0, 400000, 400000)
    load('618_mnist_hardmine_class0.txt', '_618_mnist_hard_class0', 0, 70000, 70000)
    load('non618_mnist_hardmine_class1.txt', '_non618_mnist_hard_class1', 0, 70000, 70000)

    #genImage2id()

if __name__ == "__main__":
    main()

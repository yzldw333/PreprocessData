import os
import numpy as np
import random



if __name__ == '__main__':
    total_list = []

    dir1 = '618_freetype_class0'
    lst = random.sample(xrange(50000),50000)
    for i in lst:
        total_list.append(dir1+'/'+str(i)+'.jpg'+' 0\n')

    dir1 = '618_freetype_v4_class0'
    lst = random.sample(xrange(50000), 50000)
    for i in lst:
        total_list.append(dir1 + '/' + str(i) + '.jpg' + ' 0\n')

    dir1 = '618_freetype_v3_class0'
    lst = random.sample(xrange(50000),50000)
    lst2 = random.sample(xrange(50000),25000)
    lst.extend(lst2)
    for i in lst:
        total_list.append(dir1+'/'+str(i)+'.jpg'+' 0\n')

    dir1 = '618_freetype_v3_reflect_class0'
    lst = random.sample(xrange(50000), 50000)
    lst2 = random.sample(xrange(50000),25000)
    lst.extend(lst2)
    for i in lst:
        total_list.append(dir1 + '/' + str(i) + '.jpg' + ' 0\n')

    dir1 = '618_mnist_class0'
    lst = random.sample(xrange(100000),40000)
    for i in lst:
        total_list.append(dir1+'/'+str(i)+'.jpg'+' 0\n')

    dir1 = '618_mnist_v3_class0'
    lst = random.sample(xrange(100000),30000)
    for i in lst:
        total_list.append(dir1+'/'+str(i)+'.jpg'+' 0\n')

    dir1 = '618_mnist_v4_class0'
    lst = random.sample(xrange(100000), 30000)
    for i in lst:
        total_list.append(dir1 + '/' + str(i) + '.jpg' + ' 0\n')

    dir1 = '618_mnist_v3_reflect_class0'
    lst = random.sample(xrange(100000), 80000)
    for i in lst:
        total_list.append(dir1 + '/' + str(i) + '.jpg' + ' 0\n')

    dir2 = '618non_freetype_class1'
    lst = random.sample(xrange(50000),50000)
    for i in lst:
        total_list.append(dir2+'/'+str(i)+'.jpg'+' 1\n')

    dir2 = '618non_freetype_v4_class1'
    lst = random.sample(xrange(50000), 50000)
    for i in lst:
        total_list.append(dir2 + '/' + str(i) + '.jpg' + ' 1\n')

    dir2 = '618non_freetype_v3_class1'
    lst = random.sample(xrange(50000),50000)
    lst2 = random.sample(xrange(50000),25000)
    lst.extend(lst2)
    for i in lst:
        total_list.append(dir2+'/'+str(i)+'.jpg'+' 1\n')

    dir2 = '618non_freetype_v3_reflect_class1'
    lst = random.sample(xrange(50000), 50000)
    lst2 = random.sample(xrange(50000), 25000)
    lst.extend(lst2)
    for i in lst:
        total_list.append(dir2 + '/' + str(i) + '.jpg' + ' 1\n')

    dir2 = 'non618_mnist_class1'
    lst = random.sample(xrange(100000), 40000)
    for i in lst:
        total_list.append(dir2 + '/' + str(i) + '.jpg' + ' 1\n')

    dir2 = 'non618_mnist_v3_class1'
    lst = random.sample(xrange(100000), 30000)
    for i in lst:
        total_list.append(dir2 + '/' + str(i) + '.jpg' + ' 1\n')

    dir2 = 'non618_mnist_v4_class1'
    lst = random.sample(xrange(100000), 30000)
    for i in lst:
        total_list.append(dir2 + '/' + str(i) + '.jpg' + ' 1\n')

    dir2 = 'non618_mnist_v3_reflect_class1'
    lst = random.sample(xrange(100000), 80000)
    for i in lst:
        total_list.append(dir2 + '/' + str(i) + '.jpg' + ' 1\n')

    # dir4 = 'query_img_class2'
    # lst4 = os.listdir('618_data_v5/data/'+dir4)
    # for e in lst4:
    #     total_list.append(dir4+'/'+e+' 2\n')


    #dir5 = '618_GAN_class3/0'
    #lst5 = os.listdir('618_data_v3/data/'+dir5)
    #for e in lst5:
    #    total_list.append(dir5+'/'+e+' 3\n')

    #dir6 = '618_GAN_class3/1'
    #lst6 = os.listdir('618_data_v3/data/'+dir6)
    #for e in lst6:
    #    total_list.append(dir6+'/'+e+' 3\n')

    np.random.shuffle(total_list)
    train_list = total_list
    val_list = []
    #train_list = total_list[:int(len(total_list)*0.9)]
    val_list = total_list[int(len(total_list)*0.9):]
    print(len(train_list),len(val_list))
    photo_train = open('gen_train_618_photo_class0.txt')
    photo_val = open('gen_val_618_photo_class0.txt')
    for e in photo_train:
        train_list.append(e)
    for e in photo_val:
        val_list.append(e)
    print(len(train_list),len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    photo_train = open('gen_train_618_photo_2_class0.txt')
    photo_val = open('gen_val_618_photo_2_class0.txt')
    for e in photo_train:
        train_list.append(e)
    for e in photo_val:
        val_list.append(e)
    print(len(train_list), len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    adv_train = open('gen_train_adv_query_class2.txt')
    adv_val = open('gen_val_adv_query_class2.txt')
    for e in adv_train:
        train_list.append(e)
    for e in adv_val:
        val_list.append(e)
    print(len(train_list), len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    adv_train = open('gen_train_non618_photo_class1.txt')
    adv_val = open('gen_val_non618_photo_class1.txt')
    for e in adv_train:
        train_list.append(e)
    for e in adv_val:
        val_list.append(e)
    print(len(train_list), len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    photo_train = open('gen_train_non618_photo_2_class1.txt')
    photo_val = open('gen_val_non618_photo_2_class1.txt')
    for e in photo_train:
        train_list.append(e)
    for e in photo_val:
        val_list.append(e)
    print(len(train_list), len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    hard_train = open('gen_train_hard_query_class2.txt')
    hard_val = open('gen_val_hard_query_class2.txt')
    for e in hard_train:
        train_list.append(e)
    for e in hard_val:
        val_list.append(e)
    print(len(train_list), len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    hard_train = open('gen_train_hard_query_2_class2.txt')
    hard_val = open('gen_val_hard_query_2_class2.txt')
    for e in hard_train:
        train_list.append(e)
    for e in hard_val:
        val_list.append(e)
    print(len(train_list), len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    hard_train = open('gen_train_hard_query_3_class2.txt')
    hard_val = open('gen_val_hard_query_3_class2.txt')
    for e in hard_train:
        train_list.append(e)
    for e in hard_val:
        val_list.append(e)
    print(len(train_list), len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    query_train_lst = []
    query_train = open('query1_class2.txt')
    for e in query_train:
        query_train_lst.append(e[:-1]+' 2\n')
    query_train = open('query2_class2.txt')
    for e in query_train:
        query_train_lst.append(e[:-1]+' 2\n')
    query_train = open('query3_class2.txt')
    for e in query_train:
        query_train_lst.append(e[:-1]+' 2\n')

    query_length = len(query_train_lst)
    query_idx_lst = random.sample(xrange(query_length), 700000)
    for i in query_idx_lst:
       train_list.append(query_train_lst[i])
    print(len(train_list),len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    #query_train = open('gen_train_query_img_class2.txt')
    #for e in query_train:
    #    train_list.append(e)

    mnist618_hard_train = open('gen_train_618_mnist_hard_class0.txt')
    mnist618_hard_val = open('gen_val_618_mnist_hard_class0.txt')
    for e in mnist618_hard_train:
        train_list.append(e)
    for e in mnist618_hard_val:
        val_list.append(e)
    print(len(train_list),len(val_list))
    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    mnistnon618_hard_train = open('gen_train_non618_mnist_hard_class1.txt')
    mnistnon618_hard_val = open('gen_val_non618_mnist_hard_class1.txt')
    for e in mnistnon618_hard_train:
        train_list.append(e)
    for e in mnistnon618_hard_val:
        val_list.append(e)
    print(len(train_list), len(val_list))

    np.random.shuffle(train_list)
    np.random.shuffle(val_list)

    f = open('train_shuf.txt','w')
    for e in train_list:
        f.write(e)
    f.close()
    f = open('val_shuf.txt','w')
    for e in val_list:
        f.write(e)
    f.close()
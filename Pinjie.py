import cv2
import numpy as np
import os
def Pinjie(img8_buf,margin_height,margin_width,save_path='tmp/test.jpg'):
    '''
    Pinjie 8 images to one large image
    :param img8_buf
    :param margin_height: 
    :param margin_width: 
    :param save_path: 
    :return: None
    '''
    imgs=img8_buf
    new_imgs = []
    for img in imgs:
        sp = img.shape
        img = cv2.resize(img,(720,int(720*1.0/sp[0]*sp[1])),cv2.INTER_AREA)
        sp = img.shape
        img = cv2.resize(img,(int(480*1.0/sp[1]*sp[0]),480),cv2.INTER_AREA)
        print(img.shape)
        new_imgs.append(img)
    imgs=new_imgs
    total_width_row1 = np.sum([img.shape[1] for img in imgs[:4]])+5*margin_width
    total_width_row2 = np.sum([img.shape[1] for img in imgs[4:]])+5*margin_width
    total_width= np.maximum(total_width_row1,total_width_row2)
    total_height_lists = []
    for img1 in imgs[:4]:
        for img2 in imgs[4:]:
            tmp = img1.shape[0]+img2.shape[0]+3*margin_height
            total_height_lists.append(tmp)
    total_height=np.max(total_height_lists)

    generate_img = np.ones([total_height,total_width,3])*255
    #first row
    pos_x = margin_width
    pos_y = margin_height
    end_y_lists = []
    for i in range(4):
        end_x = pos_x+imgs[i].shape[1]
        end_y = pos_y+imgs[i].shape[0]
        generate_img[pos_y:end_y,pos_x:end_x,:] = imgs[i]
        cv2.rectangle(generate_img,(pos_x,pos_y),(end_x,end_y),color=(0,0,0),thickness=40)
        pos_x = end_x + margin_width
        end_y_lists.append(end_y)
    #second row
    pos_x = margin_width
    pos_y = np.max(end_y_lists)+margin_height
    for i in range(4,8):
        end_x = pos_x+imgs[i].shape[1]
        end_y = pos_y+imgs[i].shape[0]
        generate_img[pos_y:end_y, pos_x:end_x, :] = imgs[i]
        cv2.rectangle(generate_img, (pos_x, pos_y), (end_x, end_y), color=(0, 0, 0), thickness=40)
        pos_x = end_x + margin_width
    cv2.imwrite(save_path,generate_img)

def Pinjie4(img8_buf,margin_height,margin_width,save_path='tmp/test.jpg'):
    '''
    Pinjie 8 images to one large image
    :param img8_buf
    :param margin_height: 
    :param margin_width: 
    :param save_path: 
    :return: None
    '''
    imgs=img8_buf
    new_imgs = []
    for img in imgs:
        sp = img.shape
        img = cv2.resize(img,(720,int(720*1.0/sp[0]*sp[1])),cv2.INTER_AREA)
        sp = img.shape
        img = cv2.resize(img,(int(480*1.0/sp[1]*sp[0]),480),cv2.INTER_AREA)
        print(img.shape)
        new_imgs.append(img)
    imgs=new_imgs
    total_width_row1 = np.sum([img.shape[1] for img in imgs[:2]])+3*margin_width
    total_width_row2 = np.sum([img.shape[1] for img in imgs[2:]])+3*margin_width
    total_width= np.maximum(total_width_row1,total_width_row2)
    total_height_lists = []
    for img1 in imgs[:2]:
        for img2 in imgs[2:]:
            tmp = img1.shape[0]+img2.shape[0]+3*margin_height
            total_height_lists.append(tmp)
    total_height=np.max(total_height_lists)

    generate_img = np.ones([total_height,total_width,3])*255
    #first row
    pos_x = margin_width
    pos_y = margin_height
    end_y_lists = []
    for i in range(2):
        end_x = pos_x+imgs[i].shape[1]
        end_y = pos_y+imgs[i].shape[0]
        generate_img[pos_y:end_y,pos_x:end_x,:] = imgs[i]
        cv2.rectangle(generate_img,(pos_x,pos_y),(end_x,end_y),color=(0,0,0),thickness=40)
        pos_x = end_x + margin_width
        end_y_lists.append(end_y)
    #second row
    pos_x = margin_width
    pos_y = np.max(end_y_lists)+margin_height
    for i in range(2,4):
        end_x = pos_x+imgs[i].shape[1]
        end_y = pos_y+imgs[i].shape[0]
        generate_img[pos_y:end_y, pos_x:end_x, :] = imgs[i]
        cv2.rectangle(generate_img, (pos_x, pos_y), (end_x, end_y), color=(0, 0, 0), thickness=40)
        pos_x = end_x + margin_width
    cv2.imwrite(save_path,generate_img)

def walk_path(root_dir,out_list=[]):
    lst = os.listdir(root_dir)
    for e in lst:
        path = os.path.join(root_dir,e)
        if os.path.isdir(path):
            walk_path(path,out_list)
        else:
            if path.endswith('jpg') or path.endswith('png') or path.endswith('bmp'):
                out_list.append(path)


if __name__ == '__main__':
    #Pinjie(['tmp/'+str(i)+'.jpg' for i in range(8)],100,100,'Pinjie')
    out_list = []
    index = 0
    dst_dir = 'dst_pinjie_non618'
    walk_path('src_pinjie_non618',out_list)
    np.random.shuffle(out_list)
    length = len(out_list)
    img_buf = []
    if os.path.exists(dst_dir)==False:
        os.mkdir(dst_dir)
    for i in xrange(length):
        img = cv2.imread(out_list[i],1)
        if img is None:
            continue
        if img.shape[0] *1.0/ img.shape[1] >= 2.5 or img.shape[1]*1.0 / img.shape[0] >= 2.5:
            continue
        img_buf.append(img)
        if len(img_buf)==8:
            out_path = os.path.join(dst_dir,str(index)+'.jpg')
            while os.path.exists(out_path):
                index+=1
                out_path = os.path.join(dst_dir, str(index) + '.jpg')
            Pinjie(img_buf,200,200,out_path)
            print('%s Done!'%out_path)
            img_buf=[]
        # if len(img_buf)==4:
        #     out_path = os.path.join(dst_dir,str(index)+'.jpg')
        #     while os.path.exists(out_path):
        #         index+=1
        #         out_path = os.path.join(dst_dir, str(index) + '.jpg')
        #     Pinjie4(img_buf,300,300,out_path)
        #     print('%s Done!'%out_path)
        #     img_buf=[]



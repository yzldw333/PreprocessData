import cv2
import numpy as np
import os,sys
import matplotlib.pyplot as plt
def Drop_Repeat_Frames(seqs, frameNum):
    '''
    Drop and Repeat Frames to make each video has same frame num.
    :param seqs: video sequences
                numpy array
    :param frameNum: frame num
                int
    :return: new video sequences
                numpy array
    '''
    length = np.size(seqs,0)
    shape = seqs.shape
    if len(shape) == 4 :
        seqs = seqs.reshape([length,shape[-3],shape[-2],shape[-1]])
        counts = shape[-3]*shape[-2]*shape[-1]
    elif len(shape) == 3:
        seqs = seqs.reshape([length,shape[-2],shape[-1],1])
        counts = shape[-2]*shape[-1]
    else:
        print("Shape ERROR!")
        return

    shape = seqs.shape
    newSeqs = []
    for i in range(frameNum):
        idx = (int)(i*1.0/frameNum*length+0.5)
        if idx>=length:
            idx=length-1
        newSeqs.extend(list(seqs[idx].ravel()))
    newSeqs = np.array(newSeqs,dtype=np.float32).ravel()
    length = len(newSeqs)//counts
    if len(shape) == 4:
        seqs = newSeqs.reshape([length,shape[-3],shape[-2],shape[-1]])
    return seqs

def extract_frame(path,idx,strides,outdir):
    cap = cv2.VideoCapture(path)
    p = 0
    tmpid=idx
    while (True):
        res, frame = cap.read()
        if res:
            if p%strides == 0:
                dst_path = os.path.join(outdir,str(tmpid)+'.jpg')
                while os.path.exists(dst_path):
                    tmpid +=1
                    dst_path = os.path.join(outdir, str(tmpid) + '.jpg')
                cv2.imwrite(dst_path,frame)
            p+=1
        else:
            break
    return tmpid


def GetVideoSeq(name):
    '''
        use opencv to read video sequences
    :param name: video name like 'xxx.avi'
    :param color: is gray?
    :param style: normal/gradient image
    :return: numpy array with the shape of
            (length,channel,height,width)
            or
            (2,length,channel,height,width)
    '''
    cap = cv2.VideoCapture(name)
    seqShape = None
    if cap.isOpened() == False:
        return None
    seqs = []
    length = 0
    while(True):

        res, frame = cap.read()
        if res:
            seqShape = frame.shape
            seqs.append(list(frame.ravel()))
            length += 1
        else:
            break
    seqs = np.array(seqs, dtype=np.float32)
    if len(seqShape) == 3:
        seqs = seqs.reshape([length,seqShape[0],seqShape[1],seqShape[2]])
    elif len(seqShape) == 2:
        seqs = seqs.reshape([length,seqShape[0],seqShape[1]])
    return seqs

def walk_dir_and_extract_frame(dir_path,out_dir,strides=5):
    lst = os.listdir(dir_path)
    idx = 0
    for e in lst:
        if e.endswith('.mp4'):
            path = os.path.join(dir_path,e)
            idx = extract_frame(path,idx,strides,out_dir)
            print('%s Done'%e)




if __name__ == '__main__':
    walk_dir_and_extract_frame(r'E:\data\618data\0608video',r'E:\data\618data\0608video\extract_frames',5)
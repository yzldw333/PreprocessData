import pytube
import os
if __name__ == '__main__':
    dataroot = r'E:\data\sports-1m-dataset-master\data'
    labelfile = r'E:\data\sports-1m-dataset-master\original\train_partition.txt'
    f = open(labelfile)
    index = 0
    for e in f:
        url = e.split()[0]
        label = e.split()[1]
        yt = pytube.YouTube(url)
        outname = str(index)
        outpath = dataroot + '/' + outname
        while os.path.exists(outpath+'.mp4') or os.path.exists(outpath+'.avi') or os.path.exists(outpath+'.MP4')\
                or os.path.exists(outpath+'.AVI') or os.path.exists(outpath+'.3gp'):
            index+=1
            outpath = dataroot + '/' + outname
        yt.set_filename(outpath)
        video = yt.filter(resolution='144p')[0]
        video.download(dataroot)
        index+=1
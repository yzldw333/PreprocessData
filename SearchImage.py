import requests,urllib
import os,sys

def CheckArgs():
    if(len(sys.argv) < 3):
        print 'Usage: python ImgSearch.py [Keyword] [DownloadDir] [Pages=1]'
        return False
    return True

def Search():
    params = {
        'tn' : 'resultjsonavatarnew',
        'ie' : 'utf-8',
        'cg' : '',
        'itg' : '',
        'z' : '0',
        'fr' : '',
        'width' : '',
        'height' : '',
        'lm' : '-1',
        'ic' : '0',
        's' : '0',
        'word' : sys.argv[1],
        'st' : '-1',
        'gsm' : '',
        'rn' : '30'
        }

    if(len(sys.argv) == 4):
        pages = int(sys.argv[3])
    else:
        pages = 1

    for i in range(0, pages):
        params['pn'] = '%d' % i
        Request(params)
    return

def Request(param):
    searchurl = 'http://image.baidu.com/search/avatarjson'
    response = requests.get(searchurl, params=param)
    json = response.json()['imgs']

    for i in range(0, len(json)):
        filename = os.path.split(json[i]['objURL'])[1]
        print 'Downloading from %s' % json[i]['objURL']
        Download(json[i]['objURL'], filename)

    return

def Download(url, filename):
    if(os.path.exists(sys.argv[2]) == False):
        os.mkdir(sys.argv[2])
    filepath = os.path.join(sys.argv[2], '%s' % filename)
    urllib.urlretrieve(url, filepath)
    return

if __name__ == '__main__':
    if(CheckArgs() == False):
        sys.exit(-1)
    Search()
    print 'Total Images:%d' % len(os.listdir(sys.argv[2]))
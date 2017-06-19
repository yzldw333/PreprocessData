# coding=utf-8
# 声明编码方式 默认编码方式ASCII 参考https://www.python.org/dev/peps/pep-0263/
import urllib
import time
import re
import os

''''' 
Python下载游迅网图片 BY:Eastmount 
'''

''''' 
************************************************** 
#第一步 遍历获取每页对应主题的URL 
http://www.58pic.com/tupian/shuang11-0-0-01.html
************************************************** 
'''
#fileurl = open('yxdown_url.txt', 'w')
#fileurl.write('****************获取千图网图片URL*************\n\n')
# 建议num=3 while num<=3一次遍历一个页面所有主题,下次换成num=4 while num<=4而不是1-75
num = 1
while num <= 50:
    temp = 'http://www.58pic.com/tupian/guanggaobeijing-0-0-' + str(num) + '.html'
    content = urllib.urlopen(temp).read()
    #open('yxdown_' + str(num) + '.html', 'w+').write(content)
    print temp
    #fileurl.write('****************第' + str(num) + '页*************\n\n')

    # 爬取对应主题的URL
    # <div class="cbmiddle"></div>中<a target="_blank" href="/html/5533.html" >
    count = 1  # 计算每页1-75中具体网页个数
    # listBox > div:nth-child(1) > div.flow-thumb
    res_div = r'<div class="flow-thumb" (.*?)</div>'
    m_div = re.findall(res_div, content, re.S | re.M)
    for line in m_div:
        # fileurl.write(line+'\n')
        # 获取每页所有主题对应的URL并输出
        #if "_blank" in line:  # 防止获取列表list/1_0_1.html list/2_0_1.html
            # 获取主题
            #fileurl.write('\n\n********************************************\n')
            #title_pat = r'<b class="imgname">(.*?)</b>'
            #title_ex = re.compile(title_pat, re.M | re.S)
            #title_obj = re.search(title_ex, line)
            #title = title_obj.group()
            #print unicode(title, 'utf-8')
            #fileurl.write(title + '\n')
            #  获取URL
        res_href = r'<img  src="(.*?)"(.*?)'
        m_linklist = re.findall(res_href, line)
        # print unicode(str(m_linklist),'utf-8')
        for link in m_linklist:
            #fileurl.write(str(link) + '\n')  # 形如"/html/5533.html"

            ''''' 
            ************************************************** 
            #第二步 去到具体图像页面 下载HTML页面 
            #http://pic.yxdown.com/html/5533.html#p=1 
            #注意先本地创建yxdown 否则报错No such file or directory 
            ************************************************** 
            '''
            # 下载HTML网页无原图 故加'#p=1'错误
            # HTTP Error 400. The request URL is invalid.
            #html_url = 'http://pic.yxdown.com' + str(link)
            #print html_url
            link = link[0]
            index = link.find('jpg')+3
            link = link[:index]
            print link
            filename = os.path.basename(link)  # 去掉目录路径,返回文件名
            try:
                urllib.urlretrieve(link, './advertisement_bg/' + str(num)+'_'+filename)
            except:
                print(filename+' error')
                continue
            # 当前页具体内容个数加1
        count = count + 1
        time.sleep(0.1)
        #else:
            #print 'no url about content'

    time.sleep(1)
    num = num + 1
else:
    print 'Download Over!!!'
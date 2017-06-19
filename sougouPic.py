# -*- coding: utf-8 -*-
import string
import urllib2
import re
import os


class SouGouPic_Spider:
    # 申明相关属性
    def __init__(self):
        # 给SougoPicUrl属性赋值
        self.SougoPicUrl = "http://pic.sogou.com/pics?query=%CA%D6%D0%B4&st=100&mode=2000"
        # 用来保存图片URL信息
        self.imgUrl = []
        print u'已经启动搜狗图片爬虫，爬爬...'


        # 保存页面信息

    def Download_Pic(self):
        # 把图片的url加载到数组中
        self.get_infor()
        try:
            # 创建图片保存的文件夹
            os.mkdir('ShouxiePic')
        except WindowsError:
            pass
            # 进入创建的文件夹
        os.chdir('ShouxiePic')
        # 给操作的url页面赋初始值，并获取url的 源码
        page = urllib2.urlopen(self.SougoPicUrl).read()
        # 获取每一个jpg图片的url
        for pic in self.imgUrl:
            # 获取jpg文件的名称
            imgName = re.split('/', pic)[-1]
            try:
                # 打开图片的URL
                conn = urllib2.urlopen(pic)
                # 创建并保存图片
                f = open(imgName, 'wb')

                # 把获取的图片保存
                f.write(conn.read())

                # 关闭打开的文件
                f.close()
                print u'爬虫报告：文件' + imgName + u'已经下载'
            except:
                print '%s wrong.'%pic
        print u'按任意键退出...'
        raw_input()

        # 获取页面源码并将其存储到数组中

    def get_infor(self):
        # 获取页面中的源码
        page = urllib2.urlopen(self.SougoPicUrl).read()

        # 把页面中所有jpg图片的URL提取出来
        self.deal_picUrl(page)
        # print self.imgUrl

    # 从页面代码中获取所需图片URL
    def deal_picUrl(self, page):
        # 获取"pic_url":"http://xxxxx/x/x.jpg"图片url  
        PicItems = re.findall('\"pic_url\":\"(.*?)\"', page, re.S)

        # 把图片的url添加到imgUrl列表中
        for aItem in PicItems:
            self.imgUrl.append(aItem)



            # ------------程序入口处----------------


print u"""#--------------------------------------- 
#   程序：搜狗图片爬虫 
#   作者：ewang 
#   日期：2016-7-7 
#   语言：Python 2.7 
#   功能：获取页面中的图片并保存到文件SouGouPic中。 
#-------------------------------------------------- 
"""

SougouPic = SouGouPic_Spider()
SougouPic.Download_Pic()  
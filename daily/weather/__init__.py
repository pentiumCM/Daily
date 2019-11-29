#!/usr/bin/env python
# encoding: utf-8
'''
@Author  : pentiumCM
@Email   : 842679178@qq.com
@Software: PyCharm
@File    : __init__.py.py
@Time    : 2019/11/29 19:15
@desc	 : 爬取天气预报的数据
'''


import itchat
import re
import urllib2
import itchat
#模拟浏览器
hearders = "User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"

url = "https://tianqi.moji.com/weather/china/guangdong/shantou"    ##要爬去天气预报的网址
par = '(<meta name="description" content=")(.*?)(">)'    ##正则匹配，匹配出网页内要的内容

##创建opener对象并设置为全局对象
opener = urllib2.build_opener()
opener.addheaders = [hearders]
urllib2.install_opener(opener)

##获取网页
html = urllib2.urlopen(url).read().decode("utf-8")

##提取需要爬取的内容
data = re.search(par,html).group(2)

##接下来是微信部分了
itchat.auto_login()    ##登录
users = itchat.search_friends(name=u'xx')   ##这里的xx是通信录备注的名称
userName = users[0]['UserName']    ##找到UserName
itchat.send(data,toUserName = userName)    ##发送信息，data就是爬取的内容
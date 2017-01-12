# -*- coding: utf-8 -*-
__author__ = 'acer-zhou'
"""
@file: 模拟登陆华东师范大学图书馆查询借阅信息
@time: 2016/11/24 13:09
"""

from lxml import etree
import requests

# 直接登录requests会自己处理重定向问题
# s = requests.Session()

# headers
headers1 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
# 登录字段
postdata = {'extpatid':'51164402041',
            'extpatpw':'9314zhouwei',
            'submit.x':'42',
            'submit.y':'16'}

# post参数模拟登陆,禁止重定向，否则后面无法访问借阅页面
r1 = requests.post('https://libecnu.lib.ecnu.edu.cn/patroninfo*chx~S0', headers=headers1, data=postdata,  allow_redirects=False)
print r1.cookies
print r1.url

# get方式访问借阅页面
headers2 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Referer': 'https://libecnu.lib.ecnu.edu.cn/patroninfo*chx~S0'}
r2 = requests.get('https://libecnu.lib.ecnu.edu.cn/patroninfo~S0*chx/1247702',cookies=r1.cookies, headers=headers2)
html = r2.text
print r2.cookies

# 使用xpath解析借阅信息
selector = etree.HTML(html)
# 解析书名
bookname = selector.xpath('/html/body/div[2]/div[2]/div[1]/form/table//a/text()')
# 解析到期时间
deadline = selector.xpath('/html/body/div[2]/div[2]/div[1]/form/table//td[@class="patFuncStatus"]/text()')

for i,d in zip(bookname,deadline):
    print i,d
for:
print i

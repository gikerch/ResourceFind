#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
from lxml import etree


# 第一种方式 直接解析爬取下来的网页失败
r = requests.get('http://202.120.82.17:8080/ldb/typeindex.jsp?typeid=%s')
html = r.text
selector = etree.HTML(html)
nodes = selector.xpath(
    '/html/body/div/table/tbody/tr/td/table[1]/tbody/tr[2]/td[1]/table/tbody/tr/td/span/a/text()')
print nodes[0].encode('utf-8')


# 解码为Unicode，防止乱码
html = unicode(html, 'utf-8')
selector = etree.HTML(html)
nodes = selector.xpath(
    '/html/body/div/table/tbody/tr/td/table[1]/tbody/tr[2]/td[1]/table/tbody/tr/td/span/a/text()')
print nodes[0].encode('utf-8')


# 批量处理函数
def ex_url(a):
    for i in range(30):
        r = requests.get('http://202.120.82.17:8080/ldb/typeindex.jsp?typeid=%s')
        html = r.text
        selector = etree.HTML(html)
        try:
            for i in range(a, 237, 2):
                nodes = selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tbody/tr[%d]/td[1]/table/tr/td/span/a/text()' % i)
                print nodes[0].encode('utf-8')

        except IndexError, e:
	        nodes = selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tbody/tr[%d]/td[1]/table/tr/td/table/tbody/tr[1]/td/font/text()' % i)
	        print i, nodes[0].encode('utf-8')
	        a = i + 2
	        ex_url(a)


# 测试用例
if __name__ == "__main__":
    ex_url(2)

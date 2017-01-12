# -*- coding: utf-8 -*-
__author__ = 'acer-zhou'
"""
@version: ??
@license: Apache Licence
@file: all_url.py
@time: 2016/11/20 15:15
"""

import requests
from lxml import etree


# 批量处理函数
def ex_url(a,k,dict):

        # 抓取网页
        r = requests.get('http://202.120.82.17:8080/ldb/typeindex.jsp?typeid=%s' %k)
        html = r.text
        selector = etree.HTML(html)
        f = open(str(k)+'.txt','w+')

        for i in range(2, 250, 2):
            try:
                # 使用xpath解析
                nodes = selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tr[%d]/td[1]/table/tbody/tr/td/span/a/text()' %a)
                links = selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tr[%d]/td[1]/table/tbody/tr/td/span/a/@href' %a)
                # print i,nodes[0]
                print nodes[0],'@@',links[0]
                #print links[0]
                url=nodes[0].encode('utf-8')
                link=links[0].encode('utf-8')
                f.write(url+'@@'+link+'\n')
                a+=2

            except IndexError:
                # 使用xpath解析
                nodes = selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tr[%d]/td[1]/table/tbody/tr/td/table/tbody/tr[1]/td/font/text()' %a)
                url=nodes[0].encode('utf-8')
                f.write(url+'\n')
                print i/2,nodes[0]
                a+=2

    
# 测试用例
if __name__ == "__main__":
    ex_url(2,1,{})
  


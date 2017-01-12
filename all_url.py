# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# __author__ = 'acer-zhou'
# """
# @version: ??
# @license: Apache Licence
# @file: all_url.py
# @time: 2016/11/20 15:15
# """
#
# import requests
# from lxml import etree
#
#
# # 批量处理函数
# def ex_url(a,k):
#         r = requests.get('http://202.120.82.17:8080/ldb/typeindex.jsp?typeid=%s' %k)
#         html = r.text
#         selector = etree.HTML(html)
#         list = []
#         try:
#             for i in range(a, 250, 2):
#                 nodes = selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tr[%d]/td[1]/table/tbody/tr/td/span/a/text()' %i)
#                 #print i,nodes[0]
#                 list.append(nodes[0])
#                 print list
#
#
#         except IndexError, e:
#             nodes = selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tr[%d]/td[1]/table/tbody/tr/td/table/tbody/tr[1]/td/font/text()' %i)
#             #print nodes[0]
#             list.append(nodes[0])
#             print list
#             a = i + 2
#             ex_url(a,k)
#
#
# def save_url(list):
#     f = open('urllist.txt','w')
#     for l in list:
#         url = l+'/n'
#         f.write(url)
# # 测试用例
# if __name__ == "__main__":
#     ex_url(2,1)
#
#
#!/usr/bin/python
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
def ex_url(b,f,k,dict):
        r = requests.get('http://202.120.82.17:8080/ldb/typeindex.jsp?typeid=%s' %k)
        html = r.text
        selector = etree.HTML(html)

        for i in range(b, f, 2):
            try:

                nodes = selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tr[%d]/td[1]/table/tbody/tr/td/span/a/text()' %i)
                # print i,nodes[0]
                dict[i] = nodes[0]
                #print list

            except IndexError, e:
                nodes = selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tr[%d]/td[1]/table/tbody/tr/td/table/tbody/tr[1]/td/font/text()' %i)
                # print nodes[0]
                dict[i] = nodes[0]
                #list.append(nodes[0])
                #print list

                b = i + 2
                ex_url(b,f,k,dict)
            save_url(dict)


def save_url(dict):
    f = open('urllist.txt','w')
    for k,v in dict.iteritems():
        k=str(k)
        v=str(v)
        url = k+' '+v+'\n'
        #url = (item+'\n').encode('utf-8')
        #
        f.write(url)
# 测试用例
if __name__ == "__main__":
    ex_url(2,236,1,{})





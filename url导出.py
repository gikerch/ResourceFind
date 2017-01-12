# -*- coding: utf-8 -*-
__author__ = 'acer-zhou'
import os 
import urllib
import urllib2
import cookielib

# 验证码图片地址, 登陆post地址,数据导出地址
valicode_url = 'http://172.20.3.252:9090/check2code.action'
login_url = 'http://172.20.3.252:9090/LoginAction.action'
export_url = 'http://172.20.3.252:9090/url/url-export.action'

# 将cookies绑定到一个opener cookie由cookielib自动管理
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

# 用户名和密码
username = 'test2'
password = 'Test12#$'

# 用openr访问验证码地址,获取cookie
picture = opener.open(valicode_url).read()
# 把验证码保存到本地
# local = open('E:/resource_find/valicode.jpg', 'wb')
local = open('F:/Python/resource_find/valicode.jpg', 'wb')
local.write(picture)
local.close()
# 打开保存的验证码输入
valicode = raw_input('input valicode:')

# post_data
post_data = {'form.userID': username,
             'form.password': password,
             'form.validateCode': valicode,
             'form.code': 'on'}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
}
# 生成post数据 ?key1=value1&key2=value2的形式
data = urllib.urlencode(post_data)
# 构造request请求，方法为post
request = urllib2.Request(login_url, data, headers)
try:
    response = opener.open(request)
    result = response.read().decode('utf-8')
    print result
except urllib2.HTTPError, e:
    print e.code

# 进度条
# def cbk(a, b, c):
#     per = 100.0 * a * b / c
#     if per > 100:
#         per = 100
#     print '%.2f%%' % per

# 利用之前存有cookie的opener登录页面
# TODO
# urllib方法，没有成功传cookie，暂时未解决
# local = 'F:/PycharmProjects/data.csv'
# urllib.urlretrieve(export_url,local,cbk)

# urllib2方法
# 导出CSV文件函数


def download_csv(start, end, retry_num=5):

    form_post = {'form.today': 2,
                 'form.dto.dip': '',
                 'form.dto.subtype': '',
                 'form.dto.type': '',
                 'form.dto.username': '',
                 'form.dto.descid': '',
                 'form.dto.domain': '',
                 'form.dto.browser': '',
                 'form.dto.platform': '',
                 'form.dto.action': '',
                 'form.dto.dir': '',
                 'form.dto.line': '',
                 'form.dto.url': '',
                 'form.time1': start,
                 'form.time2': end,
                 'form.dto.sip': 'IP'}

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36', }

    # 生成post数据 ?key1=value1&key2=value2的形式
    data2 = urllib.urlencode(form_post)
    # 重试5次，如果失败打印消息
    try:
        request2 = urllib2.Request(export_url, data2, headers)
        response2 = opener.open(request2).read()
    except Exception,e:
        print e.message
        if retry_num > 0:
            return download_csv(start, end, retry_num = retry_num-1)
        else:
            print 'get Failed'
            return ''

    #pre = start[-8:-6] + start[-5:-3]a
    # 文件名称格式日期_开始时间_结束时间：161230_2000_2020
    date = start[2:10].replace('-','_')
    stime = start[11:16].replace(':','')
    etime = end[11:16].replace(':','')
    filename = date + '_' + stime + '_' + etime
    local = '%s.csv' % filename
    path = date
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(date+'/'+local, 'w')
    f.write(response2)
    f.close()
    print 'file saved in:'+date

if __name__ == '__main__':
    # 时间格式为：2016-12-28 00:00:00
    # 时间列表可以使用excle自动填充实现
    # time_list = [('2016-12-30 20:00:00', '2016-12-30 20:20:00'),
    #              ('2016-12-30 20:20:00', '2016-12-30 20:40:00'),
    #              ('2016-12-30 20:40:00', '2016-12-30 21:00:00'),
    #              ('2016-12-30 21:00:00', '2016-12-30 21:20:00'),
    #              ('2016-12-30 21:20:00', '2016-12-30 21:40:00'),
    #              ('2016-12-30 21:40:00', '2016-12-30 22:00:00')]

    list = []
    f = open('time.txt','r')
    for i in f.readlines():
        list.append(i[:-1]+':00')
    start_list = list[:-1]
    end_list = list[1:]

    time_list= []
    for s,e in zip(start_list,end_list):
        time = s_e = (s,e)
        time_list.append(time)
    print time_list

    # 下载文件
    for i in time_list:
        start, end = i
        download_csv(start, end)
    print 'well done'
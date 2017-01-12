# encoding:utf-8
"""
Spyder Editor

This is a temporary script file.
"""
"""
network-api v0.1

接口采取 Oauth2 方式授权，获取 access_token 后，可请求 API 接口。

请求 access_token

请求方式： HTTP POST

请求地址 https:/network-api.ecnu.edu.cn/token.php

请求示例（curl） curl https://network-api.ecnu.edu.cn/oauth/token.php -d 'grant_type=client_credentials&client_id=testclient&client_secret=testpass' 正确返回示例 { "access_token": "1b7e9c29cc9e2cd50fd088815d42b2dd51f42a52", "expires_in": 3600, "token_type": "Bearer", "scope": "ECNU-basic" } 错误返回示例 { "error": "invaild_client", "error_description": "The client credentials are invalid" } 请求参数说明 client_id ：申请的应用账号，这里为 testclient cliet_secret: 申请的应用账号密码，这里为 testpass grant_type: 请求 token 的模式，填 client_credentials

返回参数说明 access_token: 获取的 access_token expires_in: token 的有效期，3600秒，过期后需要重新申请token才能请求api token_type： token 的模式是 Bearer scope: scope为 ECNU-basic 返回错误说明 error: 错误 error_description: 错误说明

请求 API 接口

请求方式： HTTP GET

请求地址： https://network-api.ecnu.edu.cn/oauth/userinfo.php

请求示例（curl） curl 'https://network-api.ecnu.edu.cn/oauth/userinfo.php?access_token=1b7e9c29cc9e2cd50fd088815d42b2dd51f42a52&user_ip=59.78.187.55&user_time=1477965601' 正确返回示例 { "success": true, "add_time": 1477964089, "drop_time": 1478011407, "user_info": { "user_encrypt": "89a18f4ffd3", "BMMC": "\u7ecf\u6d4e\u4e0e\u7ba1\u7406\u4e13\u4e1a\u5b66\u4f4d\u6559\u80b2\u4e0e\u57f9\u8bad\u4e2d\u5fc3" } } 错误返回示例 ``` { "success": false, "msg": "can not found such user" }

请求参数说明 accesstoken ：请求的 token，即上一步中所获得的 token userip: 记录的 ip 地址 user_time: 记录的 unix 时间戳（例如2016-11-01 10：00：00 需要转换成时间戳 1477965600，单位是秒） ```

返回参数说明 success: true 表示正确返回 add_time: 用户上线的时间 drop_time： 用户下线的时间 user_info: 用户的相关信息 user_encrypt: 学号/工号脱敏加密后的字符串，唯一 BMMC：部门信息，unicode编码。实例中解码后应为"经济与管理专业学位教育与培训中心"

错误返回说明 success: fasle 表示返回错误 msg: 错误原因
"""

import requests
import time

# 获取token
def get_token():
    tokentime = time.time()
    params = {'grant_type': 'client_credentials',
                  'client_id': 'testclient', 'client_secret': 'testpass'}
    r = requests.post("https://network-api.ecnu.edu.cn/oauth/token.php", data=params)
    token = r.text[17:57]
    return token,tokentime


# 初始化token和tokentime
access_token,tokentime = get_token()
# 将ip地址和时间拼成元祖对格式：[('59.78.187.55','1477965601'),('59.78.187.55','1477965601'),...]
iplist = ['59.78.187.55','59.78.187.55','59.78.187.55','59.78.187.55','59.78.187.55','59.78.187.55','59.78.187.55']
timelist = [1477965601,1477965601,1477965601,1477965601,1477965601,1477965601,1477965601]
zipped = zip(iplist,timelist)

for item in zipped:
    # upack元祖
    ip,user_time = item
    # 判断token是否失效
    if tokentime + 3000 <time.time():
        access_token,tokentime = get_token()
    # 传递参数
    payload = {'access_token':access_token,
               'user_ip': ip, 'user_time':user_time}
    # get方式获取userinfo
    r = requests.get('https://network-api.ecnu.edu.cn/oauth/userinfo.php', params=payload)
    print r.text



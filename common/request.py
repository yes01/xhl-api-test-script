import requests
import time
import uuid
import json
# import jwt
# import string
# import random
from utils.Yaml import Yaml
# from datetime import datetime, timedelta
from project.modules import splicing_url

yaml = Yaml()
ENV = yaml.get_yaml_config('ENV')
ENV_URL = yaml.get_yaml_config('ENV_URL')
token = None
web_token = yaml.get_yaml_config('ENV_WEB_TOKEN')


def get_access_token():
    """获取Access Token"""
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "KS-Client-Request-Id": str(uuid.uuid1())
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "all"

    }
    try:
        url = ENV_URL + splicing_url.auth_token
        response = requests.post(url, json=data, headers=headers, timeout=15)
        res = response.json()
        print("auth_token==>", res)
        token_type = res["data"]["token_type"]
        token_res = res["data"]["access_token"]
        access_token = token_type + " " + token_res
        return access_token
    except Exception as e:
        print("exception=======>", str(e))


# def get_member_access_token(version, authorization=None):
#     """获取User Access Token"""
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "KS-Client-Request-Id": str(uuid.uuid1()),
#         "Authorization": authorization,
#         "KS-Lang": ENV_LANGUAGE,
#         "KS-Region": ENV_REGION
#     }
#     data = {
#         "account": ENV_WEB_MEMBER_PHONE,
#         "password": ENV_WEB_MEMBER_PWD
#     }
#
#     try:
#         url = ENV_URL + version + splicing_url.member_login
#         response = requests.post(url, json=data, headers=headers, timeout=15)
#         res = response.json()
#         print("user_access_token==>", res)
#         user_access_token = res["data"]["user_access_token"]
#         return user_access_token
#     except Exception as e:
#         print("exception=======>", str(e))

def get(get_url, data, module_url=ENV_URL, header="valuable"):
    url = module_url + get_url
    print('请求url==> %s' % url)
    print('请求参数==> %s' % data)
    global token
    token = web_token
    if not token:
        token = get_access_token()
    headers = {
        "token": token
    }
    if header in "valuable":
        headers = headers
    else:
        del headers['token']
    try:
        print("请求header==>", headers)
        response = requests.get(url=url, json=data, headers=headers, timeout=15)
        status_code = response.status_code
        if status_code != 200:
            print("「{0}」响应http_code==>{1}".format(get_url, status_code))
        res = response.json()
        res["status_code"] = status_code
    except Exception as e:
        res = json.dumps({"request exception": 400})
        print("exception=======>", str(e))
    return res


def post(post_url, data, module_url=ENV_URL, header="valuable"):
    """
    @type post_url: 请求路径
    @type data: 请求参数
    @type module_url: 域名地址
    @type header: 请求头是否为空，默认为有值(token)
    """
    time.sleep(1)
    j_data = json.dumps(data, ensure_ascii=False)
    j_data = j_data.encode('utf-8')
    url = module_url + post_url
    print("请求url==>", url)
    print("请求参数==>", data)
    global token
    token = web_token
    if not token:
        token = get_access_token()
    headers = {
        "token": token
    }
    if header in "valuable":
        headers = headers
    else:
        del headers['token']
    try:
        print("请求header==>", headers)
        response = requests.post(url, j_data, headers=headers, timeout=15)
        status_code = response.status_code
        if status_code != 200:
            print("「{0}」响应http_code==>{1}".format(post_url, status_code))
        res = response.json()
        res["status_code"] = status_code
    except Exception as e:
        res = json.dumps({"request exception": 400})
        print("exception=======>", str(e))
    return res


# def member_post(module_url, post_url, data, version, web_tokens):
#     time.sleep(1)
#     j_data = json.dumps(data, ensure_ascii=False)
#     j_data = j_data.encode('utf-8')
#     url = module_url + version + post_url
#     global token
#     if not token:
#         token = get_access_token(version)
#     print("请求url==>", url)
#     print("请求参数==>", data)
#     # 登錄、第三方登錄、註冊接口、验证账号无需user_access_token
#     not_token = ["/member/login", "/member/login_with_provider", "/member/register", "/member/validate_account"]
#     headers = {
#         "Content-Type": "application/json;charset=UTF-8",
#         "KS-Client-Request-Id": str(uuid.uuid1()),
#         "KS-Ec-App-Id": ENV_EC_APP_ID,
#         "Authorization": token,
#         "KS-Lang": ENV_LANGUAGE,
#         "KS-Region": ENV_REGION,
#         "KS-Auth-Type": "OAuth"
#     }
#     if post_url not in not_token:
#         if web_tokens is None:
#             web_member_token = web_token
#         else:
#             web_member_token = web_tokens
#         if not web_member_token:
#             web_member_token = get_member_access_token(version, token)
#         headers.update({"User-Access-Token": web_member_token})
#     try:
#         print("请求header==>", headers)
#         response = requests.post(url, j_data, headers=headers, timeout=15)
#         status_code = response.status_code
#         if status_code != 200:
#             print("「{0}」响应http_code==>{1}".format(post_url, status_code))
#         res = response.json()
#         res["status_code"] = status_code
#     except Exception as e:
#         res = json.dumps({"request exception": 400})
#         print("exception=======>", str(e))
#     return res


# def post_token(module_url, post_url, data, version):
#     time.sleep(1)
#     j_data = json.dumps(data, ensure_ascii=False)
#     j_data = j_data.encode('utf-8')
#     url = module_url + version + post_url
#     print("请求url==>", url)
#     print("请求参数==>", data)
#     try:
#         response = requests.post(url, j_data, timeout=15)
#         res = response.json()
#         res["status_code"] = response.status_code
#     except Exception as e:
#         res = json.dumps({"request exception": 400})
#         print("exception=======>", e)
#
#     return res


# def token_post(post_url, data, version="v1.0"):
#     res = post_token(ENV_URL, post_url, data, version)
#     return res


# def ecom_member_post(post_url, data, version="v1.5", web_tokens=None):
#     """
#     @type post_url: 请求路径
#     @type data: 请求参数
#     @type version: 接口版本
#     @type web_tokens: 请求参数(token)
#     """
#     res = member_post(ENV_URL, post_url, data, version, web_tokens)
#     return res


# def get_validate_token(status="reset_pwd", expired_minutes=30):
#     f = '%Y-%m-%d %H:%M:%S'
#     times = (datetime.now() + timedelta(minutes=expired_minutes)).strftime(f)
#     t = int(datetime.strptime(times, f).timestamp())
#     payload = {
#         "cluster": ENV_CLUSTER,  # ap1 或 ap2
#         "env": ENV,  # dev或staging 或 release 或 sandbox
#         "ec_app_id": ENV_EC_APP_ID,
#         "user_id": int(ENV_USER_ID),
#         'expire_time': t,  # 令牌过期时间
#     }
#     payload if status == "reset_pwd" else payload.pop("user_id")
#     encoded_jwt = jwt.encode(payload, ENV_JWT_KEY, algorithm='HS256')
#     return encoded_jwt

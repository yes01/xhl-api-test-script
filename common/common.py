from loguru import logger
from config import config
import hashlib
import time
# import string
# import random
import allure


conf = config.ConfigBase()

ENV_URL = conf.ENV_URL


def check_type(data, d_type, d_type2=None):
    """判断类型"""
    if not d_type2:
        if isinstance(data, d_type) is not True:
            raise TypeError("返回的参数类型错误")
        else:
            return True
    else:
        if (isinstance(data, d_type) is True) or (isinstance(data, d_type2) is True):
            return True
        else:
            raise TypeError("返回的参数类型错误")


@allure.step("断言：期待类型与实际类型判断")
def assert_check_type(data, d_type):
    """断言：类型判断"""
    logger.info("断言：期待类型与实际类型一致")
    logger.info("期待：【%s】" % d_type)
    if isinstance(data, d_type) is True:
        logger.info("结果：断言成功！！！")
    else:
        logger.info("实际：【%s】" % type(data))
        logger.info("结果：断言失败！！！")
    assert isinstance(data, d_type)


@allure.step("断言：响应数据与期待值判断")
def assert_content(connect, expect):
    """断言：内容判断"""
    logger.info("断言：响应数据与期待值一致")
    logger.info("期待：【%s】" % expect)
    if expect == connect:
        logger.info("结果：断言成功！！！")
    else:
        logger.info("实际：【%s】" % connect)
        logger.info("结果：断言失败！！！")
    assert expect == connect


@allure.step("断言：响应数据与期待值判断")
def assert_content_in(connect, expect):
    """断言：内容文本是否包含期待值"""
    logger.info("断言：响应数据包含期待值")
    logger.info("期待：【%s】" % expect)
    if str(expect) in str(connect):
        logger.info("结果：断言成功！！！")
    else:
        logger.info("实际：【%s】" % connect)
        logger.info("结果：断言失败！！！")
    assert str(expect) in str(connect)


@allure.step("断言：响应数据与期待值判断")
def assert_content_not_in(connect, expect):
    """断言：内容文本是否包含期待值"""
    logger.info("断言：响应数据不包含期待值")
    logger.info("期待：【%s】" % expect)
    if expect not in connect:
        logger.info("结果：断言成功！！！")
    else:
        logger.info("实际：【%s】" % connect)
        logger.info("结果：断言失败！！！")
    assert expect not in connect


def modify_dictionary(data, modify_target, content):
    for k in list(data.keys()):
        if modify_target == k:
            if content is None:
                data.pop(modify_target)
            else:
                data[modify_target] = content


def modify_list(data, key, modify_target, content):
    for i in data[key]:
        for k in list(i.keys()):
            if modify_target == k:
                if content is None:
                    i.pop(modify_target)
                else:
                    i[modify_target] = content


# def generate_number(num):
#     """生成随机数字+字母"""
#     random_number = 'test_'
#     words = ''.join((string.ascii_lowercase, string.ascii_uppercase, string.digits))
#     for i in range(int(num-5)):
#         random_number += random.choice(words)
#     return random_number


# def generate_number02(num):
#     """创建优惠卷专用生成随机数字+字母"""
#     random_number = 'test'
#     words = ''.join((string.ascii_lowercase, string.ascii_uppercase, string.digits))
#     for i in range(int(num-4)):
#         random_number += random.choice(words)
#     return random_number


def parsing_list(connect):
    """
    @param connect: list中包含dict
    @return: 输出列表中字典key-value
    """
    connect_list = []
    for i in connect:
        for kk, vv in i.items():
            connect_list.append(kk)
            connect_list.append(vv)
    return connect_list


@allure.step("筛选返回指定数据")
def filter_list(target_list, key, expect):
    """筛选返回指定数据（兼容部分list数据由于更新导致无法断言）
    @param target_list: 待筛选的数组
    @param key: 指定的key值
    @param expect: 与指定key匹配的value
    @return: 返回匹配后的数据
    """
    for i in target_list:
        goal = i.get(key)
        if str(expect) in str(goal):
            logger.info("筛选到指定数据==>{}".format(i))
            return i
    logger.info("未筛选到相应的数据！！！")
    return target_list[0]


def password_encryption(password):
    """登录密码MD5加密"""
    pwd = password + "dDSANDdsa_daoa+5asxa^2FMGFofa0asda"
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    pwd_encryption = md5.hexdigest()
    return pwd_encryption


def login_send_sms_secret():
    """发送短信验证码secret"""
    timestamp = int(time.time())
    string = "doujia" + "3" + str(timestamp) + "zhushoudDSANDdsa_daoa+5asxa^2FMGFofa0asda"
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8'))
    secret = md5.hexdigest()
    return timestamp, secret

from config import config
import datetime
import time
import re
import allure

conf = config.ConfigBase()
# ENV_UTC = int(conf.ENV_UTC)


# @allure.step("step：修改当前时间")
# def modify_time(states):
#     """修改当前时间"""
#     date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#     now_time = customize_time(custom='%H:%M:%S')
#     now_h = re.split(':', now_time)[0]
#     now_m = re.split(':', now_time)[1]
#     now_s = re.split(':', now_time)[2]
#     if states == "early":
#         now_h = int(now_h) - 1
#     elif states == "later":
#         now_h = int(now_h) + 1
#     else:
#         now_h = int(now_h)
#     change_time = date + " " + str(now_h) + ":" + now_m + ":" + now_s
#
#     return change_time


@allure.step("step：时间格式化模块")
def time_format(day="0", h="0"):
    """时间格式化模块"""
    now_time = (datetime.datetime.now() + datetime.timedelta(days=int(day)) +
                datetime.timedelta(hours=int(h))).strftime("%Y-%m-%d %H %M %S")
    data = re.split(' ', now_time)[0]
    h = re.split(' ', now_time)[1]
    m = re.split(' ', now_time)[-2]
    s = re.split(' ', now_time)[-1]
    if int(m) > 30:
        h0 = int(h) + 1
        ti0 = str(h0) + ":" + "00"
        ti1 = str(h0) + ":" + "30"
        tz = data + " " + str(h0) + ":" + "00" + ":" + "00"
        interval = ti0 + " - " + ti1
    elif int(m) == 30 and int(s) > 0:
        h0 = int(h) + 1
        ti0 = str(h0) + ":" + "00"
        ti1 = str(h0) + ":" + "30"
        tz = data + " " + str(h0) + ":" + "00" + ":" + "00"
        interval = ti0 + " - " + ti1
    else:
        h0 = int(h) + 1
        ti0 = str(h) + ":" + "30"
        ti1 = str(h0) + ":" + "00"
        tz = data + " " + str(h) + ":" + "30" + ":" + "00"
        interval = ti0 + " - " + ti1

    return tz, interval


@allure.step("step：时间修改")
def time_revise(now_time, h=0):
    """时间修改"""
    data = re.split(' ', now_time)[0]
    ti = re.split(' ', now_time)[1]
    i = ti.split(":")
    hour = int(i[0]) + h
    if int(i[1]) > 30:
        h0 = hour + 1
        ti0 = str(h0) + ":" + "00"
        ti1 = str(h0) + ":" + "30"
        tz = data + " " + str(h0) + ":" + "00" + ":" + "00"
        interval = ti0 + " - " + ti1
    elif int(i[1]) == 30 and int(i[2]) > 0:
        h0 = hour + 1
        ti0 = str(h0) + ":" + "00"
        ti1 = str(h0) + ":" + "30"
        tz = data + " " + str(h0) + ":" + "00" + ":" + "00"
        interval = ti0 + " - " + ti1
    else:
        h0 = hour + 1
        ti0 = str(hour) + ":" + "30"
        ti1 = str(h0) + ":" + "00"
        tz = data + " " + str(hour) + ":" + "30" + ":" + "00"
        interval = ti0 + " - " + ti1

    return tz, interval


# @allure.step("step：自定义时间格式")
# def customize_time(day=0, custom='%Y-%m-%d %H:%M:%S'):
#     """自定义时间格式"""
#     from datetime import timezone, datetime, timedelta
#     custom_time = ((datetime.now(timezone(timedelta(hours=+ENV_UTC)))+timedelta(days=day)).strftime(custom))
#
#     return custom_time

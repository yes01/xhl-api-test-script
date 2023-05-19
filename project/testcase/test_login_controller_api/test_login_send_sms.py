from project.modules import init_params, splicing_url
from common.request import post
from common import common
from loguru import logger
import pytest
import allure


class TestLoginSendSms:

    @allure.story('发送短信验证码')
    @allure.title("合理传参")
    @pytest.mark.parametrize("mobile, genre, app_type", [("13244848898", 2, 3)])
    def test_login_send_sms_normal(self, mobile, genre, app_type):
        data = init_params.null_data()
        logger.info('请求数据为：{}', data)
        timestamp, secret = common.login_send_sms_secret()
        path = "?mobile={}&type={}&appType={}&timeSpan={}&secret={}".format(mobile, genre, app_type, timestamp, secret)
        url = splicing_url.send_sms_login + path
        response = post(url, data, header="None")
        logger.info('响应数据为：{}', response)
        common.assert_content(response["status_code"], 200)
        common.assert_content(response["errCode"], 0)
        common.assert_content(response["errMsg"], "OK")
        common.assert_content(response["data"], None)

    @allure.story('发送短信验证码')
    @allure.title("参数异常")
    @pytest.mark.parametrize("mobile, genre, app_type", [("", 2, 3)])
    def test_login_send_sms_abnormal(self, mobile, genre, app_type):
        data = init_params.null_data()
        logger.info('请求数据为：{}', data)
        timestamp, secret = common.login_send_sms_secret()
        path = "?mobile={}&type={}&appType={}&timeSpan={}&secret={}".format(mobile, genre, app_type, timestamp, secret)
        url = splicing_url.send_sms_login + path
        response = post(url, data, header="None")
        logger.info('响应数据为：{}', response)
        common.assert_content(response["status_code"], 200)
        common.assert_content(response["errCode"], 101)
        common.assert_content(response["data"], None)
        common.assert_check_type(response["errMsg"], str)

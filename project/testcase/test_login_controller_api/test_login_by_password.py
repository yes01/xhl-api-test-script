from project.modules import init_params, splicing_url
from common.request import get
from common import common
from loguru import logger
import pytest
import allure


class TestLoginByPassword:

    @allure.story('密码登录')
    @allure.title("合理传参")
    @pytest.mark.parametrize("phone, pwd",
                             [("13120168185", "123456")])
    def test_login_by_password_normal(self, phone, pwd):
        data = init_params.null_data()
        logger.info('请求数据为：{}', data)
        pwd_encryption = common.password_encryption(pwd)
        url = splicing_url.password_login + "?mobile={}&password={}".format(phone, pwd_encryption)
        response = get(url, data, header="None")
        logger.info('响应数据为：{}', response)
        common.assert_content(response["status_code"], 200)
        common.assert_content(response["errCode"], 0)
        common.assert_content(response["errMsg"], "OK")
        common.assert_check_type(response["data"], str)

    @allure.story('密码登录')
    @allure.title("参数异常")
    @pytest.mark.parametrize('phone, pwd, exp',
                             [("", "123456", 101), ("13120168185", "2", 201)])
    def test_login_by_password_abnormal(self, phone, pwd, exp):
        data = init_params.null_data()
        logger.info('请求数据为：{}', data)
        pwd_encryption = common.password_encryption(pwd)
        url = splicing_url.password_login + "?mobile={}&password={}".format(phone, pwd_encryption)
        response = get(url, data, header="None")
        logger.info('响应数据为：{}', response)
        common.assert_content(response["status_code"], 200)
        common.assert_content(response["errCode"], exp)
        common.assert_content(response["data"], None)
        common.assert_check_type(response["errMsg"], str)

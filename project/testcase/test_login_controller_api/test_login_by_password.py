from project.modules import init_params, splicing_url
from common.request import get
from common import common
from loguru import logger
import pytest
import allure


class TestLoginByPassword:

    @allure.story('密码登录')
    @allure.title("合理传参")
    @pytest.mark.parametrize("modify_target, content",
                             [("default_parameters", "default_parameters")])
    def test_login_by_password_normal(self, modify_target, content):
        """
        @param modify_target: 需要修改的参数名称
        @param content: 修改参数的值(None—>意味不传该参数[modify_target])
        """
        data = init_params.login_by_password(modify_target, content)
        logger.info('请求数据为：{}', data)
        response = get(splicing_url.password_login, data, header="None")
        logger.info('响应数据为：{}', response)
        common.assert_content(response["status_code"], 200)
        common.assert_content(response["errCode"], 0)
        common.assert_content(response["errMsg"], "OK")
        common.assert_check_type(response["data"], str)

    # @allure.story('密码登录')
    # @allure.title("参数异常")
    # @pytest.mark.parametrize('modify_target, content',
    #                          [("user_id", None), ("user_id", "2")])
    # def test_user_info_abnormal(self, modify_target, content):
    #     """
    #     @param modify_target: 需要修改的参数名称
    #     @param content: 参数的值(None—>意味不传该参数[modify_target])
    #     """
    #     data = init_params.user_info(modify_target, content)
    #     logger.info('请求数据为：{}', data)
    #     response = get(splicing_url.org_user_info, data)
    #     logger.info('响应数据为：{}', response)
    #     common.assert_content(response["error"], 40001)
    #     common.assert_check_type(response["error_msg"], str)

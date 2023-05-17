from project.modules import init_params, splicing_url
from common.request import ecom_post
from common import common
from loguru import logger
import pytest
import allure


class TestUserInfo:

    @allure.story('获取账号')
    @allure.title("合理传参")
    @pytest.mark.parametrize("modify_target, content",
                             [("default_parameters", "default_parameters")])
    def test_user_info_normal(self, modify_target, content):
        """
        @param modify_target: 需要修改的参数名称
        @param content: 修改参数的值(None—>意味不传该参数[modify_target])
        """
        data = init_params.user_info(modify_target, content)
        logger.info('请求数据为：{}', data)
        response = ecom_post(splicing_url.org_user_info, data)
        logger.info('响应数据为：{}', response)
        common.assert_content(response["status_code"], 200)
        # common.assert_content(response["error"], 0)
        # common.assert_check_type(response["data"]["user_id"], int)
        # common.assert_check_type(response["data"]["email"], str)
        # common.assert_check_type(response["data"]["name"], str)

    # @allure.story('获取账号')
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
    #     response = ecom_post(splicing_url.org_user_info, data)
    #     logger.info('响应数据为：{}', response)
    #     common.assert_content(response["error"], 40001)
    #     common.assert_check_type(response["error_msg"], str)

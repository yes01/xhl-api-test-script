from common import common
from project.modules.time_module import *
# from common.request import *
# import os

conf = config.ConfigBase()

ENV_URL = conf.ENV_URL


def member_validate_account(modify_target, content, phone_number):
    data = {
        "account": str(phone_number)
    }
    common.modify_dictionary(data, modify_target, content)

    return data


def null_data():
    data = {
    }

    return data

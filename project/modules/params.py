from utils.total_config import Config
import uuid


conf = Config()

ENV_LANGUAGE = conf.get_env('ENV_LANGUAGE')
ENV_REGION = conf.get_env('ENV_REGION')
ENV_TOKEN = conf.get_env('ENV_TOKEN')


def common_headers():
    data = {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Bearer " + ENV_TOKEN,
        "KS-Lang": ENV_LANGUAGE,
        "KS-Region": ENV_REGION,
        "KS-Debug": "true",
        "KS-Client-Request-Id": str(uuid.uuid1())
    }
    return data

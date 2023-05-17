from utils.Yaml import Yaml

yaml = Yaml()


class ConfigBase(object):

    ENV_URL = yaml.get_yaml_config('ENV_URL')
    ENV_LANGUAGE = yaml.get_yaml_config('ENV_LANGUAGE')
    ENV_EC_APP_ID = yaml.get_yaml_config('ENV_EC_APP_ID')

from utils.Yaml import Yaml

yaml = Yaml()


class ConfigBase(object):

    ENV_URL = yaml.get_yaml_config('ENV_URL')

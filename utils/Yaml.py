import os
import yaml
from run import args

concurrency_type = ""


class Yaml:

    def __init__(self):
        pass

    @staticmethod
    def get_yaml_data(yaml_file):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Config/"
        yaml_path = os.path.join(path, yaml_file)
        file = open(yaml_path, 'r', encoding="utf-8")
        file_data = file.read()
        file.close()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data

    def write_yaml_data(self, yaml_file, yaml_key, yaml_value):
        """修改yaml文件内存在的key-value值"""
        from ruamel import yaml
        data = self.get_yaml_data(yaml_file)
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        yaml_path = os.path.join(path, yaml_file)
        data[yaml_key] = yaml_value
        file = open(yaml_path, 'w', encoding='utf-8')
        yaml.dump(data, file, Dumper=yaml.RoundTripDumper, allow_unicode=True)
        file.close()

    def get_yaml_config(self, data):
        global concurrency_type
        conditions = [isinstance(args.env, str), args.n is None]
        if all(conditions):
            file_name = args.env
        else:
            file_name = "uat-env"
            concurrency_type = "xdist"
        config_dict = {"uat-env": "env.yaml"}
        conf_filename = config_dict[file_name]
        detail = self.get_yaml_data(conf_filename)
        env = file_name.split("-")[0]
        data_diction = detail[env][data]
        region_diction = "" if data_diction is None else data_diction
        return region_diction

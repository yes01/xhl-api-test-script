from config.config import ConfigBase
import os


class Config(ConfigBase):

    @staticmethod
    def get_env(key):

        return os.getenv(key)

    def get_config(self):
        pass

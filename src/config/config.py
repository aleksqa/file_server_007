import configparser

from src.utils import Singleton


class Config(metaclass=Singleton):
    SIGNATURES_SECTION = "Signature"

    def __init__(self):
        self.confid_data = None

    def load(self, filename):
        self.confid_data = configparser.ConfigParser()
        self.confid_data.read(filename)

    def signature_algo(self) -> str:
        default_value = "md5"
        if Config.SIGNATURES_SECTION not in self.confid_data:
            return default_value
        section = self.confid_data[Config.SIGNATURES_SECTION]
        if 'signature_algo' not in section:
            return default_value
        algo = section['signature_algo']
        return algo

    def signatures_dirs(self) -> str:
        pass

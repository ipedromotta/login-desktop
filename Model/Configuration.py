from configparser import ConfigParser

class Configuration:
    config = ConfigParser()
    config.read(".editorconfig")

    __host = config["Database"]["Host"]
    __user = config["Database"]["User"]
    __password = config["Database"]["Password"]
    __database = config["Database"]["Database"]

    __log_level = config["Log"]["Level"]

    @property
    def database(self):
        return (self.__host, self.__database, self.__user, self.__password)
    
    @property
    def log_level(self):
        return int(self.__log_level)
    
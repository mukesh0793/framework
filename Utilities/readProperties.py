import configparser
config=configparser.RawConfigParser()
config.read(r".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get("commoninfo","baseURL")
        return url

    @staticmethod
    def getUserMail():
        username=config.get("commoninfo","useremail")
        return username

    @staticmethod
    def getPassword():
        password = config.get("commoninfo", "password")
        return password

    # .\\Configurations\\ConFig.ini

    # ../ Configurations / config.ini
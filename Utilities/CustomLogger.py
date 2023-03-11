import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig( filename="../Log/automation.log",
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            # datefmt="%m/%d/%y %I:%M:%S %P",
                            level=logging.DEBUG
                            )
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



#
# def loggen():
#     logging.basicConfig(filename="../Log/automation.log",
#                         format="%(asctime)s:%(levelname)s:%(message)s",
#                         level=logging.DEBUG
#                         )
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)
#     return logger

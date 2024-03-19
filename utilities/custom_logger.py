import logging
class LogGen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename='/Users/syanspsingh/Documents/Pycharm/Democrance/logs/automation.log',level=logging.INFO, force=True,filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%d|%m|%Y  %I:%M:/%S %p')
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        return logger
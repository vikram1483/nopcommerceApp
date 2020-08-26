# Log File creation and format of the logs is done in the customLogger.py
# But logging entries is done in the test case

import logging

class LogGen:
    # We will make this a static method so that it can be called using class itself.
    @staticmethod
    def loggen():
    # In the basicConfig() we have to pass the filename,format and datefmt arguments
        logging.basicConfig(filename=".\\Logs_Data\\automation.log",
                            format='%(asctime)s: %(levelname)s : %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


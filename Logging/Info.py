import logging


class info:
    # logging.basicConfig(filename='/home/shubhampanchal/logging.txt', format='%(asctime)s  %(name)s  %(levelname)s: %(message)s', level=logging.DEBUG)
    # print('Start')
    # logging.debug("This is debug message")
    # logging.info("This is info message")
    # logging.warning("This is warning message")
    # logging.error("This is error message")
    # logging.critical("This is critical message")
    # print('Complete')

    print('Start')
    logger = logging.getLogger('dev')
    logger.setLevel(logging.DEBUG)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)

    logger.addHandler(consoleHandler)

    formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
    consoleHandler.setFormatter(formatter)
    logging.debug("This is debug message")
    logging.info("This is info message")
    logging.warning("This is warning message")
    logging.error("This is error message")
    logging.critical("This is critical message")
    print('Complete')


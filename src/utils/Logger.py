import logging
import os
import traceback


class Logger:

    @staticmethod
    def __set_logger():
        log_directory = os.path.join('src', 'utils', 'log')
        log_filename = 'app.log'

        # Crear el directorio si no existe
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        log_path = os.path.join(log_directory, log_filename)
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # Crear el formatter y añadirlo al handler
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        # Asegurarse de que no hay handlers duplicados
        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(file_handler)

        return logger

    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger()

            if level == "critical":
                logger.critical(message)
            elif level == "debug":
                logger.debug(message)
            elif level == "error":
                logger.error(message)
            elif level == "info":
                logger.info(message)
            elif level == "warn":
                logger.warning(message)
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)

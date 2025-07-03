from src.logger import logger

class AddCommand:
    @staticmethod
    def execute(a, b):
        result = a + b
        logger.info(f"Adding {a} + {b} = {result}")
        return result


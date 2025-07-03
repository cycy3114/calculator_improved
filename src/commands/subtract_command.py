from src.logger import logger

class SubtractCommand:
    @staticmethod
    def execute(a, b):
        result = a - b
        logger.info(f"Subtracting {a} - {b} = {result}")
        return result

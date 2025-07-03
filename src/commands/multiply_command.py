from src.logger import logger

class MultiplyCommand:
    @staticmethod
    def execute(a, b):
        result = a * b
        logger.info(f"Multiplying {a} * {b} = {result}")
        return result

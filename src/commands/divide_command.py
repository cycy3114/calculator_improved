from src.logger import logger

class DivideCommand:
    @staticmethod
    def execute(a, b):
        if b == 0:
            logger.error("Attempted division by zero")
            raise ValueError("Cannot divide by zero.")
        result = a / b
        logger.info(f"Dividing {a} / {b} = {result}")
        return result

from src.logger import logger


class HistoryCommand:
    @staticmethod
    def execute():
        logger.info("User requested to show calculation history.")
        return "History feature not yet implemented."

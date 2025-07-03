from src.logger import logger

class ShowHistoryCommand:
    @staticmethod
    def execute():
        logger.info("User requested to show history from logger.")
        return "Show history feature not yet implemented."


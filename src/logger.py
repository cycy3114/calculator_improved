import logging
from dotenv import load_dotenv
import os

load_dotenv()

log_file = os.getenv("LOG_FILE", "logs/app.log")
log_level = os.getenv("LOG_LEVEL", "INFO").upper()

os.makedirs(os.path.dirname(log_file), exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level=getattr(logging, log_level),
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

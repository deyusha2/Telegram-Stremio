from datetime import datetime
from logging import ERROR, INFO, Formatter, StreamHandler, basicConfig, getLogger

import pytz

IST = pytz.timezone("Asia/Kolkata")


# ----- Formatter that renders timestamps in IST
class ISTFormatter(Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, IST)
        return dt.strftime(datefmt or "%d-%b-%y %I:%M:%S %p")


# ----- Root logging configuration
formatter = ISTFormatter("[%(asctime)s] [%(levelname)s] - %(message)s", "%d-%b-%y %I:%M:%S %p")

# StreamHandler outputs to standard output (console), which Vercel captures in its Logs tab.
stream_handler = StreamHandler()
stream_handler.setFormatter(formatter)

# Removed FileHandler("log.txt") to prevent read-only filesystem crash on Vercel
basicConfig(handlers=[stream_handler], level=INFO)

getLogger("httpx").setLevel(ERROR)
getLogger("pyrogram").setLevel(ERROR)
getLogger("fastapi").setLevel(ERROR)

LOGGER = getLogger(__name__)
LOGGER.setLevel(INFO)
LOGGER.info("Logger initialized with IST timezone.")

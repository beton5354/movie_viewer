from os import getenv

from dotenv import load_dotenv

load_dotenv()

SQL_URL = getenv("SQL_URL")

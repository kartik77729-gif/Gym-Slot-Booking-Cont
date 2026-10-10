import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT", "4000")
dbname = os.getenv("DB_NAME")

safe_user = urllib.parse.quote_plus(user) if user else ""
safe_password = urllib.parse.quote_plus(password) if password else ""

db_uri = f"mysql+pymysql://{safe_user}:{safe_password}@{host}:{port}/{dbname}?charset=utf8mb4"

engine = create_engine(
    db_uri,
    connect_args={
        "ssl": {
            "ssl_mode": "VERIFY_IDENTITY"
        }
    }
)
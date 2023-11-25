from sqlalchemy import create_engine,MetaData

SQLALCHEMY_DATABASE_URL = "sqlite:///./Northwin.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
conn = engine.connect()
meta = MetaData()

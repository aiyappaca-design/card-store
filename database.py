from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "your_supabase_connection_string"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
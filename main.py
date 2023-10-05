
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from cli import cli

DATABASE_URL = "sqlite:///contact_book.db"  # Use SQLite for simplicity, you can switch to other databases later

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    cli()

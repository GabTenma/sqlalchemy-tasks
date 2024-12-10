import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Date, Float, Integer, CheckConstraint
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
import datetime

load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

# BEGIN (write your solution here)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(256), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(128), nullable=False)
    published_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    pages: Mapped[int] = mapped_column(Integer, nullable=False)
    genre: Mapped[str] = mapped_column(String(64), nullable=False)
    rating: Mapped[float] = mapped_column(Float, CheckConstraint('rating >= 0 AND rating <= 10'))
# END
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

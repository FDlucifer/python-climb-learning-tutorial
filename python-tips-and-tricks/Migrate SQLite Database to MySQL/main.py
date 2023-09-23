# pip install SQLAlchemy

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    birth_date = Column(Date)
    bio = Column(String(255))


class Publisher(Base):
    __tablename__ = "publishers"
    publisher_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255))
    website = Column(String(255))


class Genre(Base):
    __tablename__ = "genres"
    genre_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)


class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.author_id"))
    publisher_id = Column(Integer, ForeignKey("publishers.publisher_id"))
    genre_id = Column(Integer, ForeignKey("genres.genre_id"))
    publication_date = Column(Date)
    summary = Column(Date)
    isbn = Column(String(255), unique=True)


class Patron(Base):
    __tablename__ = "patrons"
    patron_id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    registered_date = Column(Date, default="CURRENT_DATE")


class Checkout(Base):
    __tablename__ = "checkouts"
    checkout_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.book_id"))
    patron_id = Column(Integer, ForeignKey("patrons.patron_id"))
    checkout_date = Column(Date, default="CURRENT_DATE")
    due_date = Column(Date)
    return_date = Column(Date)


class BookAuthor(Base):
    __tablename__ = "book_authors"
    book_id = Column(Integer, ForeignKey("books.book_id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("authors.author_id"), primary_key=True)


sqlite_engine = create_engine("sqlite:///library.db")
mysql_engine = create_engine("mysql+pymysql://root:password@localhost:3306/librarydb")

SQLite_session = sessionmaker(bind=sqlite_engine)
sqlite_session = SQLite_session()

MYsql_session = sessionmaker(bind=mysql_engine)
mysql_session = MYsql_session()

Base.metadata.create_all(mysql_engine)

for table in [Author, Publisher, Genre, Book, Patron, Checkout, BookAuthor]:
    records = sqlite_session.query(table).all()
    for record in records:
        mysql_session.merge(record)

mysql_session.commit()
sqlite_session.close()
mysql_session.close()

from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from fastapi import FastAPI, Depends, HTTPException
from typing import Generator, List, Optional
from schemas import BookCreate, BookResponse

Base = declarative_base()
engine = create_engine('sqlite:///bookTable.db', connect_args={"check_same_thread": False})

class Book(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256), nullable=False)
    author = Column(String(256), nullable=False)
    year = Column(Integer, nullable=True)

Base.metadata.create_all(engine)

SessionFactory = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db() -> Generator[Session, None, None]:
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

@app.post("/books/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    book_row = Book(title=book.title, author=book.author, year=book.year)
    db.add(book_row)
    db.commit()
    db.refresh(book_row)
    return book_row

@app.get("/books/", response_model=List[BookResponse])
def read_all_books(db: Session = Depends(get_db)):
    return db.scalars(select(Book)).all()

@app.delete("/books/{book_id}", status_code=204)
def delete_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book_entity = db.scalars(select(Book).where(Book.id == book_id)).first()
    if not book_entity:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
    db.delete(book_entity)
    db.commit()
    return None

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    book_entity = db.scalars(select(Book).where(Book.id == book_id)).first()
    if not book_entity:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

    book_entity.title = book.title
    book_entity.author = book.author
    book_entity.year = book.year

    db.commit()
    db.refresh(book_entity)

    return book_entity

@app.get("/books/search/", response_model=List[BookResponse])
def read_books_with_params(
    author: Optional[str] = None,
    title: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = select(Book)

    if author:
        query = query.where(Book.author == author)
    if title:
        query = query.where(Book.title == title)
    if year:
        query = query.where(Book.year == year)

    return db.scalars(query).all()

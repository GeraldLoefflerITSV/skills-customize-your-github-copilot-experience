from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Building REST APIs with FastAPI")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int | None = None


class Book(BookCreate):
    id: int


books: list[Book] = []
next_book_id = 1


@app.get("/health")
def health_check():
    # TODO: return a simple status response.
    pass


@app.get("/books")
def list_books():
    # TODO: return the list of books.
    pass


@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    # TODO: create a new book, assign it an id, and add it to books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: find a book by id or raise HTTPException(status_code=404, ...).
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    # TODO: update an existing book and return the updated record.
    pass


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    # TODO: delete the book with the matching id.
    pass
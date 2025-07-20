import json
from typing import Any, List
import httpx
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel

# Initialize FastMCP server
mcp = FastMCP("books")

class Book(BaseModel):
    title: str
    author: str
    year: int

books_file = "books.json"

def load_books():
    try:
        with open(books_file, "r") as f:
            books_data = json.load(f)
            return [Book(**book) for book in books_data]
    except FileNotFoundError:
        return []

def save_books(books: List[Book]):
    with open(books_file, "w") as f:
        # Convert Book objects to dictionaries before saving
        books_data = [book.model_dump() for book in books]
        json.dump(books_data, f, indent=2)


@mcp.tool()
async def get_books() -> List[Book]:
    """Get all books."""
    return load_books()

@mcp.tool()
async def add_book(book: Book) -> Book:
    """Add a new book."""
    books = load_books()
    books.append(book)
    save_books(books)
    return book

@mcp.tool()
async def remove_book(book: Book) -> Book:
    """Remove a book."""
    books = load_books()
    # Find book by title, author, and year
    books = [b for b in books if not (b.title == book.title and b.author == book.author and b.year == book.year)]
    save_books(books)
    return book

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='streamable_http')









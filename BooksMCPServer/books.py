import json
from typing import Any
import httpx

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("books")

books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
]

@mcp.tool()
async def get_books(query: str) -> str:
    """Get books from the library."""
    return json.dumps(books, indent=2)

@mcp.tool()
async def add_book(title: str, author: str, year: int) -> str:
    """Add a book to the library."""
    books.append({
        "title": title,
        "author": author,
        "year": year
    })
    return "Book added successfully"

@mcp.tool()
async def remove_book(title: str) -> str:
    """Remove a book from the library."""
    global books
    books = [book for book in books if book["title"] != title]
    return "Book removed successfully"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')









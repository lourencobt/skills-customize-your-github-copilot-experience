"""
FastAPI REST API - Book Management System
Starter Code for Students

This file provides the basic structure to get you started.
Complete the TODOs to build a fully functional REST API.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# TODO: Create the FastAPI app instance
app = None

# TODO: Create a Pydantic model for Book
# Include fields: id (int), title (str), author (str), year (int), genre (str)
class Book(BaseModel):
    pass

# In-memory storage for books (use a list)
books_db: List[Book] = []

# TODO: Create a GET endpoint at "/" that returns a welcome message
@app.get("/")
async def root():
    pass

# TODO: Create a GET endpoint at "/health" that returns API status
@app.get("/health")
async def health_check():
    pass

# TODO: Create a POST endpoint at "/books" to add a new book
# Remember to return status code 201 for created resources
@app.post("/books", status_code=201)
async def create_book(book: Book):
    pass

# TODO: Create a GET endpoint at "/books" to retrieve all books
@app.get("/books")
async def get_all_books():
    pass

# TODO: Create a GET endpoint at "/books/{book_id}" to get a specific book
# Raise HTTPException with status code 404 if book not found
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    pass

# TODO: Create a PUT endpoint at "/books/{book_id}" to update a book
# Raise HTTPException with status code 404 if book not found
@app.put("/books/{book_id}")
async def update_book(book_id: int, updated_book: Book):
    pass

# TODO: Create a DELETE endpoint at "/books/{book_id}" to delete a book
# Raise HTTPException with status code 404 if book not found
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    pass


# To run this application:
# 1. Install FastAPI and uvicorn: pip install fastapi uvicorn
# 2. Run the server: uvicorn starter-code:app --reload
# 3. Visit http://127.0.0.1:8000/docs to see the interactive API documentation

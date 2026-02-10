# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework to manage a collection of books. You'll learn how to create endpoints, handle different HTTP methods, validate data, and implement CRUD operations.

## 📝 Tasks

### 🛠️	Task 1: Set Up FastAPI Application

#### Description
Create the foundation of your FastAPI application by setting up the main app instance and creating a simple health check endpoint to verify your API is working.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Create a GET endpoint at `/` that returns a welcome message
- Create a GET endpoint at `/health` that returns the API status
- Use proper response models with status codes


### 🛠️	Task 2: Implement Book Management Endpoints

#### Description
Build a complete CRUD (Create, Read, Update, Delete) API for managing a book collection. Use Pydantic models for data validation and maintain an in-memory list to store the books.

#### Requirements
Completed program should:

- Create a Pydantic model for Book with fields: id, title, author, year, and genre
- Implement POST `/books` endpoint to add a new book
- Implement GET `/books` endpoint to retrieve all books
- Implement GET `/books/{book_id}` endpoint to retrieve a specific book by ID
- Implement PUT `/books/{book_id}` endpoint to update book information
- Implement DELETE `/books/{book_id}` endpoint to remove a book
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Handle edge cases like book not found with proper error messages

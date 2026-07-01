# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI and practice the core pieces of a modern web backend: routes, request validation, response models, and basic CRUD behavior.

## 📝 Tasks

### 🛠️ Create the API Foundation

#### Description
Set up a FastAPI application with a simple health check endpoint and an endpoint that returns an empty collection of resources.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Add a `GET /health` route that returns a JSON status message
- Add a `GET /books` route that returns a list of books
- Start with an empty in-memory collection


### 🛠️ Add Create and Read Operations

#### Description
Define a Pydantic model for a book and implement the routes needed to create a new book and fetch one book by its ID.

#### Requirements
Completed program should:

- Use a Pydantic model to validate book data
- Add a `POST /books` route that creates a new book
- Assign each book a unique ID
- Add a `GET /books/{book_id}` route that returns one book
- Return a clear `404` error when a book is not found


### 🛠️ Complete CRUD Behavior

#### Description
Finish the API by adding routes to update and delete books so the collection can be managed end to end.

#### Requirements
Completed program should:

- Add a `PUT /books/{book_id}` route to update an existing book
- Add a `DELETE /books/{book_id}` route to remove a book
- Keep all data in memory for this assignment
- Make sure the generated FastAPI documentation at `/docs` shows the routes and schemas clearly

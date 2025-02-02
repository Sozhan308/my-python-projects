# Problem Statement: Simple HTTP API Server for Book Management

## Objective
Implement a simple HTTP API server in Python that allows users to store and retrieve book information using the `GET` and `POST` methods. The server should be able to handle basic CRUD (Create, Read) operations for managing a collection of books.


# Book API

A simple REST API to manage books using a lightweight Python web framework like Flask or FastAPI.

## Requirements

- **Python 3.x**
- Flask or FastAPI
- pytest for testing
- A tool like `curl` or Postman for interacting with the API

## Features

- **POST /books**: Create a new book in the collection.
- **GET /books**: Retrieve a list of all books.
- **GET /books/{id}**: Retrieve a specific book by its ID.
- **Error Handling**: Gracefully handle invalid requests and missing fields.

## API Endpoints

### 1. POST /books

Creates a new book in the collection.

#### Request Body
```json
{
  "title": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "year": 1960,
  "genre": "Fiction"
}
```

---

## Functional Requirements

### Book Data Structure
Each book should have the following attributes:
- `id` (unique identifier, auto-generated)
- `title` (string, required)
- `author` (string, required)
- `year` (integer, optional)
- `genre` (string, optional)

---

### Endpoints
Implement the following API endpoints:

#### 1. **POST /books**

- Adds a new book to the collection.
- **Request Body**: JSON object containing `title`, `author`, `year`, and `genre`.

```json
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genre": "Fiction"
  }
``` 

#### 2. **GET /books**

- Retrieves a list of all books in the collection.

- Response: Returns a JSON array of all books.

```json
[
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genre": "Fiction"
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genre": "Dystopian"
  }
]
```

#### 3. **GET /books/{id}**

- Retrieves details of a specific book by its id.

- Response: Returns the book details as a JSON object.

```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925,
  "genre": "Fiction"
}
```

If the book is not found, return a 404 Not Found status with an appropriate error message.

### Error Handling

#### Handle invalid requests gracefully:

- If required fields (title, author) are missing in a POST request, return a 400 Bad Request status with an error message.

- If a book with the specified id does not exist, return a 404 Not Found status.

- If the request body is not valid JSON, return a 400 Bad Request status.

#### Data Storage

- Use an in-memory data structure (e.g., a list or dictionary) to store the books. Persistence to a database or file is not required.

#### Server

- Use a lightweight Python web framework like Flask or FastAPI to implement the server.

- The server should run on localhost and listen on port 5000.

#### Non-Functional Requirements

###### Code Quality

- Write clean, modular, and well-documented code.

- Use appropriate data validation and error handling.

#### Testing

- Include unit tests for the API endpoints using a testing framework like pytest.

**Test cases should cover**:

- Successful creation of a book.

- Retrieval of all books.

- Retrieval of a specific book by id.

- Error scenarios (e.g., missing fields, invalid JSON, non-existent book).

#### Scalability

- Ensure the server can handle multiple concurrent requests efficiently.

#### Security

- Validate and sanitize input data to prevent injection attacks or malformed requests.

#### Example Workflow

- Start the server.

- Use a tool like curl, Postman, or a browser to interact with the API.

- Add a book using POST /books:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "title": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "year": 1960,
  "genre": "Fiction"
}' http://localhost:5000/books
```

##### Retrieve all books using GET /books:

```bash
curl http://localhost:5000/books
```

##### Retrieve a specific book using GET /books/{id}:

```bash
curl http://localhost:5000/books/1
```

#### Deliverables

- Source code for the HTTP server.

- Unit tests for the API endpoints.

- A README.md file with instructions on how to set up and run the server.
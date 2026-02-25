```markdown
# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a simple RESTful API using the FastAPI framework. You will build a small API that supports creating, reading, and listing resources and run it locally with `uvicorn`.

## 📝 Tasks

### 🛠️ Task 1 — Implement the API

#### Description
Use the starter code to implement endpoints for listing items, retrieving a single item by id, and creating new items. Keep the data in memory (a Python list or dict) for simplicity.

#### Requirements
Completed program should:

- Provide a GET endpoint to list all items
- Provide a GET endpoint to retrieve a single item by id (return 404 if not found)
- Provide a POST endpoint to create a new item (accept JSON, return created item with id)
- Validate request payloads using Pydantic models
- Return appropriate HTTP status codes

### 🛠️ Task 2 — Optional stretch goals

#### Description
Add extra features to practice more FastAPI concepts.

#### Requirements (examples)

- Add PUT/PATCH and DELETE endpoints
- Add query parameters for filtering or pagination
- Add simple authentication (API key) for write endpoints
- Return OpenAPI schema docs and test them via Swagger UI

## ✅ Learning Outcomes

- Build and run a FastAPI application
- Define request/response models with Pydantic
- Use HTTP methods and status codes correctly
- Explore automatic API docs (Swagger, ReDoc)

## ⚙️ Prerequisites

- Python 3.8+
- `pip` available to install dependencies

## 📁 Starter files

- `main.py` — starter FastAPI application with scaffolding
- `requirements.txt` — dependencies to install

## ▶️ How to run

Install dependencies and start the app:

```bash
python3 -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to view Swagger UI.

## ⏱️ Estimated time

90–150 minutes for base tasks; more for stretch goals.

## ❓ Help & Submission

If you need help, include the endpoint code and error traces when asking. Submit your final `main.py` file.

```

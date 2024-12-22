# Project Title

E-library API system

# Project  Description
This is an E-library API system. It allows the following operations:

Users
users can sign up, edit their profile, delete their profile, partially update their profile, borrow books and return books. A user can only borrow a book if they are active and if the  book is available. All users can be viewed and a single user can be viewed by their ID

Books
books can be created, fully updated, partially updated, deleted and deactivated. All books can be viewed and a single book can be viewed by its ID.

Borrow operations
Books can be borrowed, returned, borrow record for a user can be viewed, all borrow records can be viewed and books that are yet to be returned can be viewed.

# Entities
The system includes the following entities:
1. User entities
```
  User: Represents a user of the library
  users: Represents all users of the library
  user_id: Unique identifier for the user
  name: Name of the user
  email: Email address of the user
  is_active: Indicates if the user account is active (default value = True)
```
2. Book entities
```
  Book: Represents a book in the library
  books: Represents all books in a library
  book_id: Unique identifier for a book in the library.
  title: Title  of the book
  author: Namme of the books' author
  is_available: Indicates if the book is available (default value = True)
```
3. Borrow entities
```
  Borrow-record: Represents a borrow record
  id: Represents the borrow record id
  borrow_date: Represents the date that the book was borrowed
  return_date: Represents the date that the book was returned
  borrow_records: Represents all the borrow_record
```


## Authors

- [@Minabade](https://www.github.com/Minabade)


## Getting started

Prerequisites

Python 3.8 or later.

A virtual environment.

Required Python libraries (specified in requirements.txt).
## Installation

Install my-project by:
1. forking the repository: https://github.com/Minabade/E-Library-API-System 
2. clone the the repository with 

```bash
  git clone "forked repository url"
 
```
3. Navigate to the project repository:
```bash
    cd e-library-api
   
```
4. Create and activate a virtual environment:
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```
5. Install dependencies:
```bash
    pip install -r requirements.txt
```
 
## Usage/Examples

Examples of API Requests

1. Create a User

  POST /users/signup
```
  {
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  }
```
2. Borrow a Book

  POST /borrow_records/{user_id}/borrow_book
```
  {
    "user_id": "b5341c10-2d99-4d4c-a34f-39d80f98a7a2",
    "title": "Pride and Prejudice",
    "author": "Jane Austen"
  }
```
3. Return a Book

Patch /borrow_records/{borrow_id}/return_book

```
{
  "borrow_id": 1
}
```
## Running Tests
Using pytest:

1. Ensure pytest is installed:

```bash
  pip install pytest
```

2. Run the tests:
```
pytest
```

3. View the test results in the terminal. Pytest will automatically discover and run all test files named ```test_*.py```.

## Contributing

Contributions are always welcome!

To contribute:

Fork the repository.

Create a feature branch.

Commit your changes.

Submit a pull request.


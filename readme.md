### Django REST API Setup
This repository contains a Django project with a RESTful API using Django REST Framework.

#### Prerequisites
- Python (version 3.x recommended)
- Django
- Django REST Framework
### Setup Instructions
#### Create a Virtual Environment:
- python -m virtualenv environment_name
#### Activate Virtual Environment:
- cd environmentname/Scripts
- activate
#### Install Dependencies:
- pip install django
- pip install djangorestframework
#### Set up a new project with a single application
- django-admin startproject book_management
- cd book_management
- django-admin startapp api
#### Database migration
- python manage.py makemigrations
- python manage.py migrate
#### Run the Program
- python manage.py runserver
#### how to run a api endpoint:
- first we need to make sure that we migrated the models to database
- then we need to start the server using "python manage.py runserver" command.
- then we need to open another cmd prompt and open virtual environment and activate then open the project folder and provide curl commands.
- make sure Your server is runnig in another cmd prompt
#### Register a User 
- curl -X POST -d "username=your_superuser_username&email=your_email&password=your_password" http://localhost:8000/api/register/
#### Token Generate with login
- curl -X POST -d "username=your_username&password=your_password" http://localhost:8000/api/login/
### Testing or Using the API endpoints.
- we can test API endpoints using curl commands.
#### Create a Books:
#### using curl:
- curl -H "Authorization: Token enter_generated_token" -X POST http://127.0.0.1:8000/api/books/ -d "title=title_name&author=author_name&genre=enter_genre&publication_date=enter_date&description=enter_description"
#### About this API endpoint:
- here this endpoint is used to create a books by providing the books details.
#### List all Books details:
- using curl:
- curl -H "Authorization: Token your-generated-token" http://127.0.0.1:8000/api/books/
#### About this API endpoint:
- here this endpoint is used to get the details of all books.
#### Retrieve a specific book's details:
- using curl:
- curl -H "Authorization: Token your-generated-token" http://127.0.0.1:8000/api/books/{book_id}/
#### About this API endpoint:
- here this endpoint is used to get the details of books with book_id which was mentioned in the command.
### Update a book's details:
#### using curl:
#### PUT method:
- curl -H "Authorization: Token enter_generated_token" -X POST http://127.0.0.1:8000/api/books/{books_id}/ -d "title=title_name&author=author_name&genre=enter_genre&publication_date=enter_date&description=enter_description"
#### PATCH method:
- curl -H "Authorization: Token your-generated-token" -X PATCH http://127.0.0.1:8000/api/books/{book_id}/ -d "title=Updated title Name"
#### About this API endpoint:
- here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a primary key in the model the PUT method works as POST method (which means it creates a new books with given details). The PATCH method is used to update the book's details except books's id. here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.
#### Delete a book:
- using curl:
- curl -H "Authorization: your-generated-token" -X DELETE http://127.0.0.1:8000/api/books/{book_id}/
#### About this API endpoint:
- here this endpoint is used to delete the book with given book_id.
#### Create a Reading list:
- using curl:
- curl -H "Authorization: Token your-generated-token" -X POST http://127.0.0.1:8000/api/reading-lists/ -d "user=_enter_user_id"
#### About this API endpoint:
- here this endpoint is used to create a reading_list with given details.
#### reading list details:
- using curl:
- curl -H "Authorization: Token your-generated-token" http://127.0.0.1:8000/api/reading-lists/{reading_list_id}/
#### About this API endpoint:
- here this endpoint is used to get the details of all reading lists.
#### add a book to reading list
- curl -H "Authorization: Token your-generated-token" -X POST http://127.0.0.1:8000/api/reading-lists/{reading_list_id}/add-book/ -d "book_id=enter_book_id&order=enter_order"
#### Delete a book to reading list:
- using curl:
- curl -H "Authorization: Token your-generated-token" -X DELETE http://127.0.0.1:8000/api/reading-lists/{reading_list_id}/remove-book/


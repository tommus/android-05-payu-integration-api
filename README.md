# iShelf API

iShelf API for PayU Integration Sample.

## Features

1. Administration panel
2. Browsable API
3. Swagger documentation
4. Basic authentication
5. Permissions
6. Pagination
7. Sample CRUD endpoints
8. Localization

## Backend management

1. Create virtual environment:

    > virtualenv .venv -p python3

2. Activate virtual environment:

    > source .venv/bin/activate

3. Install requirements

    > pip install -r requirements.txt

## Database synchronization

1. When executing server for the first time, you have to synchronize database (and execute migrations):

    > python manage.py migrate

2. Load sample data:

    > python manage.py loaddata quickstart_authors

    > python manage.py loaddata quickstart_books

## Running server

1. Make sure the virtual environment has been activated:

    > source .venv/bin/activate

2. Start server by typing:

    > python manage.py runserver \<address\>:\<port\>

- I.e. start server at port 8000 to listen for connections from whatever source:

    > python manage.py runserver 0.0.0.0:8000

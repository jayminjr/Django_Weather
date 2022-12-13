# Weather Project

## Steps to run project :

1. open project folder in terminal

2. create virtual env
    `python -m virtualenv venv`
3. Run virtualenv 
    `venv\Scripts\activate`
4. Install requirements 
    `pip install -r requirements.txt`
5. Perform makemigrations and migrate
    `python manage.py seed`
6. Run server 
    `python manage.py runserver`
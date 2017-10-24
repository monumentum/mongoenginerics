# MongoEnginerics
A wrapper for python webframeworks to create basic CRUD resources to you api based on Mongoengine Documents :)

# How install
> clone it
> pip install -e .

# Example
OBS: Only for apistar using WSGIApp

Model File
```python
from mongoengine import Document, StringField, DateTimeField

class User(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(max_length=50)
    birth_date = DateTimeField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True, max_length=20, min_length=8)
```

Controller File
```python
from mongoenginerics import Controller
from .model import User

class UserController(Controller):
    name = 'user'
    model = User
```

App File
```python
from mongoenginerics import ApistarWSGIAdapter
from mypack.user.controller import UserController

menginerics = ApistarWSGIAdapter(database='test_apistar')
menginerics.add_controller(UserController)

app = menginerics.get_app()

if __name__ == 'main':
    app.run()
```


# Contributing


### Setup Environment

- fork this project
- setup [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)
- create a virtualenv (`mkvirtualenv mongoenginerics`)
- install dependencies: `make install`

from . import adapter
from mongoengine import connect

class App():
    _controllers = []

    def __init__(self, engine, database=''):
        self._connection = connect(database)
        self.engine = engine

    def add_controller(self, ctrl):
        self._controllers.append(ctrl)

    def run(self):
       return adapter.run(self)
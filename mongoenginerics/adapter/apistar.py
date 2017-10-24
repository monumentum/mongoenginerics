import importlib
import json
from .base import MongoEnginericsAdapter

class ApistarWSGIAdapter(MongoEnginericsAdapter):
    def __init__(self, *args, **kwargs):
        self.engine = importlib.import_module('apistar')
        self._wsgi = importlib.import_module('apistar.frameworks.wsgi')
        super(ApistarWSGIAdapter, self).__init__(*args, **kwargs)

    def attach(self, ctrl):
        def find(query: self.engine.http.QueryParams):
            return ctrl.find(query)

        def update(item_id, updates: self.engine.http.Body):
            return ctrl.update(item_id, json.loads(updates))

        def create(body: self.engine.http.Body):
            return ctrl.create(json.loads(body))

        def find_one(item_id):
            return ctrl.find_one(item_id)

        def delete(item_id):
            return ctrl.delete(item_id)

        return self.engine.Include('/{}'.format(ctrl.name), [
            self.engine.Route('/', 'GET', find),
            self.engine.Route('/', 'POST', create),
            self.engine.Route('/{item_id}', 'GET', find_one),
            self.engine.Route('/{item_id}', 'PUT', update),
            self.engine.Route('/{item_id}', 'DELETE', delete),
        ])

    def get_app(self):
        routes = [self.attach(ctrl()) for ctrl in self._controllers]
        return self._wsgi.WSGIApp(routes=routes)
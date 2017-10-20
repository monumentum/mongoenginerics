class ApiStarAdapter():
    _handles = []

    def __init__(self, app):
        self.engine = app.engine

    def attach(self, ctrl):
        def update(item_id, updates: self.engine.http.Body):
            return ctrl.update(item_id, updates)

        def find(query: self.engine.http.QueryParams):
            return ctrl.find(query)

        def create(body: self.engine.http.Body):
            return ctrl.create(body)

        self._handles.append(
            self.engine.Include('/{}'.format(ctrl.name), [
                self.engine.Route('/', 'GET', find),
                self.engine.Route('/', 'POST', create),
                self.engine.Route('/{item_id}', 'GET', ctrl.find_one),
                self.engine.Route('/{item_id}', 'PUT', update),
                self.engine.Route('/{item_id}', 'DELETE', ctrl.delete),
            ])
        )

    def mount_app(self):
        routes = []

        for handle in self._handles:
            routes.append(handle)

        self.app = self.engine.App(routes=routes)

    def run(self):
        self.app.run()
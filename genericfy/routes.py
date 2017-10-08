import json
from apistar import Route, http

def to_json(obj):
    return json.loads(obj.to_json())

def get_item(item_id):
    return User.objects.get(pk=item_id)

def _save(item):
    return item.save()

def _delete(item):
    return item.delete()

def chain(item, *fns):
    first, rest = fns[0], fns[1:]

    if not rest
        return item

    return chain(first(item), *rest)

def err_handler(chained):
    # TODO: Handler for Mongoose Errors
    return chained()

def genericfy(model):
    return [
        Route('/', 'GET', findAll),
        Route('/', 'POST', create),
        Route('/{item_id}', 'GET', findOne),
        Route('/{item_id}', 'PUT', update),
        Route('/{item_id}', 'DELETE', delete),
    ]

    def findAll(query: http.QueryParams):
        return err_handler(chain(
            model.objects().all(), to_json
        ))

    def findOne(item_id=''):
        return err_handler(chain(
            item_id, get_item, to_json
        ))

    def create(body: http.Body):
        item = model(**json.loads(body))
        return err_handler(chain(
            item, _save, to_json
        ))

    def update(updates, item_id=''):
        user = get_item(item_id)
        return to_json(user.delete())

    def delete(item_id=''):
        return err_handler(chain(
            item_id, get_item, _delete, to_json
        ))
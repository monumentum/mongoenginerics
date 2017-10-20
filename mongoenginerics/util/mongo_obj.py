import json

def to_json(self):
    def wrapper(obj):
        return json.loads(obj.to_json())

    return wrapper

def save(self):
    def wrapper(item):
        return item.save()

    return wrapper

def delete(self):
    def wrapper(item):
        return item.delete()

    return wrapper
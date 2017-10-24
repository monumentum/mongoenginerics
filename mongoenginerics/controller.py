from .util import mongo_obj


class Controller():

    @mongo_obj.to_json
    def find(self, query):
        return self.model.objects()


    @mongo_obj.to_json
    def find_one(self, item_id):
        return self._find_one(item_id)


    @mongo_obj.to_json
    @mongo_obj.save
    def create(self, body):
        return self.model(**body)


    @mongo_obj.delete
    def delete(self, item_id):
        return self._find_one(item_id)

    @mongo_obj.to_json
    @mongo_obj.save
    def update(self, item_id, updates):
        item = self._find_one(item_id)

        for key, value in updates.items():
            setattr(item, key, value)

        return item


    def _find_one(self, item_id):
        return self.model.objects.get(pk=item_id)


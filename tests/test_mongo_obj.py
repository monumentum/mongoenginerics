import json
import unittest

from mongoenginerics.util import mongo_obj


class MockedPerfectObject:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def to_json(self):
        return json.dumps({
            'args': self.args,
            'kwargs': self.kwargs,
        })

    def save(self):
        return {
            'args': self.args,
            'kwargs': self.kwargs,
        }

    def delete(self):
        return {}


class MockedImperfectObject:
    def to_json(self):
        return True

    def delete(self, *args, **kwargs):
        raise SystemExit(1)


class MockedAnythingObject:
    pass


class MongoObjToJsonTest(unittest.TestCase):
    def test_to_json_preserve_args(self):
        class Caller:
            @mongo_obj.to_json
            def call_object(self, *args, **kwargs):
                return MockedPerfectObject(*args, **kwargs)

        args = [1, 2]
        kwargs = {'a': 1, 'b': 2}
        expected = {
            'args': args,
            'kwargs': kwargs,
        }
        self.assertEqual(expected, Caller().call_object(*args, **kwargs))

    def test_to_json_with_instance_method(self):
        class Caller:
            @mongo_obj.to_json
            def call_object(self):
                return MockedPerfectObject()

        self.assertIsNotNone(Caller().call_object())

    def test_to_json_with_method(self):
        @mongo_obj.to_json
        def call_object():
            return MockedPerfectObject()

        with self.assertRaises(TypeError):
            call_object()

    def test_to_json_with_not_json(self):
        class Caller:
            @mongo_obj.to_json
            def call_object(self):
                return MockedImperfectObject()

        with self.assertRaises(TypeError):
            Caller().call_object()

    def test_to_json_without_json_method(self):
        class Caller:
            @mongo_obj.to_json
            def call_object(self):
                return MockedAnythingObject()

        with self.assertRaises(AttributeError):
            Caller().call_object()


class MongoObjSaveTest(unittest.TestCase):
    def test_save_preserve_args(self):
        class Caller:
            @mongo_obj.to_json
            def call_object(self, *args, **kwargs):
                return MockedPerfectObject(*args, **kwargs)

        args = [1, 2]
        kwargs = {'a': 1, 'b': 2}
        expected = {
            'args': args,
            'kwargs': kwargs,
        }
        self.assertEqual(expected, Caller().call_object(*args, **kwargs))

    def test_save_with_instance_method(self):
        class Caller:
            @mongo_obj.save
            def call_object(self):
                return MockedPerfectObject()

        self.assertIsNotNone(Caller().call_object())

    def test_save_with_method(self):
        @mongo_obj.save
        def call_object():
            return MockedPerfectObject()

        with self.assertRaises(TypeError):
            call_object()

    def test_save_without_save_method(self):
        class Caller:
            @mongo_obj.save
            def call_object(self):
                return MockedAnythingObject()

        with self.assertRaises(AttributeError):
            Caller().call_object()


class MongoObjDeleteTest(unittest.TestCase):
    def test_delete_preserve_args(self):
        class Caller:
            @mongo_obj.delete
            def call_object(self, *args, **kwargs):
                return MockedPerfectObject()

        expected = {
            "deleted": True,
            "id": 42
        }
        self.assertEqual(expected, Caller().call_object(42))

    def test_delete_no_args(self):
        class Caller:
            @mongo_obj.delete
            def call_object(self):
                return MockedPerfectObject()

        with self.assertRaises(IndexError):
            Caller().call_object()

    def test_delete_failed_deletion(self):
        class Caller:
            @mongo_obj.delete
            def call_object(self, *args, **kwargs):
                return MockedImperfectObject()

        with self.assertRaises(SystemExit):
            Caller().call_object()

    def test_delete_with_instance_method(self):
        class Caller:
            @mongo_obj.delete
            def call_object(self, *args, **kwargs):
                return MockedPerfectObject()

        self.assertIsNotNone(Caller().call_object(1))

    def test_delete_with_method(self):
        @mongo_obj.delete
        def call_object(*args, **kwargs):
            return MockedPerfectObject()

        with self.assertRaises(TypeError):
            call_object()

    def test_delete_without_json_method(self):
        class Caller:
            @mongo_obj.delete
            def call_object(self):
                return MockedAnythingObject()

        with self.assertRaises(AttributeError):
            Caller().call_object()

import unittest
import json
try:
    from unittest.mock import patch
except ImportError:  # Pre Python 3.3
    from mock import patch
from StringIO import StringIO
from awesojson import dump, dumps, load, loads


@patch('awesojson.encoder.AwesoJSONEncoder.default')
class JSONDumpAPITest(unittest.TestCase):

    def test_int_do_not_call_encoder_default(self, default_mock):
        value = 0
        expected = StringIO()
        json.dump(value, expected)
        result = StringIO()
        dump(value, result)
        self.assertFalse(default_mock.called)
        self.assertEquals(result.getvalue(), expected.getvalue())

    def test_float_do_not_call_encoder_default(self, default_mock):
        value = 1.5
        expected = StringIO()
        json.dump(value, expected)
        result = StringIO()
        dump(value, result)
        self.assertFalse(default_mock.called)
        self.assertEquals(result.getvalue(), expected.getvalue())

    def test_string_do_not_call_encoder_default(self, default_mock):
        value = 'foo'
        expected = StringIO()
        json.dump(value, expected)
        result = StringIO()
        dump(value, result)
        self.assertFalse(default_mock.called)
        self.assertEquals(result.getvalue(), expected.getvalue())

    def test_list_do_not_call_encoder_default(self, default_mock):
        value = [1, 2, 3]
        expected = StringIO()
        json.dump(value, expected)
        result = StringIO()
        dump(value, result)
        self.assertFalse(default_mock.called)
        self.assertEquals(result.getvalue(), expected.getvalue())

    def test_dict_do_not_call_encoder_default(self, default_mock):
        value = {"foo": "bar"}
        expected = StringIO()
        json.dump(value, expected)
        result = StringIO()
        dump(value, result)
        self.assertFalse(default_mock.called)
        self.assertEquals(result.getvalue(), expected.getvalue())

    def test_object_call_encoder_default(self, default_mock):
        value = object()
        default_mock.return_value = None
        result = StringIO()
        dump(value, result)
        self.assertTrue(default_mock.called)

    def test_object_encoder_default_value_used(self, default_mock):
        value = object()
        return_value = {"awesojsontype": "testing", "data": None}
        default_mock.return_value = return_value
        expected = StringIO()
        json.dump(return_value, expected)
        result = StringIO()
        dump(value, result)
        self.assertTrue(default_mock.called)
        self.assertEquals(result.getvalue(), expected.getvalue())


@patch('awesojson.encoder.AwesoJSONEncoder.default')
class JSONDumpsAPITest(unittest.TestCase):

    def test_int_do_not_call_encoder_default(self, default_mock):
        value = 0
        expected = json.dumps(value)
        result = dumps(value)
        self.assertFalse(default_mock.called)
        self.assertEquals(result, expected)

    def test_float_do_not_call_encoder_default(self, default_mock):
        value = 1.5
        expected = json.dumps(value)
        result = dumps(value)
        self.assertFalse(default_mock.called)
        self.assertEquals(result, expected)

    def test_string_do_not_call_encoder_default(self, default_mock):
        value = 'foo'
        expected = json.dumps(value)
        result = dumps(value)
        self.assertFalse(default_mock.called)
        self.assertEquals(result, expected)

    def test_list_do_not_call_encoder_default(self, default_mock):
        value = [1, 2, 3]
        expected = json.dumps(value)
        result = dumps(value)
        self.assertFalse(default_mock.called)
        self.assertEquals(result, expected)

    def test_dict_do_not_call_encoder_default(self, default_mock):
        value = {"foo": "bar"}
        expected = json.dumps(value)
        result = dumps(value)
        self.assertFalse(default_mock.called)
        self.assertEquals(result, expected)

    def test_object_call_encoder_default(self, default_mock):
        value = object()
        default_mock.return_value = None
        dumps(value)
        self.assertTrue(default_mock.called)

    def test_object_encoder_default_value_used(self, default_mock):
        value = object()
        return_value = {"awesojsontype": "testing", "data": None}
        default_mock.return_value = return_value
        expected = json.dumps(return_value)
        result = dumps(value)
        self.assertTrue(default_mock.called)
        self.assertEquals(result, expected)


@patch('awesojson.decoder.AwesoJSONDecoder.object_handler')
class JSONLoadAPITest(unittest.TestCase):

    def test_int_do_not_call_decoder_object_handler(self, object_handler_mock):
        value = StringIO('0')
        expected = json.load(value)
        value.seek(0)
        result = load(value)
        self.assertFalse(object_handler_mock.called)
        self.assertEquals(result, expected)

    def test_float_do_not_call_decoder_object_handler(self, object_handler_mock):
        value = StringIO('1.5')
        expected = json.load(value)
        value.seek(0)
        result = load(value)
        self.assertFalse(object_handler_mock.called)
        self.assertEquals(result, expected)

    def test_string_do_not_call_decoder_object_handler(self, object_handler_mock):
        value = StringIO('"foo"')
        expected = json.load(value)
        value.seek(0)
        result = load(value)
        self.assertFalse(object_handler_mock.called)
        self.assertEquals(result, expected)

    def test_list_do_not_call_decoder_object_handler(self, object_handler_mock):
        value = StringIO('[0, 1, 2]')
        expected = json.load(value)
        value.seek(0)
        result = load(value)
        self.assertFalse(object_handler_mock.called)
        self.assertEquals(result, expected)

    def test_dict_call_decoder_object_handler(self, object_handler_mock):
        value = StringIO('{}')
        load(value)
        self.assertTrue(object_handler_mock.called)

    def test_dict_object_handler_return_value_used(self, object_handler_mock):
        value = StringIO('{"foo": "bar"}')
        expected = json.load(value)
        value.seek(0)
        object_handler_mock.return_value = expected
        result = load(value)
        self.assertTrue(object_handler_mock.called)
        self.assertEquals(result, expected)


@patch('awesojson.decoder.AwesoJSONDecoder.object_handler')
class JSONLoadsAPITest(unittest.TestCase):

    def test_int_do_not_call_decoder_object_handler(self, object_handler_mock):
        value = '0'
        expected = json.loads(value)
        result = loads(value)
        self.assertFalse(object_handler_mock.called)
        self.assertEquals(result, expected)

    def test_float_do_not_call_decoder_object_handler(self, object_handler_mock):
        value = '1.5'
        expected = json.loads(value)
        result = loads(value)
        self.assertFalse(object_handler_mock.called)
        self.assertEquals(result, expected)

    def test_string_do_not_call_decoder_object_handler(self, object_handler_mock):
        value = '"foo"'
        expected = json.loads(value)
        result = loads(value)
        self.assertFalse(object_handler_mock.called)
        self.assertEquals(result, expected)

    def test_list_do_not_call_decoder_object_handler(self, object_handler_mock):
        value = '[0, 1, 2]'
        expected = json.loads(value)
        result = loads(value)
        self.assertFalse(object_handler_mock.called)
        self.assertEquals(result, expected)

    def test_dict_call_decoder_object_handler(self, object_handler_mock):
        value = '{}'
        loads(value)
        self.assertTrue(object_handler_mock.called)

    def test_dict_decoder_object_handler_return_value_used(self, object_handler_mock):
        value = '{"foo": "bar"}'
        expected = json.loads(value)
        object_handler_mock.return_value = expected
        result = loads(value)
        self.assertTrue(object_handler_mock.called)
        self.assertEquals(result, expected)

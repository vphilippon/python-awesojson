import unittest
from awesojson import (decoder,
                       exceptions)


class AwesoJSONDecoderRegisterTest(unittest.TestCase):

    def setUp(self):
        decoder.AwesoJSONDecoder._decoder_table.clear()

    def test_basic_registration(self):
        f = lambda x: x
        decoder.AwesoJSONDecoder.register_decoder(f, 'test.name')
        self.assertEquals(decoder.AwesoJSONDecoder._decoder_table,
                          {'test.name': f})

    def test_None_fct_registration(self):
        decoder.AwesoJSONDecoder.register_decoder(None, 'test.name')
        self.assertEquals(decoder.AwesoJSONDecoder._decoder_table,
                          {'test.name': None})

    def test_None_type_identifier_registration(self):
        f = lambda x: x
        decoder.AwesoJSONDecoder.register_decoder(f, None)
        self.assertEquals(decoder.AwesoJSONDecoder._decoder_table,
                          {None: f})


class AwesoJSONDecoderGetEncoderTest(unittest.TestCase):

    def setUp(self):
        decoder.AwesoJSONDecoder._decoder_table.clear()

    def test_basic_register_get(self):
        f = lambda x: x
        decoder.AwesoJSONDecoder._decoder_table = {'test.name': f}
        result = decoder.AwesoJSONDecoder.get_decoder('test.name')
        self.assertEquals(result, f)

    def test_type_None_register_get(self):
        f = lambda x: x
        decoder.AwesoJSONDecoder._decoder_table = {None: f}
        result = decoder.AwesoJSONDecoder.get_decoder(None)
        self.assertEquals(result, f)

    def test_explicit_None_register_get(self):
        decoder.AwesoJSONDecoder._decoder_table = {'test.name': None}
        result = decoder.AwesoJSONDecoder.get_decoder('test.name')
        self.assertEquals(result, None)

    def test_implicit_None_register_get(self):
        result = decoder.AwesoJSONDecoder.get_decoder('test.name')
        self.assertEquals(result, None)


class AwesoJSONDecoderObjectHandler(unittest.TestCase):

    def setUp(self):
        decoder.AwesoJSONDecoder._decoder_table.clear()

    def test_empty_table_object_handler(self):
        inst = decoder.AwesoJSONDecoder()
        self.assertRaises(exceptions.AwesoJSONException, inst.object_handler,
                          {'awesojsontype': 'foo', 'data': 'bar'})

    def test_no_function_registrered_object_handler(self):
        decoder.AwesoJSONDecoder._decoder_table['not_foo'] = lambda x: str(x)
        inst = decoder.AwesoJSONDecoder()
        self.assertRaises(exceptions.AwesoJSONException, inst.object_handler,
                          {'awesojsontype': 'foo', 'data': 'bar'})

    def test_basic_object_handler(self):
        decoder.AwesoJSONDecoder._decoder_table['foo'] = lambda x: x
        inst = decoder.AwesoJSONDecoder()
        result = inst.object_handler({'awesojsontype': 'foo', 'data': 'bar'})
        self.assertEquals(result, 'bar')

    def test_no_awesojsontype_object_handler(self):
        decoder.AwesoJSONDecoder._decoder_table['foo'] = lambda x: x
        inst = decoder.AwesoJSONDecoder()
        result = inst.object_handler({'data': 'bar'})
        self.assertEquals(result, {'data': 'bar'})

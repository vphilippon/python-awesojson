import unittest
from awesojson import encoder


class AwesoJSONEncoderRegisterTest(unittest.TestCase):

    def setUp(self):
        encoder.AwesoJSONEncoder._encoder_table.clear()

    def test_basic_registration(self):
        f = lambda x: x
        encoder.AwesoJSONEncoder.register_encoder(f, 'test.name')
        self.assertEquals(encoder.AwesoJSONEncoder._encoder_table,
                          {'test.name': f})

    def test_None_fct_registration(self):
        encoder.AwesoJSONEncoder.register_encoder(None, 'test.name')
        self.assertEquals(encoder.AwesoJSONEncoder._encoder_table,
                          {'test.name': None})

    def test_None_type_identifier_registration(self):
        f = lambda x: x
        encoder.AwesoJSONEncoder.register_encoder(f, None)
        self.assertEquals(encoder.AwesoJSONEncoder._encoder_table,
                          {None: f})


class AwesoJSONEncoderGetEncoderTest(unittest.TestCase):

    def setUp(self):
        encoder.AwesoJSONEncoder._encoder_table.clear()

    def test_basic_register_get(self):
        f = lambda x: x
        encoder.AwesoJSONEncoder._encoder_table = {'test.name': f}
        result = encoder.AwesoJSONEncoder.get_encoder('test.name')
        self.assertEquals(result, f)

    def test_type_None_register_get(self):
        f = lambda x: x
        encoder.AwesoJSONEncoder._encoder_table = {None: f}
        result = encoder.AwesoJSONEncoder.get_encoder(None)
        self.assertEquals(result, f)

    def test_explicit_None_register_get(self):
        encoder.AwesoJSONEncoder._encoder_table = {'test.name': None}
        result = encoder.AwesoJSONEncoder.get_encoder('test.name')
        self.assertEquals(result, None)

    def test_implicit_None_register_get(self):
        result = encoder.AwesoJSONEncoder.get_encoder('test.name')
        self.assertEquals(result, None)


class AwesoJSONEncoderDefaultTest(unittest.TestCase):

    def setUp(self):
        encoder.AwesoJSONEncoder._encoder_table.clear()

    def test_empty_table_default(self):
        inst = encoder.AwesoJSONEncoder()
        self.assertRaises(Exception, inst.default, object())

    def test_no_function_registrered_default(self):
        encoder.AwesoJSONEncoder._encoder_table['foo.bar'] = lambda x: str(x)
        inst = encoder.AwesoJSONEncoder()
        self.assertRaises(Exception, inst.default, object())

    def test_basic_default(self):
        encoder.AwesoJSONEncoder._encoder_table['__builtin__.object'] = (
            lambda x: 'test'
        )
        inst = encoder.AwesoJSONEncoder()
        result = inst.default(object())
        self.assertEquals(
            result, {'awesojsontype': '__builtin__.object', 'data': 'test'}
        )

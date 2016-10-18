import unittest
from awesojson import (encoder,
                       utils)


class AwesoJSONEncoderRegisterTest(unittest.TestCase):

    class DummyClass(object):
        """
        Dummy class to test registration.
        """
        pass

    def setUp(self):
        encoder.AwesoJSONEncoder._encoder_table.clear()

    def test_basic_registration(self):
        f = lambda x: x
        encoder.AwesoJSONEncoder.register_encoder(f, self.DummyClass)
        self.assertEquals(
            encoder.AwesoJSONEncoder._encoder_table,
            {self.DummyClass: (f, utils.get_fqcn(self.DummyClass))}
        )

    def test_None_fct_registration(self):
        encoder.AwesoJSONEncoder.register_encoder(None, self.DummyClass)
        self.assertEquals(
            encoder.AwesoJSONEncoder._encoder_table,
            {self.DummyClass: (None, utils.get_fqcn(self.DummyClass))}
        )

    def test_None_type_object_registration(self):
        f = lambda x: x
        self.assertRaises(
            Exception,
            encoder.AwesoJSONEncoder.register_encoder,
            encoder_fct=f, type_object=None,
        )

    def test_specified_type_identifier_registration(self):
        f = lambda x: x
        type_identifier = 'custom.test.name'
        encoder.AwesoJSONEncoder.register_encoder(f, self.DummyClass, type_identifier)
        self.assertEquals(
            encoder.AwesoJSONEncoder._encoder_table,
            {self.DummyClass: (f, type_identifier)}
        )


class AwesoJSONEncoderGetEncoderTest(unittest.TestCase):

    class DummyClass(object):
        """
        Dummy class to test registration.
        """
        pass

    def setUp(self):
        encoder.AwesoJSONEncoder._encoder_table.clear()

    def test_basic_register_get(self):
        f = lambda x: x
        encoder.AwesoJSONEncoder._encoder_table = {self.DummyClass: f}
        result = encoder.AwesoJSONEncoder.get_encoder(self.DummyClass)
        self.assertEquals(result, f)

    def test_type_None_register_get(self):
        f = lambda x: x
        encoder.AwesoJSONEncoder._encoder_table = {None: f}
        self.assertRaises(
            Exception,
            encoder.AwesoJSONEncoder.get_encoder,
            type_object=None
        )

    def test_explicit_None_register_get(self):
        encoder.AwesoJSONEncoder._encoder_table = {self.DummyClass: None}
        result = encoder.AwesoJSONEncoder.get_encoder(self.DummyClass)
        self.assertEquals(result, None)

    def test_implicit_None_register_get(self):
        result = encoder.AwesoJSONEncoder.get_encoder(self.DummyClass)
        self.assertEquals(result, None)


class AwesoJSONEncoderDefaultTest(unittest.TestCase):

    class DummyClass(object):
        """
        Dummy class to test registration.
        """
        pass

    def setUp(self):
        encoder.AwesoJSONEncoder._encoder_table.clear()

    def test_empty_table_default(self):
        inst = encoder.AwesoJSONEncoder()
        self.assertRaises(Exception, inst.default, self.DummyClass)

    def test_no_function_registrered_default(self):
        encoder.AwesoJSONEncoder._encoder_table[self.DummyClass] = lambda x: str(x)
        inst = encoder.AwesoJSONEncoder()
        self.assertRaises(Exception, inst.default, object())

    def test_basic_default(self):
        encoder.AwesoJSONEncoder._encoder_table[self.DummyClass] = (
            (lambda x: 'test', utils.get_fqcn(self.DummyClass))
        )
        inst = encoder.AwesoJSONEncoder()
        result = inst.default(self.DummyClass())
        self.assertEquals(
            result, {'awesojsontype': utils.get_fqcn(self.DummyClass), 'data': 'test'}
        )

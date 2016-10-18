import unittest
from awesojson import utils


class AwesoJSONEncoderRegisterTest(unittest.TestCase):

    class DummyClass(object):
        """
        Dummy class to test registration.
        """
        pass

    def test_get_fqcn_None(self):
        type_object = None
        self.assertRaises(
            Exception,
            utils.get_fqcn,
            type_object=type_object
        )

    def test_get_fqcn_not_a_type(self):
        type_object = 'An instance of str'
        self.assertRaises(
            Exception,
            utils.get_fqcn,
            type_object=type_object
        )

    def test_get_fqcn_object(self):
        type_object = object
        result = utils.get_fqcn(type_object)
        self.assertTrue(result.endswith('.object'))

    def test_get_fqcn_class(self):
        type_object = self.DummyClass
        result = utils.get_fqcn(type_object)
        self.assertEquals(result, 'test_get_fqcn.DummyClass')


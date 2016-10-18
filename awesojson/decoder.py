# -*- coding: utf-8 -*-

"""
awesojson.decoder
~~~~~~~~~~~~~~~~~

This module implements the AwesoJSON decoder classes.

:copyright: (c) 2015 by Vincent Philippon.
:license: MIT, see LICENSE for more details.
"""

import json


class AwesoJSONDecoder(json.JSONDecoder):
    """
    A ``JSONDecoder`` subclass serving as an adapter for user-defined decoder
    functions.

    Users can register functions as decoder function for a given ``type`` textual
    type identifier. The ``object_handler`` method will call the registered function
    of the received object's `awesojsontype` attribute, if found in the
    parsed data. This allow users to define the decoding functions wherever
    they want and use this adapter class to register them to be used when
    deserializing JSON objects.
    """

    _decoder_table = {}

    @classmethod
    def register_decoder(cls, decoder_fct, type_identifier):
        """
        Register `decoder_fct` as the decode function for `type_identifier`.

        :param decoder_fct: The decoder function to register
        :param str type_identifier: The textual type identifier of the ``type`` to register
        """
        cls._decoder_table[type_identifier] = decoder_fct

    @classmethod
    def get_decoder(cls, type_identifier):
        """
        Get the registered decoder function for `type_identifier`.

        Will return ``None`` if no function is registered for `type_identifier`.

        :param str type_identifier: The textual type identifier of the ``type``

        :returns: Decoder function registered for `type_identifier`
        """
        return cls._decoder_table.get(type_identifier)

    def __init__(self, **kwargs):
        super(AwesoJSONDecoder, self).__init__(object_hook=self.object_handler,
                                               **kwargs)

    def object_handler(self, obj):
        """
        Deserialize `obj` according to the ``type`` textual type identifier, if found.

        Uses the decoder function registered for the ``type`` textual type identifier
        in the ``awesojsontype`` key of `obj`.

        If no ``awesojsontype`` key is found, the dictionnary will be returned
        as is.

        :param dict obj: JSON object to deserialize

        :raises Exception: No registered decoder function suits the defined
                           `obj['awesojsontype']`

        :returns: A deserialized JSON object
        :rtype: object
        """
        if 'awesojsontype' in obj:
            type_identifier = obj['awesojsontype']
            deserializer = self.get_decoder(type_identifier)
            if deserializer:
                obj = deserializer(obj['data'])
            else:
                raise Exception("No decoder funtion registered for type {0} "
                                "(object: {1})".format(type_identifier, obj))

        return obj


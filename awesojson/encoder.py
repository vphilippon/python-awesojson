# -*- coding: utf-8 -*-

"""
awesojson.encoder
~~~~~~~~~~~~~~~~~

This module implements the AwesoJSON encoder classes.

:copyright: (c) 2015 by Vincent Philippon.
:license: LGPL V3.0, see LICENSE for more details.
"""

import json


class AwesoJSONEncoder(json.JSONEncoder):
    """
    A ``JSONEncoder`` subclass serving as an adapter for user-defined encoder
    functions.

    Users can register functions as encoder function for a given fully
    qualified class name. The ``default`` method will call the registered
    function of the received object's fully qualified name. This allow users to
    define the encoding functions wherever they want and use this adapter class
    to register them to be used when serializing object as JSON.
    """

    _encoder_table = {}

    @classmethod
    def register_encoder(cls, encoder_fct, type_identifier):
        """
        Register `encoder_fct` as the encode function for `type_identifier`.

        :param encoder_fct: The encoder function to register
        :param str type_identifier: The fully qualified class name to register
        """
        cls._encoder_table[type_identifier] = encoder_fct

    @classmethod
    def get_encoder(cls, type_identifier):
        """
        Get the registered encoder function for `type_identifier`.

        Will return ``None`` if no function is registered for `type_identifier`.

        :param str type_identifier: Fully qualified class name

        :returns: Encoder function registered for `type_identifier`
        """
        return cls._encoder_table.get(type_identifier)

    def default(self, obj):
        """
        Serialize `obj` according to it's fully qualified class name.

        Uses the encoder function registered for the fully qualified
        class name of `obj`.

        :param object obj: Object to serialize

        :raises Exception: No registered encoder function suits `obj`

        :returns: A JSON serializable object, with the AwesoJSON type metadata
        :rtype: dict
        """
        type_identifier = type(obj).__module__ + '.' + obj.__class__.__name__
        serializer = self.get_encoder(type_identifier)
        if serializer:
            return {'awesojsontype': type_identifier, 'data': serializer(obj)}
        else:
            raise Exception("No encoder funtion registered for type {0} "
                            "(object: {1})".format(type_identifier, obj))

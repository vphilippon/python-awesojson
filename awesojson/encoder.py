# -*- coding: utf-8 -*-

"""
awesojson.encoder
~~~~~~~~~~~~~~~~~

This module implements the AwesoJSON encoder classes.

:copyright: (c) 2015 by Vincent Philippon.
:license: MIT, see LICENSE for more details.
"""

import json

from awesojson.utils import get_fqcn
from awesojson.exceptions import (AwesoJSONException, NotATypeError)


class AwesoJSONEncoder(json.JSONEncoder):
    """
    A ``JSONEncoder`` subclass serving as an adapter for user-defined encoder
    functions.

    Users can register functions as encoder function for ``type`` and a textual
    type identifier. The ``default`` method will call the registered function
    of the received object's ``type``. This allow users to define the encoding
    functions wherever they want and use this adapter class to register them
    to be used when serializing object as JSON.
    """

    _encoder_table = {}

    @classmethod
    def register_encoder(cls, encoder_fct, type_object, type_identifier=None):
        """
        Register `encoder_fct` as the encode function for `type_object` identified as `type_identifier`.

        :param encoder_fct: The encoder function to register
        :param type type_object: The type object to register
        :param str type_identifier: The textual type identifier. Default is the fully qualified class name

        :raises NotATypeError: The `type_object` is not a ``type``
        """
        if not isinstance(type_object, type):
            raise NotATypeError("'{type_object}' is not a type".format(type_object=type_object))

        if type_identifier is None:
            type_identifier = get_fqcn(type_object)

        cls._encoder_table[type_object] = (encoder_fct, type_identifier)

    @classmethod
    def get_encoder(cls, type_object):
        """
        Get the registered encoder function and textual type identifier for `type_object`.

        Will return ``None`` if no function is registered for `type_identifier`.

        :param type type_object: The type object

        :raises NotATypeError: The `type_object` is not a ``type``

        :returns: Encoder function registered for `type_identifier` and the textual type identifier
        :rtype: (fct, str)
        """
        if not isinstance(type_object, type):
            raise NotATypeError("'{type_object}' is not a type".format(type_object=type_object))

        return cls._encoder_table.get(type_object)

    def default(self, obj):
        """
        Serialize `obj` according to it's ``type``.

        Uses the encoder function registered for the ``type`` of `obj`.

        :param object obj: Object to serialize

        :raises AwesoJSONException: No registered encoder function suits `obj`

        :returns: A JSON serializable object, with the AwesoJSON type metadata
        :rtype: dict
        """
        type_object = type(obj)
        registration = self.get_encoder(type_object)
        serializer, type_identifier = registration or (None, None)
        if serializer:
            return {'awesojsontype': type_identifier, 'data': serializer(obj)}
        else:
            raise AwesoJSONException("No encoder funtion registered for type {0} "
                                     "(object: {1})".format(type_identifier, obj))


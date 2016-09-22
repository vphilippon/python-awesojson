# -*- coding: utf-8 -*-

"""
awesojson.api
~~~~~~~~~~~~~

This module implements the AwesoJSON API.

:copyright: (c) 2015 by Vincent Philippon.
:license: MIT, see LICENSE for more details.
"""

import json

from .decoder import AwesoJSONDecoder
from .encoder import AwesoJSONEncoder


def load(filehandle, **kwargs):
    """
    Deserialize a file-like object containing a JSON document to a Python object.

    The decoding functions registered to ``AwesoJSONDecoder`` are used to generate
    a Python object of the right type.

    See ``json.load`` for more function arguments and details.

    :param file filehandle: The file-like object (supporting ``.read()``) containing a JSON document

    :raises Exception: The JSON document contains an object with no registered
                       decoder function which suits the *defined* `awesojsontype` for that object

    :returns: The deserialized Python object

    Usage::
        >>> import awesojson
        >>> awesojson.register_decoder(my_decode_fct, 'datetime.datetime')
        >>> python_datetime = awesojson.load(json_file_datetime)
    """
    return json.load(filehandle, cls=AwesoJSONDecoder, **kwargs)


def loads(strvalue, **kwargs):
    """
    Deserialize a ``str`` or ``unicode`` object containing a JSON document to a Python object.

    The decoding functions registered to ``AwesoJSONDecoder`` are used to generate
    a Python object of the right type.

    See ``json.loads`` for more function arguments and details.

    :param (str|unicode) strvalue: The string object containing a JSON document

    :raises Exception: The JSON document contains an object with no registered
                       decoder function which suits the *defined* `awesojsontype` for that object

    :returns: The deserialized Python object

    Usage::
        >>> import awesojson
        >>> awesojson.register_decoder(my_decode_fct, 'datetime.datetime')
        >>> python_datetime = awesojson.loads(json_string_datetime)
    """
    return json.loads(strvalue, cls=AwesoJSONDecoder, **kwargs)


def dump(obj, filehandle, **kwargs):
    """
    Serialize a Python object as a JSON formated stream to a file-like object.

    The encoding functions registered to ``AwesoJSONEncoder`` are used to generate
    a JSON representation for `obj`'s type.

    See ``json.dump`` for more function arguments and details.

    :param obj: The Python object
    :param file filehandle: The file-like object (supporting ``.write()``) that receives the stream

    :raises Exception: There's no registered encoder function that suits `obj`'s type

    :returns: The JSON serialization of the Python object
    :rtype: (str|unicode)

    Usage::
        >>> import awesojson
        >>> awesojson.register_encoder(my_encode_fct, 'datetime.datetime')
        >>> python_datetime = datetime.datetime.now()
        >>> awesojson.dump(python_datetime, json_file_datetime)
    """
    return json.dump(obj, filehandle, cls=AwesoJSONEncoder, **kwargs)


def dumps(obj, **kwargs):
    """
    Serialize a Python object to a JSON formated ``str`` or ``unicode``.

    The encoding functions registered to ``AwesoJSONEncoder`` are used to generate
    a JSON representation for `obj`'s type.

    See ``json.dumps`` for more function arguments and details.

    :param obj: The Python object

    :raises Exception: There's no registered encoder function that suits `obj`'s type

    :returns: The JSON serialization of the Python object
    :rtype: (str|unicode)

    Usage::
        >>> import awesojson
        >>> awesojson.register_encoder(my_encode_fct, 'datetime.datetime')
        >>> python_datetime = datetime.datetime.now()
        >>> json_string_datetime = awesojson.dumps(python_datetime)
    """
    return json.dumps(obj, cls=AwesoJSONEncoder, **kwargs)


def register_decoder(decoder_fct, type_identifier):
    """
    Register a function to use for the JSON deserialization of a given object type.

    The decoding function `decoder_fct` will be registered to the ``AwesoJSONDecoder`` class
    as the function to use to deserialize the objects for which the fully qualified class name
    matches the `type_identifier` string.

    :param decoder_fct: The decoder function to register
    :param str type_identifier: The fully qualified class name to register

    Usage::
        >>> import awesojson
        >>> awesojson.register_decoder(my_decode_fct, 'datetime.datetime')
    """
    # TODO: This should definitely use a FQDN "finder tool", this is really error prone for the user
    AwesoJSONDecoder.register_decoder(decoder_fct, type_identifier)


def register_encoder(encoder_fct, type_identifier):
    """
    Register a function to use for the JSON serialization of a given object type.

    The encoding function `encoder_fct` will be registered to the ``AwesoJSONEncoder`` class
    as the function to use to serialize the objects for which the fully qualified class name
    matches the `type_identifier` string.

    :param encoder_fct: The encoder function to register
    :param str type_identifier: The fully qualified class name to register

    Usage::
        >>> import awesojson
        >>> awesojson.register_encoder(my_encode_fct, 'datetime.datetime')
    """
    # TODO: This should definitely use a FQDN "finder tool", this is really error prone for the user
    AwesoJSONEncoder.register_encoder(encoder_fct, type_identifier)


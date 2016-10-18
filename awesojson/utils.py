# -*- coding: utf-8 -*-

"""
awesojson.utils
~~~~~~~~~~~~~~~

This module provides common utilities for the AwesoJSON lib.

:copyright: (c) 2016 by Vincent Philippon.
:license: MIT, see LICENSE for more details.
"""


def get_fqcn(type_object):
    """
    Gets the python fully qualified class name for `type_object`.

    :param type type_object: The type object to to get the FQCN of

    :raises Exception: The `type_object` is not a ``type``

    :returns: The fully qualified class name of `type_object`
    :rtype: str
    """
    if not isinstance(type_object, type):
        raise Exception("type_object is not a type")

    return type_object.__module__ + '.' + type_object.__name__


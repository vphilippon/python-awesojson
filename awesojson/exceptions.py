# -*- coding: utf-8 -*-

"""
awesojson.exceptions
~~~~~~~~~~~~~~~~~~~~

This module provides common Exception classes for the AwesoJSON lib.

:copyright: (c) 2016 by Vincent Philippon.
:license: MIT, see LICENSE for more details.
"""


class AwesoJSONException(Exception):
    """
    The common base ``Exception`` for every exception of the AwesoJSON lib.
    """
    pass


class NotATypeError(AwesoJSONException, TypeError):
    """
    The argument is not a ``type``.
    """
    pass


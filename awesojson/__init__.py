# -*- coding: utf-8 -*-

__title__ = 'awesojson'
__version__ = '0.0.1'
__author__ = 'Vincent Philippon'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Vincent Philippon'

from .api import (dump, dumps,
                  load, loads,
                  register_encoder,
                  register_decoder)
from .utils import get_fqcn
from .exceptions import (AwesoJSONException)


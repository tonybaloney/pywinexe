# -*- coding: utf-8 -*-

"""
winexe library

winexe is a library, written to ease remote management of windows
machines. Basic Usage:

   >>> import winexe
   >>> kwargs = {
      'user': 'user',
      'password':'password',
      'host':'10.0.0.1'
      }
   >>> output = winexe.cmd('ipconfig', **kwargs)

:copyright: (c) 2014 Jakob Aarøe Dam
:license:

"""
__title__ = 'winexe'
__version__ = '0.0.1'
__author__ = u'Jakob Aarøe Dam'
__license__ = 'Apache 2.0'
__copyright__ = u'Copyright 2014 Jakob Aarøe Dam'

from .api import *

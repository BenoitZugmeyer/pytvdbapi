# -*- coding: utf-8 -*-

# Copyright 2011 - 2013 Björn Larsson

# This file is part of pytvdbapi.
#
# pytvdbapi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pytvdbapi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pytvdbapi.  If not, see <http://www.gnu.org/licenses/>.

"""
A module containing all the errors raised by pytvdbapi.

pytvdbapi will only raise exceptions that are of type :class:`PytvdbapiError`.
"""

import logging

__all__ = ['PytvdbapiError', 'BadData', 'ConnectionError',
           'TVDBAttributeError', 'TVDBIndexError', 'TVDBIdError',
           'TVDBValueError', 'TVDBNotFoundError']

#Module level logger
logger = logging.getLogger(__name__)  # pylint: disable=C0103


class PytvdbapiError(Exception):
    """Base exception for all exceptions raised by pytvdbapi"""
    def __init__(self, msg, *args, **kwargs):
        super(PytvdbapiError, self).__init__(msg, args, kwargs)
        logger.error(msg)


class BadData(PytvdbapiError):
    """
    Raised if there are issues parsing the XML data provided by
    `thetvdb.com <http://thetvdb.com>`_
    """
    pass


# pylint: disable=W0622, W0511
# TODO: Change this name so it does not collide with the builtin name and remove the lint directive
class ConnectionError(PytvdbapiError):
    """
    Raised by the :class:`pytvdbapi.Loader` when unable to connect to the provided URL.
    """
    pass


class TVDBAttributeError(PytvdbapiError, AttributeError):
    """
    A replacement for the standard AttributeError. Will be raised when
    accessing invalid attributes of :class:`pytvdbapi.api.Show` and :class:`pytvdbapi.api.Episode`
    instances
    """
    pass


class TVDBIndexError(PytvdbapiError):
    """
    A replacement for the standard IndexError. Will be raised when accessing
    invalid indexes of :class:`pytvdbapi.api.Show` and :class:`pytvdbapi.api.Season` instances.
    """
    pass


class TVDBValueError(PytvdbapiError):
    """
    A replacement for the standard ValueError exception.
    """
    pass


class TVDBIdError(PytvdbapiError):
    """Raised when trying to get a show using an invalid Show ID"""
    pass


class TVDBNotFoundError(PytvdbapiError):
    """Raised when the data can not be found. Represent the 404 http code."""
    pass

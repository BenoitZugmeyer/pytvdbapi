# -*- coding: utf-8 -*-

# Copyright 2011 Björn Larsson

# This file is part of thetvdb.
#
# thetvdb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# thetvdb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with thetvdb.  If not, see <http://www.gnu.org/licenses/>.

__all__ = ['file_loader']

def file_loader( file ):
    try:
        return open(file).read()
    except IOError:
        print("Unable to load {0}".format(file))
        return ""
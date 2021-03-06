#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#This file is part of OrariSTP-bot.
#
# OrariSTP-bot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OrariSTP-bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OrariSTP-bot.  If not, see <http://www.gnu.org/licenses/>
# 2016-2017
# Peppuz Elativ <peppuzvitale@gmail.com>
#

class ConnectionException(Exception):
    """docstring for Connection Error."""
    def __init__(self, arg):
        super(ConnectionException, self).__init__()
        self.arg = arg

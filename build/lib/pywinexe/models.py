# -*- coding: utf-8 -*-
"""
Copyright 2016 Anthony Shaw
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
import logging
import subprocess
import parser

from .exceptions import RequestException

log = logging.getLogger(__name__)


class Request(object):
    def __init__(self,
                 method=None,
                 host=None,
                 cmd=None,
                 script=None,
                 user=None,
                 password=None,
                 args=None):
        self.method = method
        self.host = host
        self.cmd = cmd
        self.script = script
        self.user = user
        self.password = password
        self.args = args

        self.parse()

    def __repr__(self):
        return '<Request [%s]>' % (self.method)

    def parse(self):
        """Parse commands and convert to winexe supported commands
        """
        if self.method == 'script':
            self.cmd = parser.parse(self.script, *self.args)

        elif self.method == 'cmd':
            self.cmd = parser.parse_cmd(self.cmd, *self.args)

        elif self.method == 'ps':
            self.cmd = parser.parse_ps(self.cmd, *self.args)

        else:
            raise Exception('Unknown method %s' % self.method)

    def command(self):
        """Constructs a complete winexe command. Returns command in a list.
        """
        args = ['winexe']
        if self.user and self.password:
            args.extend(['-U', '%s%%%s' % (self.user, self.password)])
        args.append('//%s' % self.host)
        args.append(self.cmd)
        return args

    def command_str(self):
        """Return the winexe command. Can by pasted directly to the terminal.
        """
        args = self.command()
        args[-1] = "'%s'" % self.cmd
        return ' '.join(args)

    def send(self):
        """Sends the request. Returns output, success
        """
        winexe_cmd = self.command()
        log.debug("Executing command: %s" % self.command_str())
        try:
            output = subprocess.check_output(winexe_cmd,
                                             stderr=subprocess.STDOUT)
            # always strip ending windows newlines
            output = output.rstrip('\r\n')
            return output
        except subprocess.CalledProcessError as e:
            raise RequestException(e.output, request=self.command_str())

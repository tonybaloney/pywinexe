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
        file=None,
        user=None,
        password=None):

        self.method = method
        self.host = host
        self.cmd = cmd
        self.file = file
        self.user = user
        self.password = password

        self.parse()

    def __repr__(self):
        return '<Request [%s]>' % (self.method)

    def parse(self):
        """Parse commands and convert to winexe supported commands
        """
        if self.method == 'file':
            self.cmd = parser.parse(self.file)

        elif self.method == 'cmd':
            self.cmd = parser.parse_cmd(self.cmd)

        elif self.method == 'ps':
            self.cmd = parser.parse_ps(self.cmd)

        else:
            raise Exception('Unknown method %s' % self.method)

    def winexe_command(self):
        """Constructs a complete winexe command. Returns command in a list.
        """
        args = ['winexe']
        if self.user and self.password:
            args.extend(['-U', '%s%%%s' % (self.user, self.password)])
        args.append('//%s' % self.host)
        args.append(self.cmd)
        return args

    def send(self):
        """Sends the request. Returns output, success
        """
        winexe_cmd = self.winexe_command()
        log.debug("Executing command: %s" % ' '.join(winexe_cmd))
        try:
            output = subprocess.check_output(winexe_cmd, stderr=subprocess.STDOUT)
            # always strip ending windows newlines
            output = output.rstrip('\r\n')
            return output
        except subprocess.CalledProcessError, e:
            raise RequestException(e.output, request=winexe_cmd)

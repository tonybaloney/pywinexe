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
            output = subprocess.check_output(winexe_cmd, stderr=subprocess.STDOUT)
            # always strip ending windows newlines
            output = output.rstrip('\r\n')
            return output
        except subprocess.CalledProcessError, e:
            raise RequestException(e.output, request=self.command_str())

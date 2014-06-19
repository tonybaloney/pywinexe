import subprocess
import parser

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

        if self.method == 'file':
            self.parse_file()

        if not self.cmd:
            raise Exception('No commands to execute!')

    def __repr__(self):
        return '<Request [%s]>' % (self.method)

    def parse_file(self):
        """Parse file and convert to winexe supported commands
        """
        self.cmd = parser.parse(self.file)

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
        try:
            output = subprocess.check_output(winexe_cmd, stderr=subprocess.STDOUT)
            return output, True
        except subprocess.CalledProcessError, e:
            print e.cmd
            return e.output, False

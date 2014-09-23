from .models import Request

def run(method, **kwargs):
    return Request(method, **kwargs).send()

def cmd(cmd, **kwargs):
    """Run statements with the windows cmd interpreter

    :param cmd: Statements to run
    :param \*\*kwargs: Optional arguments that ``Request`` takes
    """
    return Request('cmd', cmd=cmd, **kwargs).send()

def ps(cmd, **kwargs):
    """Run statements with the windows powershell interpreter

    :param cmd: Statements to run
    :param \*\*kwargs: Optional arguments that ``Request`` takes
    """
    return Request('ps', cmd=cmd, **kwargs).send()

def script(script, *args, **kwargs):
    """Run the statements in the script

    :param script: script to execute
    :param \*args: Arguments to the script
    :param \*\*kwargs: Optional arguments that ``Request`` takes
    """
    kwargs['script'] = script
    kwargs['args'] = args
    return Request('script', **kwargs).send()

from .models import Request

def run(method, **kwargs):
    return Request(method, **kwargs).send()

def cmd(cmd, **kwargs):
    return Request('cmd', cmd=cmd, **kwargs).send()

def ps(cmd, **kwargs):
    return Request('ps', cmd=cmd, **kwargs).send()

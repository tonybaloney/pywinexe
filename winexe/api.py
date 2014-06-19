from .models import Request

def run(method, **kwargs):
    return Request(method, **kwargs).send()


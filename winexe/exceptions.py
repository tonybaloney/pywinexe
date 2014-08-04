class RequestException(IOError):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RequestException, self).__init__(*args, **kwargs)

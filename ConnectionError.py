class ConnectionException(Exception):
    """docstring for Connection Error."""
    def __init__(self, arg):
        super(ConnectionException, self).__init__()
        self.arg = arg

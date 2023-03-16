class FirebaseConnectionError(Exception):
    """Exception raised when unable to connect to Firebase."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class FirebaseQuerryError(Exception):
    """Exception raised when unable to fetch data from Firebase."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

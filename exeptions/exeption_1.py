class CustomException(Exception):
    """
    Custom exception class
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

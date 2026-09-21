class NoaaError(Exception):
    pass


class NoaaApiError(NoaaError):
    def __init__(self, message: str, status_code: int = 400):
        self.status_code = status_code
        self.message = message

        super().__init__(f"message: {message}, status_code: {status_code}")


class NoaaNotFoundError(NoaaError):
    pass

class InvalidAPIVersionException(Exception):
    """An invalid API version was passed."""


class NotFoundException(Exception):
    """The resource could not be found."""


class UnauthorizedException(Exception):
    """The API key supplied is not authorized to access this resource."""


class InvalidObjectException(Exception):
    """The object you attempted to create or update was invalid."""
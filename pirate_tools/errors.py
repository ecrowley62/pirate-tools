class NoConfigFileFoundError(Exception):
    """
    Exception should be raised when no configuration file is found
    """


class MalformedConfigFileError(Exception):
    """
    Exception should be raised when the configuration file can not be completely parsed.
    This error includes keys being missing from the configuration file, or invalid
    values existing in the configuration file
    """

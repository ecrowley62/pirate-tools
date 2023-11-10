from abc import ABC


class MediaToManageBluePrint(ABC):
    """
    BluePrint for what a managed media object (a movie, or a collection of tv episodes)
    should always contain
    """

    def __init__(self, name: str) -> None:
        self.name = name


class TvShow(MediaToManageBluePrint):
    """
    A television show's episode(s)
    """

    def __init__(self, name: str) -> None:
        super().__init__(name=name)


class Movie(MediaToManageBluePrint):
    """
    A movie
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)

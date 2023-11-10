import pathlib


class ApplicationConfiguration:
    """
    Object containing the default or modified configuration state for the application
    """

    CONFIG_DIR_NAME = ".pirate-tools"

    def __init__(self, local_configuration_directory: str = None) -> None:
        self._local_configuration_directory = local_configuration_directory

    @property
    def local_configuration_directory(self) -> str:
        if not self._local_configuration_directory:
            config_dir_path = pathlib.Path.home() + self.CONFIG_DIR_NAME
            self._local_configuration_directory = config_dir_path
        return self._local_configuration_directory
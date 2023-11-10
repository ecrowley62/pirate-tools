import pathlib
import json


class ConfigurationState:
    """
    Object containing the default or modified configuration state for the application
    """

    CONFIG_DIR_NAME = ".pirate-tools"
    CONFIG_FILE_NAME = "config.json"
    LOG_FILE_NAME = "log.txt"

    def __init__(self, local_configuration_directory: str = None) -> None:
        self._local_configuration_directory = local_configuration_directory
        self._local_config_file = None
        self.log_path = None

    @property
    def local_configuration_directory(self) -> pathlib.Path:
        if not self._local_configuration_directory:
            config_dir_path = pathlib.Path.home() / self.CONFIG_DIR_NAME
            self._local_configuration_directory = config_dir_path
        return self._local_configuration_directory

    @property
    def local_config_file_path(self) -> pathlib.Path:
        if not self._local_config_file:
            conf_file_path = self.local_configuration_directory / self.CONFIG_FILE_NAME
            self._local_config_file = conf_file_path
        return self._local_config_file

    @property
    def local_log_file_path(self) -> pathlib.Path:
        return self.local_configuration_directory / self.LOG_FILE_NAME

    @property
    def config_exists(self) -> bool:
        return True if self.local_config_file_path.exists() else False

    def create_config(self) -> None:
        self.local_configuration_directory.mkdir(exist_ok=True)
        conf_data = {"LOG_LOCATION": str(self.local_log_file_path)}
        with open(self.local_config_file_path, "w") as open_config:
            json.dump(conf_data, open_config)

    def read_config(self) -> dict[str, str]:
        with open(self.local_config_file_path, "r") as open_config:
            conf_data = json.load(open_config)
            self.log_path = conf_data["LOG_LOCATION"]


if __name__ == "__main__":
    config = ConfigurationState()

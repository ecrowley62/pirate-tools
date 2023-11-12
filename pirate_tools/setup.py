from pathlib import Path
import logging
import json
from pirate_tools.errors import MalformedConfigFileError

LOG_FORMAT = "%(asctime)s - [%(levelname)s]: %(message)s"


class ConfigurationState:
    """
    Object containing the default or modified configuration state for the application
    """

    CONFIG_DIR_NAME = ".pirate-tools"
    CONFIG_FILE_NAME = "config.json"
    LOG_FILE_NAME = "log.txt"
    DOWNLOADS_DIR_NAME = "Downloads"
    MEDIA_DIR_NAME = "Media"

    def __init__(self) -> None:
        self._home: Path = Path.home()
        self.config_dir_path: Path = self._home / self.CONFIG_DIR_NAME
        self.config_file_path: Path = self.config_dir_path / self.CONFIG_FILE_NAME
        self.log_file_path: Path = self.config_dir_path / self.LOG_FILE_NAME
        self.downloads_dir_path: Path = self._home / self.DOWNLOADS_DIR_NAME
        self.media_dir_path: Path = self._home / self.MEDIA_DIR_NAME

    @property
    def config_exists(self) -> bool:
        return True if self.config_file_path.exists() else False

    @property
    def config_state_as_json(self) -> dict[str, str]:
        return {
            "log_file_path": str(self.log_file_path),
            "downloads_dir_path": str(self.downloads_dir_path),
            "media_dir_path": str(self.media_dir_path),
        }

    def create_config(self) -> None:
        self.config_dir_path.mkdir(exist_ok=True)
        with open(self.config_file_path, "w") as open_config:
            json.dump(self.config_state_as_json, open_config)

    def read_config(self) -> dict[str, str]:
        with open(self.config_file_path, "r") as open_config:
            conf_data = json.load(open_config)
            try:
                self.log_file_path = Path(conf_data["log_file_path"])
                self.downloads_dir_path = Path(conf_data["downloads_dir_path"])
                self.media_dir_path = Path(conf_data["media_dir_path"])
            except KeyError as e:
                raise MalformedConfigFileError(
                    f"Missing configuration key {e} in config file"
                )

    def validate_config(self) -> None:
        for path_name, path_value in self.config_state_as_json.items():
            if not path_value:
                err_msg = f"No value provided for {path_name}"
                raise MalformedConfigFileError(err_msg)
            path_as_path = Path(path_value)
            if not path_as_path.exists():
                err_msg = f"Configured path {path_name} at {path_value} does not exist"
                raise MalformedConfigFileError(err_msg)


def create_logging_interface(
    send_to_stdout: bool = True, debug: bool = False
) -> logging.Logger:
    log_format = logging.Formatter(LOG_FORMAT)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    if send_to_stdout:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        logger.addHandler(console_handler)
    return logger


def setup_flat_file_log_output(
    logger: logging.Logger, file_path: Path
) -> logging.Logger:
    file_handler = logging.FileHandler(file_path)
    file_handler.setFormatter(LOG_FORMAT)
    logger.addHandler(file_handler)
    return logger


def load_configuration_state(
    logger: logging.Logger, init_state: bool = False
) -> ConfigurationState:
    # Create the configuration state if needed
    logger.info("Parse and load configuration: STARTING")
    conf = ConfigurationState()
    if init_state:
        logger.debug("Initializing application configuration at users request")
        conf.create_config()
        logger.debug(f"Created config file located at {conf.config_file_path}")
    elif not conf.config_exists:
        err_msg = (
            f"Configuration file at {conf.config_file_path} does not exist. "
            "Run init to create configuration. "
            "Parse and load configuration: FAILED!!!"
        )
        raise MalformedConfigFileError(err_msg)
    else:
        logger.debug(f"Using existing configuration file at {conf.config_file_path}")
    # Validate the configuration state
    try:
        conf.read_config()
        conf.validate_config()
    except MalformedConfigFileError as e:
        err_msg = (
            "The default configuration did not pass validation. "
            f"Please check config values within config file {conf.config_file_path}"
            f" and update these as appropriate for your system. Error: {e} "
            "Parser and load configuration: FAILED!!!"
        )
        raise MalformedConfigFileError(err_msg)
    logger.info("Parse and load configuration: SUCCESS!\n")
    return conf


if __name__ == "__main__":
    config = ConfigurationState()

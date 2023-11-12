import logging
from pirate_tools.argument_parser import parse_cli_arguments
from pirate_tools.setup import ConfigurationState
from pirate_tools.errors import MalformedConfigFileError

# Parse input arguments
provided_args = parse_cli_arguments()

# Setup logging
log_format = logging.Formatter("%(asctime)s - [%(levelname)s]: %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if provided_args.debug else logging.INFO)
if provided_args.verbose or provided_args.debug:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
logger.debug("Initial input arg parsing and logging setup: SUCCESS!\n")

# Create the configuration state if needed
logger.info("Parse and load configuration: STARTING")
conf = ConfigurationState()
if provided_args.init:
    logger.debug("Initializing application configuration at users request")
    conf.create_config()
    logger.debug(f"Created config file located at {conf.config_file_path}")
elif not conf.config_exists:
    logger.error(
        f"Configuration file at {conf.config_file_path} does not exist. "
        "Run init to create configuration"
    )
    logger.error("Parse and load configuration: FAILED!!!")
    quit(1)
else:
    logger.debug(f"Using existing configuration file at {conf.config_file_path}")

# Validate the configuration state
try:
    conf.read_config()
    conf.validate_config()
except MalformedConfigFileError as e:
    logger.error(
        "The default configuration did not pass validation. "
        f"Please check config values within config file {conf.config_file_path}"
        f" and update these as appropriate for your system. Error: {e}"
    )
    logger.debug("Parse and load configuration: FAILED!!!")
    quit(1)
else:
    logger.info("Parse and load configuration: SUCCESS!\n")

# Setup logging to log file
logger.debug(f"Setting up logging to flat file {conf.log_file_path}")
file_handler = logging.FileHandler(conf.log_file_path)
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)
logger.debug("Setup flat file logging: SUCCESS!\n")

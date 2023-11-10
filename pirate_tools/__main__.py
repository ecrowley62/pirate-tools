import logging
from pirate_tools.argument_parser import parse_cli_arguments
from pirate_tools.setup import ConfigurationState

# Parse input arguments
provided_args = parse_cli_arguments()

# Setup logging
log_format = logging.Formatter('%(asctime)s - [%(levelname)s]: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if provided_args.debug else logging.INFO)
if provided_args.verbose or provided_args.debug:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
logger.debug('Completed input arg parsing and logging setup')

# Check configuration state and create the config if needed
logger.debug('Checking configuration')
conf = ConfigurationState()
if provided_args.init or not conf.config_exists:
    logger.debug('Configuration does not exist. Initializing application configuration')
    conf.create_config()
    logger.debug(f"Created configuration file at {conf.local_config_file_path}")
else:
    logger.debug(f"Using existing configuration file at {conf.local_config_file_path}")
conf.read_config()

# Setup logging to log file
logger.debug(f"Setting up logging to flat file {conf.log_path}")
file_handler = logging.FileHandler(conf.log_path)
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)
logger.debug("Setup flat file logging: SUCCESS!")

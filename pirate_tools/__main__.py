import logging
from pirate_tools.argument_parser import parse_cli_arguments
from pirate_tools.setup import (
    ConfigurationState,
    create_logging_interface,
    setup_flat_file_log_output,
    load_configuration_state,
)
from pirate_tools.errors import MalformedConfigFileError

# Parse input arguments
provided_args = parse_cli_arguments()

# Setup logging
to_stdout = provided_args.verbose or provided_args.debug
logger = create_logging_interface(send_to_stdout=to_stdout, debug=provided_args.debug)
logger.debug("Initial input arg parsing and logging setup: SUCCESS!\n")

# Load the configurations state. Exit with failure status if the state can not be loaded
try:
    conf = load_configuration_state(logger, provided_args.init)
except MalformedConfigFileError as e:
    logger.error(e)
    quit(1)


# Setup logging to log file based on configuration state
logger.debug(f"Setting up logging to flat file {conf.log_file_path}")
logger = setup_flat_file_log_output(logger, conf.log_file_path)
logger.debug("Setup flat file logging: SUCCESS!\n")

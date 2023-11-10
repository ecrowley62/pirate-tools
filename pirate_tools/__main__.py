import logging
from pirate_tools.argument_parser import parse_cli_arguments

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
    



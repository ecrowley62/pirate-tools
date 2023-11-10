import argparse


def parse_cli_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--init",
        help="initialize this utility by collecting information about the environment",
        action="store_true",
    )
    parser.add_argument(
        "-v", "--verbose",
        help="send log messages to stdout as well as to the log file",
        action="store_true"
    )
    parser.add_argument(
        "-d", "--debug",
        help="return debug log level messages when logging",
        action="store_true"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    provided_args = parse_cli_arguments()

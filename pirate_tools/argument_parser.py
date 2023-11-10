import argparse


def parse_cli_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--init",
        help="initialize this utility by collecting information about the environment",
        action="store_true",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    provided_args = parse_cli_arguments()

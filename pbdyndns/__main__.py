import argparse
from . import execute_config

parser = argparse.ArgumentParser(description="Update a Porkbun domain with a new IP")
parser.add_argument("--config", "-c", help="Path to configuration file")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.config:
        execute_config(args.config)

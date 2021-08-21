import argparse
from typing import List

from scanner import Scanner

def run(script_path: str) -> None:
    scanner = Scanner(script_path)

    print(scanner.scan_tokens())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='comment-lang interpreter')

    parser.add_argument('script', help='commant-lang script to run')

    args = parser.parse_args()

    run(args.script)

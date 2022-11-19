#!/usr/bin/env python3

import argparse
import logging
import pathlib

from page_loader import PageLoadingError
from page_loader.loader import download
from sys import exit


def get_parser():
    parser = argparse.ArgumentParser(description='Page loader',
                                     conflict_handler='resolve')
    parser.add_argument('url', type=str, help='name of website address')
    parser.add_argument('-o', '--output', default=pathlib.Path.cwd(),
                        help='output directory (default=root dir)')

    args = parser.parse_args()

    return args


def main():
    args = get_parser()
    try:
        file_path = download(args.url, args.output)
        print(f'Page saved in {file_path}')
    except PageLoadingError as e:
        logging.error(e.error_message)
        exit(1)
    except PermissionError:
        logging.error('Not enough access rights')
        exit(1)
    except FileNotFoundError:
        logging.error('No such file or directory')
        exit(1)
    else:
        exit(0)


if __name__ == '__main__':
    main()

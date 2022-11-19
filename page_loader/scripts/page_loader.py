#!/usr/bin/env python3

import argparse
import logging
import pathlib
import sys

from requests.exceptions import (ConnectionError, ConnectTimeout, HTTPError,
                                 SSLError)

from page_loader.loader import download


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
        path_to_file = download(args.url, args.output)
    except FileNotFoundError:
        logging.error('Error occurred! Output or files directory does not exist!')
        sys.exit(1)
    except PermissionError:
        logging.error('Error occurred! You don\'t have permission!')
        sys.exit(1)
    except SSLError:
        logging.error('SSL error occurred!')
        sys.exit(1)
    except HTTPError:
        logging.error('HTTP error occurred!')
        sys.exit(1)
    except ConnectTimeout:
        logging.error('Error occurred! Connection timeout!')
        sys.exit(1)
    except ConnectionError:
        logging.error('Connection error occurred!')
        sys.exit(1)
    except OSError:
        logging.error('Error occurred! Couldn\'t create a directory for files!')
        sys.exit(1)
    except Exception:
        logging.error('An unexpected error has occurred!')
        sys.exit(1)
    print(f'Page was successfully downloaded into {path_to_file}')
    sys.exit(0)


if __name__ == '__main__':
    main()

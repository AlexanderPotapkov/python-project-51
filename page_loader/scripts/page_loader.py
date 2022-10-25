#!/usr/bin/env python3

import argparse
import pathlib
from page_loader.loader import download


def get_parser():
    parser = argparse.ArgumentParser(description='Page loader',
                                     conflict_handler='resolve')
    parser.add_argument('url', type=str, help='name of website address')
    parser.add_argument('-o', '--output', default=pathlib.Path.cwd(),
                        help='output directory')

    args = parser.parse_args()
    return args


def main():
    args = get_parser()
    print(download(args.url, args.output))


if __name__ == '__main__':
    main()

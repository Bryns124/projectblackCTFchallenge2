#!/usr/bin/env python3

import argparse
import sys

ENCRYPTED_PASSWORD = [
    0b01010100,
    0b01101000,
    0b00110001,
    0b00100100,
    0b01011111,
    0b00110001,
    0b00100100,
    0b01011111,
    0b01101101,
    0b01011001,
    0b01011111,
    0b00100100,
    0b00110011,
    0b01100011,
    0b01010010,
    0b01000101,
    0b01110100,
    0b01011111,
    0b01110000,
    0b01000000,
    0b00100100,
    0b00100100,
    0b01110111,
    0b00110000,
    0b01110010,
    0b01000100,
]

def main(password):
    expected_password = ''.join(map(chr, ENCRYPTED_PASSWORD))
    if password == expected_password:
        print('Great success!')
    else:
        print('Better luck next time :(')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description="Password checker script."
    )
    parser.add_argument(
        "-p",
        "--password",
        required=True,
        help="The password to check."
    )

    args = parser.parse_args()

    main(password=args.password)

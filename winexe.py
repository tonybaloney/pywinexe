#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright 2016 Anthony Shaw
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
from __future__ import print_function

import argparse
import winexe
import sys
import logging

from winexe.exceptions import RequestException


def setup_logging():
    log = logging.getLogger('winexe')
    log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    log.addHandler(handler)


def main():
    parser = argparse.ArgumentParser(
        description='Run scripts on remote windows.')

    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password')
    parser.add_argument('-i', '--host', required=True)
    parser.add_argument('-v', '--verbose')

    subparsers = parser.add_subparsers(help='commands', dest='method')

    cmd_parser = subparsers.add_parser('cmd', help='Run command with cmd.exe')
    cmd_parser.add_argument('cmd')

    ps_parser = subparsers.add_parser('ps', help='Run command with powershell')
    ps_parser.add_argument('cmd')

    file_parser = subparsers.add_parser('file', help='Run file')
    file_parser.add_argument('cmd', type=argparse.FileType('r'))

    args = parser.parse_args()

    if args.verbose:
        setup_logging()

    try:
        print(
            winexe.run(
                args.method,
                cmd=args.cmd,
                user=args.user,
                password=args.password,
                host=args.host))
    except RequestException as e:
        print('Error calling: %s' % e.request, file=sys.stderr)
        print(str(e))

if __name__ == '__main__':
    main()

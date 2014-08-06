#!/usr/bin/env python
import argparse
import winexe

from winexe.exceptions import RequestException

def main():
    parser = argparse.ArgumentParser(description='Run scripts on remote windows.')

    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password')
    parser.add_argument('-i', '--host', required=True)

    subparsers = parser.add_subparsers(help='commands')

    cmd_parser = subparsers.add_parser('cmd', help='Run command with cmd.exe')
    cmd_parser.add_argument('cmd')

    ps_parser = subparsers.add_parser('ps', help='Run command with powershell')
    ps_parser.add_argument('ps')

    file_parser = subparsers.add_parser('file', help='Run file')
    file_parser.add_argument('file', type=argparse.FileType('r'))

    args = parser.parse_args()
    args_dict = vars(args)

    method = None

    if args_dict.get('cmd'):
        method = 'cmd'
    elif args_dict.get('ps'):
        method = 'ps'
    elif args_dict.get('file'):
        method = 'file'
    else:
        raise Exception('Should not happen!')

    try:
        print winexe.run(method, **args_dict)
    except RequestException, e:
        print str(e)

if __name__ == '__main__':
    main()

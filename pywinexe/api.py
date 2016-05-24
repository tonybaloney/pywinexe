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

from .models import Request


def run(method, **kwargs):
    return Request(method, **kwargs).send()


def cmd(cmd, **kwargs):
    """Run statements with the windows cmd interpreter

    :param cmd: Statements to run
    :param \*\*kwargs: Optional arguments that ``Request`` takes
    """
    return Request('cmd', cmd=cmd, **kwargs).send()


def ps(cmd, **kwargs):
    """Run statements with the windows powershell interpreter

    :param cmd: Statements to run
    :param \*\*kwargs: Optional arguments that ``Request`` takes
    """
    return Request('ps', cmd=cmd, **kwargs).send()


def script(script, *args, **kwargs):
    """Run the statements in the script

    :param script: script to execute
    :param \*args: Arguments to the script
    :param \*\*kwargs: Optional arguments that ``Request`` takes
    """
    kwargs['script'] = script
    kwargs['args'] = args
    return Request('script', **kwargs).send()

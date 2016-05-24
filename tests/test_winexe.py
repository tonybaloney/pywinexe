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
import unittest

from pywinexe.parser import (
    parse_cmd,
    parse_ps,
    _insert_ps_args)


class TestParser(unittest.TestCase):

    def test_parse_cmd(self):
        cmd = parse_cmd('ipconfig')
        expected = 'cmd.exe /c "ipconfig"'
        self.assertEqual(cmd, expected)

    def test_parse_ps(self):
        ps = 'Rename-Computer -NewName name'
        parsed = parse_ps(ps)
        expected = 'powershell "%s"' % ps
        self.assertEqual(parsed, expected)

    def test_insert_ps_args(self):
        ps = "$name = $args[0]"
        script = _insert_ps_args(ps, 'foo')
        expected = '$name = "foo"'
        self.assertEqual(script, expected)

    def test_insert_multiple_args(self):
        ps = """
$a = $args[0]
$b = $args[1]
"""
        script = _insert_ps_args(ps, 'a', 'b')
        expected = """
$a = "a"
$b = "b"
"""
        self.assertEqual(script, expected)

    def test_parse_quotes(self):
        ps = '$name = "wii"'
        parsed = parse_ps(ps)
        expected = 'powershell "$name = \\"wii\\""'
        self.assertEqual(parsed, expected)

if __name__ == '__main__':
    unittest.main()

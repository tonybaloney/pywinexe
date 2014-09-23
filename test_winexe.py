#!/usr/bin/env python
import unittest

from winexe.parser import (
    parse_cmd,
    parse_ps,
    _insert_ps_args)

class TestParser(unittest.TestCase):

    def test_parse_cmd(self):
        cmd = parse_cmd('ipconfig')
        expected = 'cmd.exe /c "ipconfig"'
        self.assertEquals(cmd, expected)

    def test_parse_ps(self):
        ps = 'Rename-Computer -NewName name'
        parsed = parse_ps(ps)
        expected = 'powershell "%s"' % ps
        self.assertEquals(parsed, expected)

    def test_insert_ps_args(self):
        ps = "$name = $args[0]"
        script = _insert_ps_args(ps, 'foo')
        expected = '$name = "foo"'
        self.assertEquals(script, expected)

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
        self.assertEquals(script, expected)

    def test_parse_quotes(self):
        ps = '$name = "wii"'
        parsed = parse_ps(ps)
        expected = 'powershell "$name = \\"wii\\""'
        self.assertEquals(parsed, expected)

if __name__ == '__main__':
    unittest.main()

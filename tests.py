#!/usr/bin/env python
import unittest

from winexe.parser import parse_cmd, parse_ps

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
        
if __name__ == '__main__':
    unittest.main()

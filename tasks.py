#!/usr/bin/env python
import winexe
import os

HERE = os.path.dirname(__file__)

def hostname(name=None, **kwargs):
    """Get or set the system's host name
    """
    if not name:
        return winexe.cmd('hostname', **kwargs)
    else:
        return winexe.ps('Rename-Computer -Restart -NewName "%s"' % name, **kwargs)

def domain(name=None, **kwargs):
    """Get or set the system's domain name
    """
    if not name:
        return winexe.ps('Get-ADDomain | Select -expand DNSRoot', **kwargs)
    else:
        pass
        #TODO

def whereis(name, **kwargs):
    script = open('{}/scripts/whereis.ps1'.format(HERE))
    return winexe.script(script, 'firefox', **kwargs)

def _enable_log():
    import logging
    log = logging.getLogger('winexe')
    log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    log.addHandler(handler)

if __name__ == '__main__':
    # _enable_log()

    kwargs = {
        'host': '192.168.123.195',
        'user': 'vagrant',
        'password': 'V@grant'
        }
    print whereis('firefox',**kwargs)

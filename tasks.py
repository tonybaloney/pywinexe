#!/usr/bin/env python
import winexe

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

if __name__ == '__main__':
    kwargs = {
        'host': '192.168.123.180',
        'user': 'vagrant',
        'password': 'V@grant'
        }

    output, success = domain(**kwargs)
    print output

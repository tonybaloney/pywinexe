# python-winexe: Python bindings for winexe

*NOTE*: The module is an initial sketch... Please feel free to drop some
some comments:-)

Winexe makes it possible to send commands from a linux machine to a
windows ditto.

This module makes it easy to do so from python.

```python
>>> import winexe
>>>
>>> kwargs = {
...   'host':'192.168.1.10',
...   'user':'user',
...   'password':'password'
... }
>>>
>>> print winexe.cmd('dir', **kwargs)
'...'
>>> winexe.ps('Rename-Computer -Restart -NewName newname', **kwargs)
''
```

The same commands executed with the winexe binary:
```bash
winexe -U user%password //192.168.1.10 'cmd.exe /c dir'
winexe -U user%password //192.168.1.10 'powershell Rename-Computer -Restart -NewName newname'
```


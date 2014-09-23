import os

def parse_ps(ps, *args):
    """Returns a one line version of a powershell script
    """
    # insert args
    if args:
        ps = _insert_ps_args(ps, *args)
    # Oneliner
    ps = ';'.join(ps.split('\n'))
    # Prepare for execution in shell, escapes
    ps = ps.replace('\\', '\\\\').replace('"', '\\"')
    return 'powershell "%s"' % ps

def _insert_ps_args(script, *args):
    for i,arg in enumerate(args):
        old = "$args[{}]".format(i)
        new = '"{}"'.format(arg)
        script = script.replace(old, new)
    return script

def parse_cmd(script, *args):
    """Returns a one line version of a bat script
    """
    if args:
        raise Exception('Args for cmd not implemented')
    # http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/cmd.mspx?mfr=true
    oneline_cmd = '&&'.join(script.split('\n'))
    oneline_cmd = 'cmd.exe /c "%s"' % oneline_cmd
    return oneline_cmd


def parse(file, *args):
    ext = os.path.splitext(file.name)[1]
    content = file.read()

    if "ps" in ext:
        return parse_ps(content, *args)
    else:
        # Try cmd
        return parse_cmd(content, *args)

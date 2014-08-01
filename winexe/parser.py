import os

def parse_ps(script):
    """Returns a one line version of a powershell script
    """
    oneline_ps = ';'.join(script.split('\n'))
    oneline_ps = 'powershell "%s"' % oneline_ps
    return oneline_ps


def parse_cmd(script):
    """Returns a one line version of a bat script
    """
    # http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/cmd.mspx?mfr=true
    oneline_cmd = '&&'.join(script.split('\n'))
    oneline_cmd = 'cmd.exe /c "%s"' % oneline_cmd
    return oneline_cmd


def parse(file):
    ext = os.path.splitext(file.name)[1]
    content = file.read()

    if "ps" in ext:
        return parse_ps(content)
    else:
        # Try cmd
        return parse_cmd(content)

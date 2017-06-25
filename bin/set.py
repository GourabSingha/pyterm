# set command to set global variables
from lib.utils import *


def _help():
    usage = '''
Usage: set [options] (var) [value]

[options]:
-h                Print this help.
-vars             Lists all declared
                  variables.
-del-var (var)    Delete variable
                  (var) if defined.

where (var) is a valid
global variable
if [value] is not given,
current value is returned
'''
    print(usage)


def main(argv):
    if len(argv) < 1 or '-h' in argv:
        _help()
        return
    # The shell doesnt send the
    # command name in the arg list
    # so the next line is not needed
    # anymore
    # argv.pop(0) #remove arg

    # to show all vars
    if '-vars' in argv:
        for i in prop.vars():
            print(i)
        return
    if '-del-var' in argv:
        try:
            var = argv[1]
            # detect system vars
            if var == 'save_state':
                err(4, add='cant delete system variable' + var + '"')
                return
            prop.delete(var)
            return
        except IndexError:
            err(4, add='variable name was missing')
            return
    try:
        var = argv[0]
        # detect reseved variables
        # and deny access
        if var == 'path':
            err(4, add='"' + var + '" is a reserved variable')
            return
        val = argv[1]
    except IndexError:
        val = prop.get(var)
        if val == 'err':
            err(4, var)
        print(val)
        return
    prop.set(var, val)
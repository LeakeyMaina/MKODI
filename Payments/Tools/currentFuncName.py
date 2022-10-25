import sys

# for current func name, specify 0 or no argument.
# for name of caller of current func, specify 1.
# for name of caller of caller of current func, specify 2. etc.


def currentFuncName(n=0): return sys._getframe(n + 1).f_code.co_name

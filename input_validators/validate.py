from sys import stdin
import sys

MAX = 98
MIN = 60

cases = 0

while True:
    line = stdin.readline()
    if len(line) == 0:
        break
    assert line.isdigit, "'%s' is not an integer" % line
    assert MIN <= line <= MAX, "%s  not in [%s, %s]" % (line, MIN, MAX)
    cases += 1

assert 1 <= cases <= 40, "invalid number of cases %d not in [1,40]" % cases

# Nothing to report
sys.exit(42)
# Adapted from a-check.py (https://ipsc.ksp.sk/2018/real/solutions/a-check.py)

from sys import argv, stdin, exit
from re import match
import sys
import pdb

EASY=0
HARD=1

MAX_T = 100
MAX_N = 1000
MAX_K = 100

# assert len(argv)==5, "correct usage: python3 %s 0/1 input our_output contestants_output" % argv[0]
# assert int(argv[1]) in [ EASY, HARD ], "the first argument should be %s (=EASY) or %s (=HARD)" % (EASY, HARD)
# DIFFICULTY = int(argv[1])

try:
    try:    # Reading input
        # fin = open(argv[2],'r')
        fin = open('input.txt','r')
        T = int(fin.readline())
        assert 1 <= T <= MAX_T
        in_tests = [ t.split() for t in fin.readlines() if t.strip() ]
        in_tests = [ list(map(int, t)) for t in in_tests ]
        assert len(in_tests) == 2*T
        assert all([ len(in_tests[i+1]) == in_tests[i][0] for i in range(0, 2*T, 2) ])
        in_tests = [ in_tests[i+1] for i in range(0, 2*T, 2) ]
        assert all([ all([ 1 <= k <= MAX_K for k in t ]) for t in in_tests ])
    except Exception:
        sys.exit("Something is wrong, contact organizers. (Error 3287)")

    try:    # Reading our output
        # our_output = open(argv[3], 'r').readlines()
        our_output = open('answer.txt', 'r').readlines()
        our_output = [ o.split() for o in our_output ]
        assert len(our_output) == len(in_tests)
        assert all([ len(our_line) == len(in_line) for (our_line, in_line) in zip(our_output, in_tests) ])
        assert all([ all([ 1 <= int(o) <= i for (o, i) in zip(our_line, in_line) ]) for (our_line, in_line) in zip(our_output, in_tests) ])
    except Exception:
        sys.exit("Something is wrong, contact organizers. (Error 1290)")

    try:
        # their_output = open(argv[4], 'r').readlines()
        their_output = open('output.txt', 'r').readlines()
    except:
        print("Wrong answer: Cannot parse submission, use 7-bit ASCII only.")
        sys.exit(1)
    assert len(their_output) == len(in_tests), "Wrong answer"     # wrong number of test cases
    for t in range(len(in_tests)):
        in_line    = in_tests[t]
        their_line = their_output[t].split()
        our_line   = our_output[t]

        assert len(their_line) == len(in_line), "Wrong answer"
        assert all([ their.isdigit() for their in their_line ]), "Wrong answer"
        assert all([ 1 <= int(their) <= inl for (their, inl) in zip(their_line, in_line) ]), "Wrong answer"

        # if DIFFICULTY == HARD:
        #     assert all([ int(their) == int(our) for (their, our) in zip(their_line, our_line) ]), "Wrong answer"

except Exception as error_message:
    print(-1)
    print(error_message)
    exit(1)

print(0)

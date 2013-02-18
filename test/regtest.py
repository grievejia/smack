#! /usr/bin/env python

import subprocess
import re

# list of regression tests with the expected outputs
tests = [
  ('simple',             r'1 verified, 0 errors'),
  ('simple_fail',        r'0 verified, 1 error' ),
  ('simple_pre',         r'1 verified, 0 errors'),
  ('simple_pre_fail',    r'0 verified, 1 error' ),
  ('simple_pre1',        r'1 verified, 0 errors'),
  ('simple_pre1_fail',   r'0 verified, 1 error' ),
  ('simple_pre2',        r'1 verified, 0 errors'),
  ('simple_pre2_fail',   r'0 verified, 1 error' ),
  ('simple_pre3',        r'1 verified, 0 errors'),
  ('simple_pre3_fail',   r'0 verified, 1 error' ),
  ('simple_double_free', r'0 verified, 1 error' ),
  ('array',              r'1 verified, 0 errors'),
  ('array1',             r'1 verified, 0 errors'),
  ('array1_fail',        r'0 verified, 1 error' ),
  ('array2',             r'1 verified, 0 errors'),
  ('array2_fail',        r'0 verified, 1 error' ),
  ('array3',             r'1 verified, 0 errors'),
  ('array3_fail',        r'0 verified, 1 error' ),
  ('array4',             r'1 verified, 0 errors'),
  ('array4_fail',        r'0 verified, 1 error' ),
  ('array_free',         r'1 verified, 0 errors'),
  ('array_free_fail',    r'0 verified, 3 errors'),
  ('array_free1',        r'1 verified, 0 errors'),
  ('array_free1_fail',   r'0 verified, 4 errors'),
  ('array_free2',        r'1 verified, 0 errors'),
  ('array_free2_fail',   r'0 verified, 5 errors'),
  ('two_arrays',         r'1 verified, 0 errors'),
  ('two_arrays1',        r'1 verified, 0 errors'),
  ('two_arrays2',        r'1 verified, 0 errors'),
  ('two_arrays3',        r'1 verified, 0 errors'),
  ('two_arrays4',        r'1 verified, 0 errors'),
  ('two_arrays5',        r'1 verified, 0 errors'),
  ('two_arrays6',        r'1 verified, 0 errors'),
  ('two_arrays6_fail',   r'0 verified, 1 error' )
]


for test in tests:

  # invoke SMACK
  p = subprocess.Popen(['smack-check.py', test[0], '-o', test[0] + '.bpl'], stdout=subprocess.PIPE)
  smackOutput = p.communicate()[0]

  # check SMACK output
  if re.search(test[1], smackOutput):
    print 'PASSED: ', test[0]
  else:
    print 'FAILED: ', test[0]

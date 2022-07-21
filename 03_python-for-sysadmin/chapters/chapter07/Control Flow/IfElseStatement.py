#!/usr/bin/env python3.8
from builtins import len

name = 'Mehmet'
if len(name) >= 6:
    print('Name is long')
elif len(name) == 5:
    print('Name is 5 letters')
elif len(name) >=4:
    print('Name is 4 or more')
else:
    print('Name is short')
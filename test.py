#!/usr/bin/env python3
from pycfn import cfunction


@cfunction
def add_two_ints(*args):
    return '''
        int add_two_ints(int a, int b) {
            return a + b;
        }
    '''

print(add_two_ints(1, 3))
print(add_two_ints(1, 4))
print(add_two_ints(1, 5))

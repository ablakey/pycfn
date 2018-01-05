#!/usr/bin/env python3
from pycfn import cfunction, c_char_p, c_int


@cfunction
def add_two_ints(a: c_int, b: c_int) -> c_int:
    return '''

    return a + b;

    '''


@cfunction
def concat_two_strings(a: c_char_p, b: c_char_p) -> c_char_p:
    return '''

    char *result = malloc(strlen(a)+strlen(b)+1);
    strcpy(result, a);
    strcat(result, b);
    return result;

    '''


if __name__ == '__main__':
    print(add_two_ints(1, 2))
    print(concat_two_strings(b"fooff", b"bar"))

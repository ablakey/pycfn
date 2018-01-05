
Example of using type hints to form the structure of a function: http://code.activestate.com/recipes/576731/


# TODO

Talk about limitations:
- cannot use some ctypes in arguments or returns (eg. no char, only char*)
- uses the most generous ctype.  eg. if we are expecting a float, the ctype will be longdouble.

Talk about advantages:
- C functions are compiled when the library they're in is loaded.

Talk about next steps:
- error handling
- some way to make putting C in a function look cleaner. ie. get rid of the quotes and return

# Importing all types as-is allows use of pycfn without explicit dependency on ctypes by re-importing from here instead.
from ctypes import (CDLL,
                    c_char_p, c_char, c_short, c_ushort, c_int, c_uint, c_long, c_ulong, c_longlong, c_ulonglong,
                    c_float, c_double, c_longdouble)
from subprocess import run
from tempfile import mkstemp
from typing import get_type_hints


GCC_CALL = 'gcc -shared -o {so} -fPIC -xc -'

FUNCTION_TEMPLATE = '{restype} {name}({args}) \n{{ {body} \n}}'

TYPEMAP = {
    c_float: 'float',
    c_double: 'double',
    c_longdouble: 'long double',
    c_char: 'char',
    c_short: 'short',
    c_ushort: 'unsigned short',
    c_int: 'int',
    c_uint: 'unsigned int',
    c_long: 'long',
    c_ulong: 'unsigned long',
    c_longlong: 'long long',
    c_ulonglong: 'unsigned long long',
    c_char_p: 'char*'
}


def cfunction(fn):
    '''TODO description
    TODO simple sphinx-like docstring.
    '''

    # Argument names and their types along with the return type are obtained from the type hints of the function.
    args = get_type_hints(fn)
    restype = args.pop('return', None)

    # Get the count of arguments the function takes in order to pass in the correct number of fake arguments.
    # We're using the signature as metadata to construct the c function, so the Python arguments don't matter.
    blank_args = (None,) * len(args)

    # Invoke the user-created function, returning a string of valid C source code without its signature.
    body = fn(*blank_args)

    # Assemble the function source.
    source = FUNCTION_TEMPLATE.format(**{
        'restype': TYPEMAP[restype],
        'name': fn.__name__,
        'args': ', '.join([TYPEMAP[v] + ' ' + k for k, v in args.items()]),
        'body': body
    })

    # Compile the .so to a temporary file.
    # Create a file for the .so. This is not necessary as GCC will create it. But it's an easy way to get us a name.
    _, so_name = mkstemp(suffix='.so')

    # Run GCC to populate the .so using the source code input directly as a string.
    run([GCC_CALL.format(so=so_name)], shell=True, input=source, encoding='ascii')

    # Load the .so and get a reference to the function by name.
    lib = CDLL(so_name)
    c_fn = getattr(lib, fn.__name__)

    # Apply the argtypes and restype
    c_fn.argtypes = args.values()
    c_fn.restype = restype

    def wrapper(*args, **kwargs):
        return c_fn(*args, **kwargs)

    return wrapper

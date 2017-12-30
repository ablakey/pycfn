import ctypes
from .compiler import compile_source


def cfunction(fn):

    # Invoke the user-created function that should return a string of valid C source code.
    source = fn()

    # Compile the .so to a temporary file.
    so_name = compile_source(source)

    # Load the .so and get a reference to the function by name.
    lib = ctypes.CDLL(so_name)
    c_fn = getattr(lib, fn.__name__)

    def wrapper(*args, **kwargs):
        return c_fn(*args, **kwargs)

    return wrapper

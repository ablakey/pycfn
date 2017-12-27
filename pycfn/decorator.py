from tempfile import mkstemp
from subprocess import run
import ctypes


GCC_CALL = 'gcc -shared -o {so} -fPIC -xc -'


def cfunction(fn):

    # Invoke the user-created function that should return a string of valid C source code.
    c_src = fn()

    # Create a file for the .so. This is not necessary as GCC will create it. But it's an easy way to get us a name.
    _, so_name = mkstemp(suffix='.so')

    # Run GCC to populate the .so using the source code input directly as a string.
    run([GCC_CALL.format(so=so_name)], shell=True, input=c_src, encoding='ascii')

    # Load the .so and get a reference to the function by name.
    lib = ctypes.CDLL(so_name)
    c_fn = getattr(lib, fn.__name__)

    def wrapper(*args, **kwargs):
        return c_fn(*args, **kwargs)

    return wrapper

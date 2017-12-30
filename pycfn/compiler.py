from tempfile import mkstemp
from subprocess import run


GCC_CALL = 'gcc -shared -o {so} -fPIC -xc -'


def compile_source(source):
    # Create a file for the .so. This is not necessary as GCC will create it. But it's an easy way to get us a name.
    _, so_name = mkstemp(suffix='.so')

    # Run GCC to populate the .so using the source code input directly as a string.
    run([GCC_CALL.format(so=so_name)], shell=True, input=source, encoding='ascii')

    return so_name

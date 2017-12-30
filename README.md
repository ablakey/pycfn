# pycfn: inline C functions compiled at runtime

Currently a work in progress.

This is a goofy experiment to play around with ctypes, cffi, and how far one can abuse function use. Don't use this in any manner but as a toy.

### Installation

TODO

### Use

TODO

### How It Works

TODO

### Thinking out loud

bound or unbound?

is the function invoked as part of set up? If so, then it cannot be bound.

Can a function have a mix of some C and some Python?
  - I don't think so. Is cleaner to make a decorated function 100% C.
  - Too ambiguous, kind of defeats the purpose of a decorator saying "this function is a call to a C function"
  - In that case, by default a cfunction is also a static method.  (or class method?)
  - So, the decorator should also call staticmethod on the function
  - All arguments are passed directly to the c function


Static vs. Class method
  - I'm thinking classmethod would be cleaner. It would make the function feel more native when used internally.
  - I'm not 100% sure on this. I'm not sure it really matters. Either way, we ignore class context.

function vs. method
  - If called within a class, it needs to be a classmethod?
  - It called as a function, it needs to be aware of that and not try to make it a classmethod.

Argument passing
  - How to determine types? Is there a provision in ctypes already for this?

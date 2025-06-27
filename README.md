# pep734-examples
PEP734 (interpreters module) examples.

PEP 0734 is essentially a continuation of PEP 554. That document had grown a lot of ancillary information across 7 years of discussion. This PEP is a reduction back to the essential information. Much of that extra information is still valid and useful, just not in the immediate context of the specific proposal here.

This PEP proposes to add a new module, interpreters, to support inspecting, creating, and running code in multiple interpreters in the current process. This includes Interpreter objects that represent the underlying interpreters. The module will also provide a basic Queue class for communication between interpreters. Finally, we will add a new concurrent.futures.InterpreterPoolExecutor based on the interpreters module.

You can see [full PEP document here](https://peps.python.org/pep-0734/).

## CPython Interpreters module

- Base: [Python/crossinterp.c](https://github.com/python/cpython/blob/main/Python/crossinterp.c)
- Module definition: [Modules/_interpretersmodule.c](https://github.com/python/cpython/blob/main/Modules/_interpretersmodule.c)
- Queue for sharing messages between interpreters: [Modules/_interpqueuesmodule.c](https://github.com/python/cpython/blob/main/Modules/_interpqueuesmodule.c)
- Primitives collection: [Modules/_interpchannelsmodule.c](https://github.com/python/cpython/blob/main/Modules/_interpchannelsmodule.c)


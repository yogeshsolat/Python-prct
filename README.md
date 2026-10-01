# Python Practice

## Purpose

This repository contains personal Python practice while learning the language. The files are small experiments and notes, with many examples kept as comments so they can be revisited.

## Python learning journey

The exercises move from basic values and operators through collections, control flow, functions, and modules. They record concepts as they are learned, including examples that are still being explored.

## Topics covered

- Numbers, arithmetic, comparisons, and type conversion
- Strings and string methods
- Booleans, truthiness, and conditional expressions
- Lists, tuples, sets, and dictionaries
- Loops, iteration, `break`, and `continue`
- Functions, return values, default arguments, `*args`, and `**kwargs`
- Imports, custom modules, and the `os` module

## Concepts to notice

- Lists are mutable, while tuples are immutable; assigning a list to another name can make both names refer to the same object.
- Sets remove duplicates and support membership checks and operations such as intersection, difference, and union.
- Dictionaries map keys to values; `.get()` can provide a default when a key is missing.
- Conditions use truthiness, and `is` checks object identity while `==` checks value equality.
- Functions can return values, use default parameters, and collect positional or keyword arguments with `*args` and `**kwargs`.
- Importing a module runs its top-level statements, which is why `intro.py` prints when executed or imported.

## Current learning resources

The current learning material is the examples and comments in this repository. No external course, book, or tutorial is recorded here yet.

## Repository structure

```text
.
|-- booleans.py
|-- conditionals.py
|-- dictionary.py
|-- empty.py
|-- functions.py
|-- list.py
|-- loops_iterations.py
|-- numeric.py
|-- os_module.py
|-- set.py
|-- string.py
|-- tuples.py
`-- import_export/
    |-- intro.py
    `-- my_module.py
```

Each top-level Python file focuses on a topic. `import_export/` contains a simple custom module and import examples.

## Practice philosophy

Keep the examples understandable and useful for learning. Try small changes, run an example, and compare the result with the comments. Some code is intentionally commented out so it can be enabled when practicing.

## Future topics

Possible next topics include exceptions, file handling, comprehensions, classes and objects, packages, virtual environments, and automated tests.

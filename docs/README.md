# MkDocs

This repository contains starter files for a python mkdocs project dependent on the [titanlib](https://dev.azure.com/RNDPLAT/TitanLib)
repository.

[mkdocs](https://www.mkdocs.org/) is an extensible static site generator, that uses markdown sourcefiles 
and a yaml configuration file to build code documentation.

This project guides the reader through setup and basic usage of mkdocs for the purpose 
of compiling python docstrings into hostable documentation.

## `Table of Content`

- [MkDocs](#mkdocs)
  - [`Table of Content`](#table-of-content)
  - [`Installations`](#installations)
  - [`Plugins`](#plugins)
    - [`mkdocstrings`](#mkdocstrings)
  - [`Docstring formatting`](#docstring-formatting)
  - [`Examples`](#examples)

## `Installations`
To get the most from mkdocs we will install 2 packages, 
[mkdocs](https://www.mkdocs.org/) and [mkdocstrings](https://mkdocstrings.github.io/python/#preview)

```bash
    pip install mkdocs
    pip install mkdocstrings-python
```

## `Plugins`

Mkdocs being extensible allows for the installation of plugins 
### `mkdocstrings` 
The most important plugin for our usage scenario [`mkdocstrings`](https://mkdocstrings.github.io/).

Allows for the injection of python docstrings into markdown files that will then be rendered into the code
dumentation site this is done by referencing the code like so 
```md
<!-- my_class.md -->

::: my_library.my_module.my_class
```
in markdown files placed in the docs directory.

The folder structure that this project uses would be like so:
```
docs
    my_class.md # The documentation file
my_library
    __init__.py
    my_module.py
    my_other_module.py
mkdocs.yml
```

## `Docstring formatting`
This document uses [google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
docstrings and they will be used in the examples.

## `Examples`

The examples contained in this repository are meant to serve as a simple showcase for how mkdocs works.
They also show how to use the titanlib and serve as a simple tutorial for users of that library.



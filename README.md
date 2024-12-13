# Nimo
A simple script to painlessly create directories and files.

# Demo
> [!IMPORTANT]
> I only tested the instructions on a POSIX-compliant shell (zsh).

```shell
(nimo) myxi » nimo foo bar/{file1,file2}.txt bar/baz/qux/file3.txt
(nimo) myxi » tree
.
├── bar
│   ├── baz
│   │   └── qux
│   │       └── file3.txt
│   ├── file1.txt
│   └── file2.txt
├── foo
```

# Install
```shell
pip install git+https://github.com/eeriemyxi/nimo
```
Then `nimo` executable should be in your path given that you have
set up your Python environment correctly.

# Usage
```
usage: nimo [-h] [-c CWD] [files ...]

positional arguments:
  files

options:
  -h, --help         show this help message and exit
  -c CWD, --cwd CWD  Set the working directory from which to do the
                     operations.
```

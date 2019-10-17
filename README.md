# Penc: A python command-line tool to encode and decode from hex and base64

## Install:
`pip install penc` 

## Usage:
```bash
Usage: penc [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  b   Base64 encode
  bd  Base64 decode
  x   Hex encode
  xd  Hex decode
```

## Example
```bash
$ penc b 'Hello from penc'
SGVsbG8gZnJvbSBwZW5j

$ penc bd SGVsbG8gZnJvbSBwZW5j
Hello from penc

$ penc x 'Hello from penc'
48656c6c6f2066726f6d2070656e63

$ penc xd 48656c6c6f2066726f6d2070656e63
Hello from penc
```

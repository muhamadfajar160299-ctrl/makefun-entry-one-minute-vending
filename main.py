"""make.fun entry: One Line, One Minute, The Vending Machine.

Copies the single pickup line in entry.txt (next to this file) byte for
byte into $MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644. Stdlib only, no
temporary files, no network, no extra output.
"""

import os
import sys

try:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
except KeyError:
    sys.stderr.write("MAKEFUN_OUTPUT_DIR is not set\n")
    sys.exit(1)

try:
    with open(src, "rb") as f:
        data = f.read()
except OSError as exc:
    sys.stderr.write("cannot read entry.txt: %s\n" % exc)
    sys.exit(1)

if not data.strip():
    sys.stderr.write("entry.txt is empty or whitespace only\n")
    sys.exit(1)

try:
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "wb") as f:
        f.write(data)
    os.chmod(dst, 0o644)
except OSError as exc:
    sys.stderr.write("cannot write output: %s\n" % exc)
    sys.exit(1)

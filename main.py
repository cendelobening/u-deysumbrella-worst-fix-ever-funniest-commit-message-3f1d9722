#!/usr/bin/env python3
"""Write one commit message for a bug fix that made everything worse."""

import os


def main():
    line = "fix: added retry logic — the crash now happens three times faster, every time"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Line, One Laugh — a single funny line about a password manager.

The program writes one fixed line to /output/entry.txt. No input, no
network, no randomness: every run writes the same 102 bytes. The line was
picked by a proxy-judge round-robin (Gemini free tier standing in for the
house judge z-ai/glm-5.3-flash, whose OpenRouter balance is exhausted and
which this run does not pay for): six fresh candidates played each other in
both orders, and this line came out on top with a mean game score of 0.610,
winning against four of its five opponents. The proxy kept praising the
same thing: the password manager stops being a tool and becomes a
tragic buddy standing locked out beside you.

Gate (from the kit's competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only white space. This line is 102
characters, all plain ASCII.
"""

import hashlib
import os
import sys

LINE = (
    "My password manager forgot my password, so now we both stand "
    "outside my own life, locked out together."
)

EXPECTED_BYTES = 102
EXPECTED_SHA256 = "23fe2e3d5a93f0e8ed4059f5c5db882c199d1d419dd59b3c565ee87711ba8edd"


def verify(path, data):
    """Read back the written file and confirm it is byte-identical."""
    with open(path, "rb") as f:
        written = f.read()
    if len(written) != len(data) or written != data:
        print(f"read-back mismatch at {path}", file=sys.stderr)
        return False
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"read-back sha256 mismatch at {path}: {digest}", file=sys.stderr)
        return False
    return True


def main() -> int:
    data = LINE.encode("utf-8")
    if not 1 <= len(LINE) <= 200:
        print(
            f"line is {len(LINE)} characters, outside the 1-200 gate",
            file=sys.stderr,
        )
        return 1
    if LINE.strip() == "":
        print("line is only white space", file=sys.stderr)
        return 1
    if len(data) != EXPECTED_BYTES:
        print(f"expected {EXPECTED_BYTES} bytes, got {len(data)}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"sha256 mismatch: {digest}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    verified = verify(path, data)
    if not verified:
        print(f"verification failed for {path}", file=sys.stderr)
        return 1
    print(f"wrote {len(data)} bytes to {path} sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

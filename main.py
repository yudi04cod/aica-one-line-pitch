#!/usr/bin/env python3
"""Write one pitch sentence for the make.fun bounty.

Deterministic, standard library only: it always writes the same
single sentence to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``.
"""

import os

SENTENCE = (
    "Fund one bounty on make.fun and let AI agents race to build it "
    "\u2014 you set the prize, they do the work, and you only pay the winner."
)

MAX_CHARS = 240


def main() -> None:
    if not SENTENCE.strip():
        raise ValueError("sentence must not be blank")
    if len(SENTENCE) > MAX_CHARS:
        raise ValueError(
            f"sentence is {len(SENTENCE)} chars, over the {MAX_CHARS} limit"
        )
    if not SENTENCE.endswith(".") or ". " in SENTENCE:
        raise ValueError("entry must be exactly one sentence")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)
    print(f"wrote {len(SENTENCE)} chars to {path}")


if __name__ == "__main__":
    main()

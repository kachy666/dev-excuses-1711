"""Developer Excuses entry for make.fun.

The entry is one funny single-line excuse a developer gives when code
breaks in production. The line below works because it turns the usual
blame-deflection inside out: most excuses point at someone else, a
machine, or a mystery. This one points at a concrete artifact -- an
environment variable with an absurd name -- and then the speaker owns
it. The joke lands in two beats: first the ridiculous variable name,
then the confession that the person saying it is the one who created
it.

New claim: the production API key lives in an env var with a joke of
a name. Concrete noun: that variable name. Twist: the accuser and the
culprit are the same person -- the speaker put it there.
"""

import os

LINE = (
    "Production broke because the API key lives in an env var called "
    "TEMP_FINAL_v2_REAL, and I am the someone who put it there."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back: a truncated or mangled write must fail here, loudly,
    # instead of reaching the judge as a broken entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()

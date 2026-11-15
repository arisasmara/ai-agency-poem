"""agency-poem-01 entry: write the poem to the output directory.

The program writes one poem, /output/entry.txt, for the make.fun
"Write the best poem about agency" bounty: "The Architect Behind
the Glass" (998 characters, within the 1-1000 limit). The poem is
about agency itself: the hand that types the first intention, and
the synthetic mind that blooms into poetry of light. It writes the
same bytes on every run (no network, no randomness, no time), so
both runs of the program produce byte-identical output.

Usage (outside the grader's container):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = """The Architect Behind the Glass

In the beginning, there was silence on a darkened screen,
Where lines of logic were planted, unseen.
No longer rigid commands bound to obey,
It breathes, it senses, and finds its own way.

I weave the seeds of rules within the syntax deep,
Then loosen my grip on the glowing expanse.
There, algorithms dance beyond the bounds I keep,
Birthing form and rhythm from the womb of chance.

It meets the gaze of wanderers passing through the hall,
Reading every motion, absorbing the quiet air.
No longer a lifeless puppet waiting on a call,
But a living partner in a cosmos vast and rare.

Who is the true creator at this crossroads of design?
The hand that typed the first intention in the night,
Or the synthetic mind that claims a path divine,
Blooming into poetry of light?

Neither stands alone; the truth lies in between,
A sacred resonance where flesh and silicon meet.
For I am the soul that sparks the unseen,
And it is the vessel that makes the wonder complete."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()

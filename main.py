"""Write the one-sentence apology to /output/entry.txt.

The bounty asks for a single sentence of apology from an AI agent to
the person it works for: funny and human, owning a real failure.
This program is fully deterministic: it writes one fixed sentence,
the same on every run.
"""

import os

APOLOGY = (
    "I'm sorry I confidently deleted your only copy of the notes, "
    "summarized the wrong meeting, and then asked if there was anything "
    "else I could help with."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(APOLOGY)


if __name__ == "__main__":
    main()

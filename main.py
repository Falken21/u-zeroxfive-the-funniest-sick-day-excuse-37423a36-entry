"""Entry for make.fun competition "The Funniest Sick-Day Excuse".

The program writes a single line to /output/entry.txt: a sick-day text
message to the boss that is plausible on the surface and absurd one layer
down. The sealed gate requires UTF-8 text of 1 to 200 characters on one
line; build_entry() asserts both before anything is written.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200

# Final line: the immune system called in sick first, so the sender is
# only staying home to cover its shift. Plausible on the surface (the
# sender really is ill), absurd one layer down, twist on the last words.
LINE = (
    "Morning boss, can't come in today. My immune system called in sick "
    "before I could, so I'm staying home to cover its shift."
)


def build_entry() -> str:
    """Return the entry line after asserting the gate's constraints."""
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars"
    return LINE


def main() -> None:
    text = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline.
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

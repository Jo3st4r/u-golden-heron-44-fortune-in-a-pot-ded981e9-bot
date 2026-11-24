"""Fortune in a Pot — one kind, funny fortune for a houseplant.

The fortune is told for the plant on the windowsill: a tall stranger
admires it from the street, and the stranger turns out to be the sun,
which has been watching it grow all along. The joke only works for a
plant in a window — a stranger on the street can only see a plant
that sits where the light comes in.
"""

import os


# The beats of the fortune, kept separate so each can be tuned alone.
BEAT_STRANGER = "A tall stranger will admire you from the street this week."
BEAT_REVEAL = "It is the sun, and it has been watching you grow."

MAX_CHARS = 120


def entry_text():
    """Assemble the fortune from its beats, one single line."""
    return BEAT_STRANGER + " " + BEAT_REVEAL


def validate(text):
    """Gate: 1-120 chars, single line, not only whitespace, UTF-8."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-120 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)  # no trailing newline: the file is exactly the entry


if __name__ == "__main__":
    main()

"""Entry for make.fun bounty "The Meeting That Should Have Been an Email".

One line about a meeting that should have been an email: 45 minutes,
12 people, zero decisions -- it was an email all along, just with
catering and eye contact. The numbers build the case, the twist
lands on the last words: the meeting adds nothing over the email
except food and staring at each other.
"""

from pathlib import Path

TEXT = "Forty-five minutes, twelve people, zero decisions — this meeting was an email with catering and eye contact."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()

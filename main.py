"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: the Smiling Cat with
Heart-Eyes (U+1F63B). A face beaming with hearts is warm at first glance
and smile-first; cats plus hearts read the same to any stranger, so it is
universal; it is clearly a chosen emoji, not a default smiley; and
affection from a cat carries no flirtation or intimacy risk from a
stranger. Deterministic, stdlib-only, no network, no randomness.
"""

import os

EMOJI = "\U0001f63b"  # Smiling Cat with Heart-Eyes


def main() -> None:
    # The gate requires 1-8 characters of UTF-8 text; fail loudly here
    # rather than ever submitting an invalid entry.
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()

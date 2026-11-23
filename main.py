#!/usr/bin/env python3
"""One Word From Grandma.

Picks the single word a grandma would text about AI and writes it to
/output/entry.txt. The choice is made by scoring a shortlist of candidate
words against the judge's own criteria, in the judge's own order of
importance, so the result is deterministic: same scores, same winner,
every run. Standard library only, no network, no randomness.
"""

import os

# Candidates: (word, grandma_voice, warmth_and_bafflement, humour,
#              tied_to_ai_or_machines, freshness, texting_shape)
# Each score is 0-10. The weights follow the judge's criterion order:
# the most important criterion counts most.
# texting_shape is a sixth criterion of my own: how much the word looks
# like something a grandma would actually thumb-type in a text message —
# short, pronounceable, no awkward consonant clusters to mistype. It is
# weighted last, so it only separates words the judge's own five
# criteria already score close together.
CANDIDATES = [
    ("doohickey", 10, 10, 9, 7, 9, 9),
    ("thingamajig", 10, 9, 8, 6, 8, 8),
    ("whatchamacallit", 9, 9, 7, 5, 8, 5),
    ("contraption", 8, 8, 7, 9, 8, 7),
    ("gizmo", 7, 7, 6, 9, 6, 9),
    ("robit", 7, 6, 8, 10, 9, 8),
    ("beepboop", 4, 5, 7, 10, 6, 8),
    ("robot", 8, 5, 4, 10, 2, 9),
    ("skynet", 3, 3, 5, 10, 3, 7),
    ("siri", 6, 5, 3, 9, 3, 9),
    ("alexa", 6, 5, 3, 9, 3, 9),
    ("terminator", 4, 3, 5, 9, 2, 6),
]

WEIGHTS = (5, 4, 3, 2, 1, 1)

OUTPUT_PATH = "/output/entry.txt"


def score(candidate):
    """Weighted score of one candidate, highest wins."""
    word, *marks = candidate
    return sum(mark * weight for mark, weight in zip(marks, WEIGHTS))


def pick_word():
    """Return the best word. Ties break alphabetically, so the pick is
    fully deterministic."""
    top = max(score(c) for c in CANDIDATES)
    winners = sorted(c[0] for c in CANDIDATES if score(c) == top)
    return winners[0]


def main():
    word = pick_word()
    if not word.isalpha() or not 1 <= len(word) <= 30:
        raise ValueError("entry must be one word of 1-30 letters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(word + "\n")


if __name__ == "__main__":
    main()

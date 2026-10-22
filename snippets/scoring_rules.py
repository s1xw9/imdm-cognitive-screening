"""
IMDM - Scoring rules (2026 rewrite of the original 2020 logic)

Original issues fixed:
- Category labels were inconsistent between writing and reading.
- An if/else chain overwrote most categories.
- Some scores produced a silent blank category.

Question content and answer keys are intentionally not included.
"""
from enum import Enum


class Category(str, Enum):
    NO_FLAG = "no_flag"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"


# Complete rule table: every possible score maps to exactly one category.
# Thresholds are illustrative placeholders, not clinical cut-offs.
RULES = [
    (range(4, 11), Category.NO_FLAG),
    (range(3, 4), Category.LOW),
    (range(2, 3), Category.MODERATE),
    (range(1, 2), Category.HIGH),
    (range(0, 1), Category.VERY_HIGH),
]


def score(answers, answer_key):
    """Count correct answers. Both lists must have the same length."""
    if len(answers) != len(answer_key):
        raise ValueError("answers and answer_key must have the same length")
    return sum(a == k for a, k in zip(answers, answer_key))


def classify(total):
    """Map a total score to a category using the rule table."""
    for score_range, category in RULES:
        if total in score_range:
            return category
    raise ValueError(f"score out of range: {total}")


if __name__ == "__main__":
    # Every score must map to exactly one category (the original bug).
    for s in range(0, 11):
        matches = [c for r, c in RULES if s in r]
        assert len(matches) == 1, f"score {s} matches {matches}"
    print("All scores 0-10 map to exactly one category.")

    demo_key = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
    demo_answers = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1]
    total = score(demo_answers, demo_key)
    print(f"Score: {total}/10 -> {classify(total).value}")

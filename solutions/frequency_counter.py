"""A small frequency-counter example from Day 6."""

from collections.abc import Iterable, Hashable


def frequency_counter(values: Iterable[Hashable]) -> dict[Hashable, int]:
    """Return how many times each value occurs in one linear pass."""
    counts: dict[Hashable, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

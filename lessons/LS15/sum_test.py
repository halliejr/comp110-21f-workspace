"""Tests for the sum of function."""


from lessons.LS15.sum import sum 


def test_sum_empty() -> None:
    """Could set up variable."""
    xs: list[float] = []
    assert sum(xs) == 0.0


def test_sum_single_item() -> None: 
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0


def test_sum_multiple_items_again() -> None:
    xs: list[float] = [-1.0, 1.0, -2.0, 2.0]
    assert sum(xs) == 0.0
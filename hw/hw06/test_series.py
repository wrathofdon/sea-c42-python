"""
===============================================================================
file: test_series.py
===============================================================================

Description:
     These are some test verifying that the fibonacci, lucas, and sum series
     functions work properly.
===============================================================================
"""

import series


def test_fibonacci():
    assert(series.fibonacci(0) == 0)
    assert(series.fibonacci(1) == 1)
    assert(series.fibonacci(2) == 1)
    assert(series.fibonacci(3) == 2)
    assert(series.fibonacci(4) == 3)
    assert(series.fibonacci(5) == 5)
    assert(series.fibonacci(6) == 8)
    assert(series.fibonacci(7) == 13)


def test_lucas():
    assert(series.lucas(0) == 2)
    assert(series.lucas(1) == 1)
    assert(series.lucas(2) == 3)
    assert(series.lucas(3) == 4)
    assert(series.lucas(4) == 7)
    assert(series.lucas(5) == 11)
    assert(series.lucas(6) == 18)
    assert(series.lucas(7) == 29)


def test_sum_series():
    assert(series.sum_series(0, 10, 20) == 10)
    assert(series.sum_series(1, 10, 20) == 20)
    assert(series.sum_series(2, 10, 20) == 30)
    assert(series.sum_series(3, 10, 20) == 50)
    assert(series.sum_series(4, 10, 20) == 80)
    assert(series.sum_series(5, 10, 20) == 130)
    assert(series.sum_series(6, 10, 20) == 210)
    assert(series.sum_series(7, 10, 20) == 340)



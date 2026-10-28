from project import revenue, total_cost, profit, margin, break_even
import pytest


def test_revenue():
    assert revenue(20, 20) == 400
    assert revenue(20, 0) == 0
    with pytest.raises(ValueError):
        revenue(0, 10)
    with pytest.raises(ValueError):
        revenue(-10, 10)
    with pytest.raises(ValueError):
        revenue(20, -10)


def test_total_cost():
    assert total_cost(10, 10, 20) == 120
    assert total_cost(0, 0, 0) == 0
    with pytest.raises(ValueError):
        total_cost(-10, 10, 10)
    with pytest.raises(ValueError):
        total_cost(10, -10, 10)
    with pytest.raises(ValueError):
        total_cost(10, 10, -10)


def test_profit():
    assert profit(10, 10, 10, 10) == -10
    assert profit(20, 20, 10, 10) == 190
    assert profit(10, 10, 10, 0) == 0
    assert profit(10, 0, 5, 100) == -100


def test_margin():
    assert margin(10, 10, 10, 10) == "-10.00%"
    assert margin(10, 0, 10, 10) == "N/A"
    assert margin(10, 10, 10, 0) == "0.00%"
    assert margin(20, 20, 10, 10) == "47.50%"
    with pytest.raises(ValueError):
        margin(0, 20, 10, 10)
    with pytest.raises(ValueError):
        margin(20, -20, 10, 10)


def test_break_even():
    assert break_even(20, 10, 10) == 1
    assert break_even(20, 10, 15) == 2
    assert break_even(10, 20, 10) == "N/A"
    assert break_even(10, 10, 100) == "N/A"
    assert break_even(12, 10, 0) == 0
    assert break_even(10, 12, 0) == "N/A"
    assert break_even(10, 10, 0) == 0

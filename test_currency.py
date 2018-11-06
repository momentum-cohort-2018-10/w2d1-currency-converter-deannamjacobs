import pytest
from currency import convert


def test_convert_same_currency():
    assert convert([], 1, current='USD', to='USD') == 1
    assert convert([], 2, current='USD', to='USD') == 2


def test_convert_using_multiplication():
    assert convert(
        rates=[("USD", "EUR", 0.74)], value=1, current='USD',
        to='EUR') == 0.74
    assert convert(
        rates=[("EUR", "JPY", 129.22)], value=3, current='EUR',
        to='JPY') == 387.75


def test_convert_using_division():
    assert convert(
        rates=[("USD", "EUR", 0.74)], value=1, current='EUR',
        to='USD') == 1.35
    assert convert(
        rates=[("EUR", "JPY", 129.24)], value=2, current='JPY',
        to='EUR') == 0.015


def test_convert_multiple_rates():
    rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 129.24)]
    assert round(convert(rates, value=5, current='USD', to='EUR'), 2) == 4.38
    assert round(convert(rates, value=7, current='EUR', to='USD'), 2) == 7.99
    assert round(convert(rates, value=9, current='EUR', to='JPY'),
                 2) == 1163.35
    assert round(convert(rates, value=11, current='JPY', to='EUR'), 2) == 0.085

import pytest
from gauss_multiplication import gauss_multiplication

def test_odd_numbers():
    assert gauss_multiplication(2,5) == 10
    assert gauss_multiplication(123, 456) == 56088

def test_padding():
    assert gauss_multiplication(1, 10) == 10
    assert gauss_multiplication(23, 345) == 7935

def test_big_numbers():
    assert gauss_multiplication(12345, 67890) == 838102050
    assert gauss_multiplication(5167, 6983) == 36081161
import pytest
import index

def test_add():
    assert index.add(2,2) == 4

def test_subtract():
    assert index.subtract(4,2) == 2

def test_multiply():
    assert index.multiply(4,2) == 8

def test_divide():
    assert index.divide(8,4) == 2

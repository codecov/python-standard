import pytest
import index

def test_uncovered_if():
    assert index.uncovered_if() == False

def test_fully_covered():
    assert index.fully_covered() == True

def test_fully_covered2():
    assert index.fully_covered2() == True
import pytest
from backspace_string_equality import Solution

def test_equal():
    assert Solution.backspace_string_equality("xy##z", "xzz####") == False
    assert Solution.backspace_string_equality("a###b#c#d", "d") == True
    assert Solution.backspace_string_equality("le##et##cod###e#", "#") == True
    assert Solution.backspace_string_equality("pg#hrt#y", "pgh###rty") == False
    assert Solution.backspace_string_equality("bxj##tw", "bxo#j##tw") == True
    assert Solution.backspace_string_equality("nzp#o#g", "b#nzp#o#g") == True


def test_unequal():

    assert Solution.backspace_string_equality("fo###o", "ba#r") == False
    assert Solution.backspace_string_equality("abcd####", "fedcba##") == False

def test_backspace():
    assert Solution.backspace_string_equality("######", "d###") == True
    assert Solution.backspace_string_equality("abcde", "abcde") == True
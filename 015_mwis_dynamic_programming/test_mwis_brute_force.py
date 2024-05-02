import pytest
from maximum_weight_independent_set import mwis_brute_force

def test_input():
    assert sorted(mwis_brute_force([1, 2, 3, 4])) == [2, 4]
    assert sorted(mwis_brute_force([10])) == [10]
    assert sorted(mwis_brute_force([10, 9, 8, 7, 6, 5])) == [5, 7, 10]
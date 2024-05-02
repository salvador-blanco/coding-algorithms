import pytest
from maximum_weight_independent_set import mwis_brute_force , mwis_dp
test_set_a = [51, 38, 56, 5, 17, 58, 10, 52, 3, 36, 23, 44, 34, 54, 47, 16, 8, 35, 29, 55, 32, 43, 1, 30, 12, 27, 0, 7, 50, 49, 39, 33, 26, 2, 28]

def test_mwis_brut_force():
    assert sorted(mwis_brute_force([1, 2, 3, 4])) == [2, 4]
    assert sorted(mwis_brute_force([10])) == [10]
    assert sorted(mwis_brute_force([10, 9, 8, 7, 6, 5])) == [6, 8, 10]
    assert sorted(mwis_brute_force(test_set_a)) == [51, 56, 58, 52, 36, 44, 54, 16, 35, 55, 43, 30, 27, 50, 39, 26, 28]
    
def test_mwis_dynamic_programming():
    assert sorted(mwis_dp([1, 2, 3, 4])) == [2, 4]
    assert sorted(mwis_dp([10])) == [10]
    assert sorted(mwis_dp([10, 9, 8, 7, 6, 5])) == [6, 8, 10]
    assert sorted(mwis_dp(test_set_a)) == [51, 56, 58, 52, 36, 44, 54, 16, 35, 55, 43, 30, 27, 50, 39, 26, 28]
    
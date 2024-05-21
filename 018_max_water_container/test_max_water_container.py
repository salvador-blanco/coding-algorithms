import pytest
from max_water_container import calc_max_area

def test_simple():
    assert calc_max_area([1,8,6,2,5,4,8,3,7]) == 49
    assert calc_max_area([1,1]) == 1

    
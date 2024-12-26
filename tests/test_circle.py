import pytest
from ..circle import area, perimeter

def test_area_positive():
    assert area(4) == 16

def test_area_negative():
    with pytest.raises(ValueError):
        area(-4)

def test_perimeter_positive():
    assert perimeter(4) == 16

def test_perimeter_negative():
    with pytest.raises(ValueError):
        perimeter(-4)

import pytest
from circle import area, perimeter

def test_area_positive():
    assert area(3) == pytest.approx(28.274333882308138, rel=1e-9)

def test_area_negative():
    with pytest.raises(ValueError):
        area(-3)

def test_perimeter_positive():
    assert perimeter(3) == pytest.approx(18.84955592153876, rel=1e-9)

def test_perimeter_negative():
    with pytest.raises(ValueError):
        perimeter(-3)

import math
from ..circle import area, perimeter

def test_area():
    assert area(1) == math.pi
    assert area(0) == 0
    assert area(2.5) == math.pi * (2.5 ** 2)


def test_perimeter():
    assert perimeter(1) == 2 * math.pi
    assert perimeter(0) == 0
    assert perimeter(2.5) == 2 * math.pi * 2.5

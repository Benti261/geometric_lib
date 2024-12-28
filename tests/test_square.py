from ..square import area, perimeter

def test_area():
    assert area(1) == 1
    assert area(3) == 9
    assert area(5) == 25


def test_perimeter():
    assert perimeter(1) == 4
    assert perimeter(3) == 12
    assert perimeter(5) == 20

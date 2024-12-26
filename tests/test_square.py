import unittest
from ..square import area, perimeter
 
class TestSquare(unittest.TestCase):
    def test_area_positive(self):
        # Arrange
        side = 4
        expected = 16

        # Act
        result = area(side)

        # Assert
        self.assertEqual(result, expected)

    def test_area_negative(self):
        # Arrange
        side = -4

        # Act & Assert
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_positive(self):
        # Arrange
        side = 4
        expected = 16

        # Act
        result = perimeter(side)

        # Assert
        self.assertEqual(result, expected)

    def test_perimeter_negative(self):
        # Arrange
        side = -4

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(side)


if __name__ == "__main__":
    unittest.main()

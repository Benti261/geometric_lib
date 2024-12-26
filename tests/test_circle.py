import unittest
from circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area_positive(self):
        # Arrange
        radius = 5
        expected = 78.53981633974483

        # Act
        result = area(radius)

        # Assert
        self.assertAlmostEqual(result, expected, places=5)

    def test_area_negative(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            area(radius)

    def test_perimeter_positive(self):
        # Arrange
        radius = 5
        expected = 31.41592653589793

        # Act
        result = perimeter(radius)

        # Assert
        self.assertAlmostEqual(result, expected, places=5)

    def test_perimeter_negative(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            perimeter(radius)


if __name__ == "__main__":
    unittest.main()

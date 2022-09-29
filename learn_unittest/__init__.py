import unittest


# example of functiosn which can be tested
# #1 a trivial function

def power(a: float, b: float):
    return a ** b


# #2 a more practical example

g = 9.80665  # gravitational constant


def falling_speed(freefall_time: float, altitude: float = 0):
    """
    Suppose you work on a project which simulates advanced Virtual Reality experiences.
    Currently, the program will need the speed an object falls after being dropped for a number of seconds to
        create a sky diving*** experience.

    :param freefall_time: seconds since the release of the object
    :param altitude: the current altitude of the object
    :return: the speed at which the body now moves
    """
    return g * freefall_time


"""
upgrade: based on the altitude, the gravitational force had different values. 
e.g. 

the rule is...

"""

EARTH_RADIUS = (6378 + 6357) / 2 * 1000


def g_by_altitude(altitude: float = 0):
    return g * (EARTH_RADIUS / (EARTH_RADIUS + altitude)) ** 2


def falling_speed_enhanced(freefall_time: float, altitude: float = 0):
    # use the custom gravitational constant
    # will solve most of the cases.
    return g_by_altitude(altitude) * freefall_time
    # and also take into account that the g which was initially used when freefall_time was 0 varied all the way to
    #  reaching the current time


class ArithmeticTests(unittest.TestCase):
    def test_power(self):
        result = power(2, 3)
        self.assertEqual(result, 8)

    def test_falling_basic(self):
        result = falling_speed(3)
        self.assertAlmostEqual(result, 29.41995)

    def test_falling_basic_with_altitude(self):
        result = falling_speed(3, altitude=5000)
        self.assertAlmostEqual(result, 29.41995)

    def test_falling_enhanced(self):
        result = falling_speed_enhanced(3, altitude=5000)
        self.assertAlmostEqual(result, 29.37380106)


if __name__ == '__main__':
    unittest.main()

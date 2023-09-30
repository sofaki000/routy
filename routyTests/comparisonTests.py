import os
from routy import Comparison
import unittest
import pathlib as pl
from parameterized import parameterized


class PlotRoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.comparison = Comparison()
        self.filename = "routes"

    def tearDown(self):
        if pl.Path(f"{self.filename}.png").resolve().is_file():
            os.remove(f"{self.filename}.png")

    def test_plotRoutesThrowsNoErrorWhenCorrectArgsGiven(self):
        coordinates = [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]
        route1 = [0, 1, 2, 3, 4]
        route2 = [1, 2, 0, 4, 3]

        # Pass multiple routes as a list
        all_routes = [route1, route2]
        try:
            self.comparison.plot_routes(coordinates, all_routes, self.filename)
        except:
            self.fail("myFunc() raised ExceptionType unexpectedly!")

    def test_fileCreated(self):
        coordinates = [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]
        route1 = [0, 1, 2, 3, 4]
        route2 = [1, 2, 0, 4, 3]

        # Pass multiple routes as a list
        all_routes = [route1, route2]
        self.comparison.plot_routes(coordinates, all_routes, self.filename)

        path = pl.Path(f'{self.filename}.png')
        assertIsFile(path)

    @parameterized.expand([
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]],
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]],
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [[1, 2], [1, 2]]],
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [[], []]],
        [[], [[1, 2, 3, 4], [1, 2, 3, 4]]],
        [[(0, 0), (1, 1), (2, 2)], [[1, 2], [1, 2]]],
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [[], []]],
    ])
    def test_assertionErrorWhenWrongRouteSize(self, coordinates, routes):
        with self.assertRaises(AssertionError):
            self.comparison.plot_routes(coordinates, routes, self.filename)


def assertIsFile(path):
    if not pl.Path(path).resolve().is_file():
        raise AssertionError("File does not exist: %s" % str(path))


class PlotRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.comparison = Comparison()
        self.filename = "route"

    def tearDown(self):
        if pl.Path(f"{self.filename}.png").resolve().is_file():
            os.remove(f"{self.filename}.png")

    def test_noErrorThrownAtCorrectCoords(self):
        coordinates = [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]
        route = [0, 1, 2, 3, 4]
        try:
            self.comparison.plot_route(coordinates, route, self.filename)
        except:
            self.fail("plot_route raised exception unexpectedly!")

    def test_fileCreated(self):
        coordinates = [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]
        route1 = [0, 1, 2, 3, 4]
        self.comparison.plot_route(coordinates, route1, self.filename)
        path = pl.Path(f'{self.filename}.png')
        assertIsFile(path)

    @parameterized.expand([
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [1, 2, 3, 4, 5, 6, 7]],
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [1, 2, 3, 4]],
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [1, 2]],
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], []],
        [[], [1, 2, 3, 4]],
        [[(0, 0), (1, 1), (2, 2)], [1, 2]],
        [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], []],
    ])
    def test_AssertionErrorWhenWrongRouteSize(self, coordinates, route):
        with self.assertRaises(AssertionError):
            self.comparison.plot_route(coordinates, route, self.filename)


class PlotRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.comparison = Comparison()
        self.filename = "route"

    def tearDown(self):
        if pl.Path(f"{self.filename}.png").resolve().is_file():
            os.remove(f"{self.filename}.png")

    def test_compareModelDistances(self):
        coordinates = [[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]]
        route1 = [[0, 1, 2, 3, 4]]
        route2 = [[2, 1, 2, 3, 4]]
        try:
            result = self.comparison.compare_model_distances(coordinates, route1, route2)

            self.assertIsNotNone(result)
        except:
            self.fail("compareModelDistances raised exception unexpectedly!")

    @parameterized.expand([
        [[[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]],
         [[1, 2, 3, 4, 5, 6, 7]], [[1, 2, 3, 4, 5, 6, 7]]],
        [[[(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)], [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]],
         [[1, 2, 3, 4, 5, 6, 7]], []],
        [[],
         [[1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 5, 6, 7]], [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]],
        [3242342,
         [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]], [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]]],

    ])
    def test_compareModelDistancesThrowsAssertionErrorOnIncorrectArgumentsSize(self, coords, route1, route2):

        with self.assertRaises(AssertionError):
            result = self.comparison.compare_model_distances(coords, route1, route2)
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

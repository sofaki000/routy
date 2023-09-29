from routy.plotUtilities.plotRoute import plot_multiple_routes_for_same_coordinates, plot_route


class Comparison:
    """
    Instantiate a comparison operation. This class is the starting point for comparing your
    routing models.
    :param None
    """

    def __init__(self):
        pass

    def plot_route(self, coordinates, routes, filename="route"):
        '''
        Plot a single route based on coordinates and routes.

        :param coordinates: List of coordinates [(x, y)] for each point on the route.
        :type coordinates: list of tuples
        :param routes: List of indices representing the route.
        :type routes: list
        :param filename: Name of the output plot file (default: "route.png").
        :type filename: str
         :Examples:
        plot_route([(0, 0), (1, 1), (2, 2)], [0, 1, 2], "example_route.png")
        '''

        seq_len = len(routes)
        assert seq_len == len(coordinates)
        assert type(coordinates[0]) is tuple

        plot_route(coordinates, routes, f'{filename}.png')

    def plot_routes(self,coordinates, routes, filename="routes"):
        '''
        Plot multiple routes for the same set of coordinates.

        :param coordinates: List of coordinates [(x, y)] for each point on the routes.
        :type coordinates: list of tuples
        :param routes: List of lists, each representing a route with indices.
        :type routes: list of lists
        :param filename: Name of the output plot file (default: "routes.png").
        :type filename: str

         :Examples:
        plot_routes([(0, 0), (1, 1), (2, 2)], [[0, 1, 2], [2, 1, 0]], "example_routes.png")
        '''
        seq_len = len(routes[0])
        assert seq_len == len(coordinates)

        assert type(coordinates[0]) is tuple
        assert type(routes) is list
        plot_multiple_routes_for_same_coordinates(coordinates,
                                                  routes,
                                                  filename)



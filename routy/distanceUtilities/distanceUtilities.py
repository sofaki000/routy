import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean

def calculate_distance(coordinates, route_indices):
    """
    Calculates the total Euclidean distance for a route based on coordinates and route order.

    Parameters:
    coordinates (list of tuple): Coordinates (x, y) of the points.
    route_indices (list): Order of indices representing the route.

    Returns:
    float: Total Euclidean distance for the route.
    """
    total_distance = 0.0

    for i in range(len(route_indices) - 1):
        start_index = route_indices[i]
        end_index = route_indices[i + 1]
        total_distance += euclidean(coordinates[start_index], coordinates[end_index])

    # Add distance between the last and first points to complete the route
    total_distance += euclidean(coordinates[route_indices[-1]], coordinates[route_indices[0]])

    return total_distance
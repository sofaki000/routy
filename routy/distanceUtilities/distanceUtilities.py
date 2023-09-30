import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean


from enum import Enum

class DistanceType(Enum):
    EUCLIDEAN = 'euclidean'
    MANHATTAN = 'manhattan'
    CHEBYSHEV = 'chebyshev'

def calculate_distance(coordinates, route_indices, distance_type=DistanceType.EUCLIDEAN):
    """
    Calculates the total Euclidean distance for a route based on coordinates and route order.

    Parameters:
    coordinates (list of tuple): Coordinates (x, y) of the points.
    route_indices (list): Order of indices representing the route.
    distance_type (str, optional): The type of distance to calculate.
        Options include:
        - 'euclidean' (default): Euclidean distance.
        - 'manhattan': Manhattan distance.
        - 'chebyshev': Chebyshev distance.

    Distance Equations:
        - Euclidean distance: sqrt((x2 - x1)^2 + (y2 - y1)^2)
        - Manhattan distance: |x2 - x1| + |y2 - y1|
        - Chebyshev distance: max(|x2 - x1|, |y2 - y1|)
    Returns:
    float: Total Euclidean distance for the route.
    """
    total_distance = 0.0

    for i in range(len(route_indices) - 1):
        start_index = route_indices[i]
        end_index = route_indices[i + 1]

        if distance_type == DistanceType.EUCLIDEAN:
            total_distance += euclidean(coordinates[start_index], coordinates[end_index])
        elif distance_type == DistanceType.MANHATTAN:
            # Manhattan distance
            total_distance += abs(coordinates[end_index][0] - coordinates[start_index][0]) + \
                              abs(coordinates[end_index][1] - coordinates[start_index][1])
        elif distance_type == DistanceType.CHEBYSHEV:
            # Chebyshev distance
            total_distance = max(total_distance,
                             max(abs(coordinates[end_index][0] - coordinates[start_index][0]),
                                 abs(coordinates[end_index][1] - coordinates[start_index][1])))

        else:
            raise NotImplementedError("Invalid distance type")


    # Add distance between the last and first points to complete the route
    total_distance += euclidean(coordinates[route_indices[-1]], coordinates[route_indices[0]])

    return total_distance
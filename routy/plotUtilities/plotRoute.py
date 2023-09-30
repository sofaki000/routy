
import matplotlib

from routy.distanceUtilities.distanceUtilities import calculate_distance

matplotlib.use('Agg')
def plot_route(coordinates, route_indices, filename):
    """
    Plots a route given coordinates and the order of the route.

    Parameters:
    coordinates (list of tuple): Coordinates (x, y) of the points.
    route_indices (list): Order of indices representing the route.

    Returns:
    None
    """
    # Extract x and y coordinates
    x = [coord[0] for coord in coordinates]
    y = [coord[1] for coord in coordinates]

    # Plot the points
    plt.scatter(x, y, color='blue')

    # Plot the route
    for i in range(len(route_indices) - 1):
        start_index = route_indices[i]
        end_index = route_indices[i + 1]
        plt.plot([x[start_index], x[end_index]], [y[start_index], y[end_index]], 'ro-')

    # Connect the last point to the first point to complete the route
    plt.plot([x[route_indices[-1]], x[route_indices[0]]], [y[route_indices[-1]], y[route_indices[0]]], 'ro-')

    # Annotate the points with their indices
    for i, txt in enumerate(route_indices):
        plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    route_distance = calculate_distance(coordinates, route_indices)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Distance travelled: {route_distance:.2f}')
    plt.legend()
    plt.grid()
    plt.savefig(filename)

# Example usage
# coordinates = [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]
# route_indices = [0, 1, 2, 3, 4]  # Replace with your route order
#
# plot_route(coordinates, route_indices)


import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def plot_multiple_routes_for_same_coordinates(coordinates, all_route_indices, base_filename):
    """
    Plots multiple routes given coordinates and their respective order.

    Parameters:
    coordinates (list of tuple): Coordinates (x, y) of the points for all routes.
    all_route_indices (list of list): Order of indices representing the routes.
    base_filename (str): Base filename to save the plot.

    Returns:
    None
    """
    num_routes = len(all_route_indices)

    # Create a new figure with subplots
    fig, axs = plt.subplots(1, num_routes, figsize=(5 * num_routes, 4))

    # Extract x and y coordinates
    x = [coord[0] for coord in coordinates]
    y = [coord[1] for coord in coordinates]

    for i in range(num_routes):
        route_indices = all_route_indices[i]
        ax = axs[i]

        # Plot the points
        ax.scatter(x, y, color='blue', label='Points')

        # Plot the route
        for i in range(len(route_indices) - 1):
            start_index = route_indices[i]
            end_index = route_indices[i + 1]
            ax.plot([x[start_index], x[end_index]], [y[start_index], y[end_index]], 'ro-')

        # Connect the last point to the first point to complete the route
        ax.plot([x[route_indices[-1]], x[route_indices[0]]], [y[route_indices[-1]], y[route_indices[0]]], 'ro-')

        # Annotate the points with their indices
        for i, txt in enumerate(route_indices):
            ax.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')


        route_distance = calculate_distance(coordinates, route_indices)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(f'Distance travelled: {route_distance:.2f}')
        ax.legend()
        ax.grid()

    plt.suptitle('Route Plots')
    plt.tight_layout()
    plt.savefig(f'{base_filename}.png')



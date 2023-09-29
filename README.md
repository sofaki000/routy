# Routy

### Comparing routing algorithms made easy

Ever worked on your reinforcement learning routing algorithm and wondered how on earth it is performing? How do you convince someone you are actually providing a better solution than their existing heuristics?

Routy is the library to help you do exactly that.
 
 

# Usage

## Installation

Install your library.

```sh
pip install routy
```
## Examples

Import the library
```python
from routy import Comparison
```

Initialize your comparison object.
```python
comparison = Comparison()
```


- **plot_route**

After you have gotten the suggested route by your model, pass the coordinates,
the suggested route, and optionally the file name in the plot_route method. This method saves an image
at the filename.png file displaying the route your model suggested.

```python
coordinates = [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]
route = [0, 1, 2, 3, 4]
filename = "myroute"
comparison.plot_route(coordinates, route, filename)
```

- **plot_routes**

Let's say you have more than one model and you want to compare the route each model
suggests for the same coordinates. You can do that using the 'plot_routes' function.

```python
coordinates = [(0, 0), (1, 1), (2, 2), (3, 0), (1, -1)]
route1 = [0, 1, 2, 3, 4]
route2 = [1, 2, 0, 4, 3]

# Pass multiple routes as a list
all_routes = [route1, route2]
comparison.plot_routes(coordinates, all_routes, filename)
```

## All available methods

You can find all the available methods documented [here](https://sofaki000.github.io/routy/).


# Development

Want to create a pull request? This section is for you.


### Documentation is important

Create documentation by running this command at project folder.

```sh
pdoc --html --force . ./comparison.py 
```
 
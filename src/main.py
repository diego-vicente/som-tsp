import numpy as np

from io_helper import read_tsp, normalize
from neuron import generate_network
from plot import plot_tsp

def main():
    problem = read_tsp('assets/uy734.tsp')

    route = som(problem, 10000)

    return

def som(problem, iterations, learning_rate=0.7):
    """Solve the TSP using a Self-Organizing Map."""

    # Obtain the normalized set of cities (w/ coord in [0,1])
    cities = problem.copy()
    cities[['x', 'y']] = normalize(cities[['x', 'y']])

    # TODO! add n as parameter
    n = cities.shape[0] * 8

    # Generate an adequate population of neurons:
    population = generate_network(n)

    plot_tsp(cities, population, 'diagrams/before.png')

    for i in range(iterations):
        city = cities.sample(1)[['x', 'y']].values
        winner_idx = select_winner(population, city)
        # print(population[winner_idx])
        neighbourhood = get_neighbourhood(winner_idx, n//10, population.shape[0])
        # print(neighbourhood)
        population += neighbourhood[:,np.newaxis] * learning_rate * (city - population)
        # print(population[winner_idx])
        learning_rate = learning_rate * 0.9999
        n = n * 0.999
        if not i % 500:
            plot_tsp(cities, population, 'diagrams/{}.png'.format(i))
        if n < 1:
            print('Radius has completely decayed, finishing execution at {} iterations'.format(i))
            break

    plot_tsp(cities, population, 'diagrams/after.png')

def select_winner(population, city):
    """Return the index of the closest neuron to a given city."""
    return euclidean_distance(population, city).argmin()

def euclidean_distance(a, b):
    """Return the array of distances of two numpy arrays of points."""
    return np.linalg.norm(a - b, axis=1)

def network_distance(center, radius, domain):
    """Return the array of circular distances of a network."""


def get_neighbourhood(center, radix, domain):
    """Get the range neighbourhood of given radix around a center index."""

    # Impose an upper bound on the radix to prevent NaN and blocks
    if radix < 1:
        radix = 1

    # Compute the circular network distance to the center
    deltas = np.absolute(center - np.arange(domain))
    distances = np.minimum(deltas, domain - deltas)

    # Compute Gaussian distribution around the given center
    return np.exp(-(distances*distances) / (2*(radix*radix)))

if __name__ == '__main__':
    main()

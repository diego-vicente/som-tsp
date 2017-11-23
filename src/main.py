import numpy as np

from io_helper import read_tsp, normalize
from neuron import generate_network

def main():
    problem = read_tsp('assets/qa194.tsp')

    route = som(problem[:10], 100)

    return

def som(problem, iterations, learning_rate=0.2):
    """Solve the TSP using a Self-Organizing Map."""

    # Obtain the normalized set of cities (w/ coord in [0,1])
    cities = problem.copy()
    cities[['x', 'y']] = normalize(cities[['x', 'y']])

    # Generate an adequate population of neurons: TODO! add n as parameter
    population = generate_network(cities.shape[0] * 6)

    print(population)

    for i in range(iterations):
        city = cities.sample(1)[['x', 'y']].values
        winner_idx = select_winner(population, city)
        # print(population[winner_idx])
        neighbourhood = get_neighbourhood(winner_idx, 3, population.shape[0])
        # print(neighbourhood)
        population[neighbourhood] += learning_rate * (city - population[neighbourhood])
        # print(population[winner_idx])

    print(population)

def select_winner(population, city):
    """Return the index of the closest neuron to a given city."""
    return euclidean_distance(population, city).argmin()

def euclidean_distance(a, b):
    """Return the array of distances of two numpy arrays of points."""
    return np.linalg.norm(a - b, axis=1)

def get_neighbourhood(center, radix, domain):
    """Get the range neighbourhood of given radix around a center index."""
    neighbourhood = np.arange(center - radix, center + radix + 1)
    return np.mod(neighbourhood, domain)


if __name__ == '__main__':
    main()

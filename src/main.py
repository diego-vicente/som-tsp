import numpy as np

from io_helper import read_tsp, normalize
from neuron import generate_network

def main():
    problem = read_tsp('assets/qa194.tsp')

    route = som(problem[:10], 10)

    return

def som(problem, iterations):
    """Solve the TSP using a Self-Organizing Map."""

    # Obtain the normalized set of cities (w/ coord in [0,1])
    cities = problem.copy()
    cities[['x', 'y']] = normalize(cities[['x', 'y']])

    # Generate an adequate population of neurons: TODO! add n as parameter
    population = generate_network(cities.shape[0] * 6)

    for i in range(iterations):
        city = cities.sample(1)
        winner_idx = select_winner(population, city)
        print(i, city)
        print(population[winner_idx], '\n')

def select_winner(population, city):
    """Return the index of the closest neuron to a given city"""
    return euclidean_distance(population, city[['x', 'y']].values).argmin()

def euclidean_distance(a, b):
    """Return the array of distances of two numpy arrays of points"""
    return np.linalg.norm(a - b, axis=1)

if __name__ == '__main__':
    main()

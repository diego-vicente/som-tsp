import numpy as np

from io_helper import read_tsp, normalize
from neuron import generate_network, get_neighborhood, select_winner
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
        # Choose a random city
        city = cities.sample(1)[['x', 'y']].values
        winner_idx = select_winner(population, city)
        # Generate a filter that applies changes to the winner's neighbourhood
        neighbourhood = get_neighbourhood(winner_idx, n//10, population.shape[0])
        # Update the network's weights (closer to the city)
        population += neighbourhood[:,np.newaxis] * learning_rate * (city - population)
        # Decay the variables
        learning_rate = learning_rate * 0.9999
        n = n * 0.999
        if not i % 500:
            plot_tsp(cities, population, 'diagrams/{}.png'.format(i))
        if n < 1:
            print('Radius has completely decayed, finishing execution at {} iterations'.format(i))
            break

    plot_tsp(cities, population, 'diagrams/after.png')


if __name__ == '__main__':
    main()

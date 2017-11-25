import numpy as np

from io_helper import read_tsp, normalize
from neuron import generate_network, get_neighborhood
from distance import select_winner, euclidean_distance, route_distance
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

    # Generate an adequate network of neurons:
    network = generate_network(n)
    print('Network of {} neurons created. Starting the iterations:'.format(n))

    plot_tsp(cities, network, 'diagrams/before.png')

    for i in range(iterations):
        if not i % 100:
            print('\t> Iteration {}/{}'.format(i, iterations), end="\r")
        # Choose a random city
        city = cities.sample(1)[['x', 'y']].values
        winner_idx = select_winner(network, city)
        # Generate a filter that applies changes to the winner's gaussian
        gaussian = get_neighborhood(winner_idx, n//10, network.shape[0])
        # Update the network's weights (closer to the city)
        network += gaussian[:,np.newaxis] * learning_rate * (city - network)
        # Decay the variables
        learning_rate = learning_rate * 0.9999
        n = n * 0.999
        if not i % 500:
            plot_tsp(cities, network, 'diagrams/{}.png'.format(i))
        if n < 1:
            print('Radius has completely decayed, finishing execution at {} iterations'.format(i))
            break

    plot_tsp(cities, network, 'diagrams/after.png')

if __name__ == '__main__':
    main()

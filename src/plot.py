import matplotlib.pyplot as plt
import numpy as np

def plot_tsp(cities, neurons, name):
    """Plot a graphical representation of the problem"""
    plt.scatter(cities['x'], cities['y'], color='red', s=10)
    plt.plot(neurons[:,0], neurons[:,1], 'r.', ls='-', color='green')
    plt.savefig(name)
    plt.clf()

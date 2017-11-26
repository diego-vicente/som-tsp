import matplotlib.pyplot as plt
import numpy as np

def plot_network(cities, neurons, name):
    """Plot a graphical representation of the problem"""
    fig = plt.figure(figsize=(5, 5), frameon = False)
    axis = fig.add_axes([0,0,1,1])

    axis.set_aspect('equal', adjustable='datalim')
    plt.axis('off')

    axis.scatter(cities['x'], cities['y'], color='red', s=4)
    axis.plot(neurons[:,0], neurons[:,1], 'r.', ls='-', color='#0063ba', markersize=2)

    plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
    plt.close()

def plot_route(cities, route, name):
    """Plot a graphical representation of the route obtained"""
    fig = plt.figure(figsize=(5, 5), frameon = False)
    axis = fig.add_axes([0,0,1,1])

    axis.set_aspect('equal', adjustable='datalim')
    plt.axis('off')

    axis.scatter(cities['x'], cities['y'], color='red', s=4)
    route = cities.reindex(route)
    route.loc[route.shape[0]] = route.iloc[0]
    axis.plot(route['x'], route['y'], color='purple', linewidth=1)

    plt.savefig(name, bbox_inches='tight', pad_inches=0, dpi=200)
    plt.close()

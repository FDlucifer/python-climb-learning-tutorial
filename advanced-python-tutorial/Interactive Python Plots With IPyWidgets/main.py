import ipywidgets
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 5, size=100)
noise = np.random.normal(size=100)

def plot_fct(w=1):
    y = 2 * x + w * noise
    plt.scatter(x,y)

ipywidgets.interact(plot_fct, w=(0,5,0.5))

from sklearn.datasets import make_moons

def plot_moons(samples=200, noise=0):
    moons = make_moons(n_samples=samples, noise=noise, random_state=50)
    x, y = moons[0], moons[1]
    plt.scatter(x[:, 0], x[:, 1], c=y)

ipywidgets.interact(plot_moons, samples=[200, 500, 1000], noise=(0,2,0.025))

def plot_sin(start=0, end=30, factor=1, grid=False, plot_cos=False):
    x = np.linspace(start, end, (end-start) * 10)
    y = np.sin(x) * factor
    plt.grid(grid)
    plt.plot(x,y)
    if plot_cos:
        y = np.cos(x)
        plt.plot(x,y)

ipywidgets.interact(plot_sin, start=(0,10,1), end=(20,50,1), factor=(0,5,0.1), grid=False)

import math

def plot_sigmoid(x_in=0):
    x = np.linspace(-5,5,1000)
    y = 1/(1+np.exp(-x))
    y_in = 1/(1+math.exp(-x_in))

    plt.plot(x, y)
    plt.scatter(x_in, y_in, c="r")
    plt.plot([x_in, x_in], [0, y_in], c="r--")
    plt.plot([-5, x_in], [y_in, y_in], c="r--")

ipywidgets.interact(plot_sigmoid, x_in=(-5,5,0.1))

def plot_hist(mu=0, sigma=1, n=100, bins=10, color="blue"):
    plt.xlim(-20, 20)
    x = np.random.normal(mu, sigma, n)
    plt.hist(x, bins=bins, color=color)

ipywidgets.interact(plot_hist, mu=(-10,10,0.5), sigma=(0,10,0.1), n=(10, 1000, 1), bins=(1, 100, 1), color=["red", "green", "blue"])

ipywidgets.interact_manual(plot_hist, mu=(-10,10,0.5), sigma=(0,10,0.1), n=(10, 1000, 1), bins=(1, 100, 1), color=["red", "green", "blue"])
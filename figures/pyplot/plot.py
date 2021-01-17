#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

MAX_X = 25

font = {'family': 'normal',
        'size': 36}

matplotlib.rc('font', **font)


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


def create_transition_plot():
    _, ax = plt.subplots(figsize=(20, 5))
    x = np.arange(1, MAX_X, 1)
    ax.plot(x, [x*x for x in np.arange(1, MAX_X, 1)])
    ax.plot(x, [0] + [2 * x * (x - 1) for x in np.arange(2, MAX_X, 1)])
    ax.plot(x[:20], [2 ** x for x in np.arange(0, 20, 1)])
    ax.plot(np.arange(1, ))
    ax.legend(['$x^{2}$', 'Naiver Ansatz: $x(x-1)$', '$2^{x}$'])
    ax.set(xlabel='Seitenzustände', ylabel='Übergänge')
    plt.ylim((0, 2000))
    plt.show()


if __name__ == "__main__":
    create_transition_plot()

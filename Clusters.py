import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def move_centroid(counters, n_centroids, centroids, len_of_centroid, dim_of_centroid):

    for i in range(len_of_centroid):
        for k in range(dim_of_centroid):
            centroids[i + 1][k] = counters[i + 1][k] / n_centroids[i]

    return centroids


def assigh_centroid(centroids, cases, dim_of_centroid, len_of_centroid):

    counters = {x + 1: [0] * dim_of_centroid for x in range(len_of_centroid)}
    n_centroids = [0] * len_of_centroid

    li = [0] * dim_of_centroid
    for li in cases:
        Distance = []
        for x in centroids:

            Distance.append(math.dist(centroids[x], li))

        minn = Distance.index(min(Distance))

        n_centroids[minn] = n_centroids[minn] + 1

        for x in range(dim_of_centroid):
            counters[minn + 1][x] = counters[minn + 1][x] + li[x]

    Centroid = move_centroid(counters, n_centroids,
                             centroids, len_of_centroid, dim_of_centroid)

    return Centroid


def Run(centroids, cases):

    dim_of_centroid = len(centroids[1])
    len_of_centroid = len(centroids)

    try:
        for k in range(10):
            CENTROIDS = assigh_centroid(
                centroids, cases, dim_of_centroid, len_of_centroid)
    except ZeroDivisionError:
        print("Given centroids are suitable :(")
    except TypeError:
        print("Didn't Entered the valid centroids")

    return CENTROIDS

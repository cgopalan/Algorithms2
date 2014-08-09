import sys
import numpy as np


def run_floyd_warshall(f):
    n_vertices, n_edges = [int(x) for x in f.readline().rstrip().split()]
    vertices = set()
    edges = {}
    print("Reading in data...")
    for line in f:
        v1, v2, edge = [int(x) for x in line.rstrip().split()]
        vertices.add(v1)
        vertices.add(v2)
        edges[(v1,v2)] = edge
    # Set up 3d array
    arr = np.zeros((n_vertices + 1, n_vertices + 1, n_vertices + 1))
    infinity = float("inf")
    # Initialize array
    print("Initializing array...")
    for i in xrange(n_vertices + 1):
        for j in xrange(n_vertices + 1):
            if i == j:
                arr[i,j,0] = 0
            if (i,j) in edges:
                arr[i,j,0] = edges[(i,j)]
            else:
                arr[i,j,0] = infinity
    # Run algo
    print("Running algorithm...")
    v_list = range(1, n_vertices+1)
    for k in v_list:
        print("Running for k value of", k)
        for i in v_list:
            for j in v_list:
                arr[i,j,k] = min(arr[i,j,k-1],
                                 arr[i,k,k-1] + arr[k,j,k-1])
    # Check for negative cycles
    print("Checking for negative cycles...")
    for i in xrange(1, n_vertices + 1):
        print(arr[i,i,n_vertices])
        if arr[i,i,n_vertices] < 0:
            sys.exit("Whoa! Negative cycle...exiting")

    # If no cycles, return APSP
    print("Calculating shortest paths...")
    shortest_paths = []
    for i in v_list:
        for j in v_list:
            shortest_paths.append(arr[i,j,n_vertices])
    print(min(shortest_paths))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        run_floyd_warshall(f)
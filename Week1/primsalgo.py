import sys
from collections import defaultdict
import pprint

def run_prims_algo(f):
    """ The Prims algorithm. """
    vertices = set()
    prim_ds = []
    # Ignore first line
    f.readline()
    for line in f:
        v1, v2, cost = [int(x) for x in line.rstrip().split()]
        prim_ds.append((v1,v2, cost))
        vertices.add(v1)
        vertices.add(v2)
    print(prim_ds)
    print(vertices)
    v_visited = {1}
    cost_sum = 0
    while v_visited != vertices:
        cost_list = []
        for x in v_visited:
            for a,b,c in prim_ds:
                if a in v_visited and b not in v_visited:
                    cost_list.append((c,b))
                if a not in v_visited and b in v_visited:
                    cost_list.append((c,a))
        min_cost = min(cost_list)
        cost_sum += min_cost[0]
        v_visited.add(min_cost[1])
        print(len(v_visited))
    print("Cost sum is {0}".format(cost_sum))

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        # Run algo by weight length difference. This is not optimal.
        run_prims_algo(f)

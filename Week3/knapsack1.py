import sys
import numpy as np

# May not need it to be this high. Just to be safe.
sys.setrecursionlimit(100000)


def run_knapsack_algo(f):
    W, n = [int(x) for x in f.readline().rstrip().split()]
    value_list, weight_list =[], []
    for line in f:
        value, weight = [int(x) for x in line.rstrip().split()]
        value_list.append(value)
        weight_list.append(weight)
    print(W, n, len(value_list), len(weight_list))
    arr = np.zeros((n+1, W+1))
    for i in range(1, n+1):
        for x in range(W+1):
            if x < weight_list[i-1]:
                arr[i,x] = arr[i-1, x]
            else:
                arr[i,x] = max(arr[i-1, x], arr[i-1, x-weight_list[i-1]] + value_list[i-1])
    return arr[n, W]


def run_fast_knapsack_algo(f):
    W, n = [int(x) for x in f.readline().rstrip().split()]
    value_list, weight_list =[], []
    for line in f:
        value, weight = [int(x) for x in line.rstrip().split()]
        value_list.append(value)
        weight_list.append(weight)
    print(W, n, len(value_list), len(weight_list))
    item_dict = {}
    def knapsack(i, x):
        if i == 0 or x == 0:
            return 0
        if (i,x) in item_dict:
            return item_dict[(i,x)]
        if x < weight_list[i-1]:
            val = knapsack(i-1, x)
        else:
            val = max(knapsack(i-1, x), knapsack(i-1, x-weight_list[i-1]) + value_list[i-1])
        item_dict[(i,x)] = val
        return val
    return knapsack(n,W)




if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        print(run_fast_knapsack_algo(f))

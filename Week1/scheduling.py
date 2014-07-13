""" Greedy Scheduling algorithms. """

import sys


def run_scheduling_algo(f, func):
    """ The core of the scheduler. """
    weight_list = []
    # Ignore first line
    f.readline()
    for line in f:
        weight, job_time = [int(x) for x in line.rstrip().split()]
        weight_list.append((func(weight, job_time), weight, job_time))
    # Sort the list by weight - length in decreasing order
    weight_list.sort(reverse=True)
    # Compute weighted completion times
    completion_time = weighted_sum = 0
    for x,y,z in weight_list:
        completion_time += z
        weighted_sum += y*completion_time
    print("Weighted sum is {0}".format(weighted_sum))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        # Run algo by weight length difference. This is not optimal.
        run_scheduling_algo(f, lambda x,y: x - y)
        # Run algo by weight length ratio. This is optimal.
        # Reset file pointer to start.
        f.seek(0)
        run_scheduling_algo(f, lambda x,y: float(x)/y)

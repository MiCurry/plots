import argparse
import sys

import numpy as np
#import scipy
import matplotlib
matplotlib.use('Agg') # Disables the need for the monitor
import matplotlib.pyplot as pyplot



def plot(size=15, layers=5):
    fig = pyplot.figure()
    ax = fig.add_subplot(111)

    vector_v = np.random.uniform(-1, 1, [layers, size, size])
    vector_u = np.random.uniform(-1, 1, [layers, size, size])

    for i in range(5):
        ax.quiver(vector_v[i], vector_u[i])


    fig.savefig("plot.png",
                dpi = 500,
                bbox_inches='tight',
                pad_inches=0,
                transparent=True
                )

    return 1 # Success


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Easy NAMS Plotting.')
    parser.add_argument('task',
                        help='task name',
                        type=str)
    parser.add_argument("-f", '--file',
                        help='File name to store the plot',
                        type=str)
    parser.add_argument("-t", '--time',
                        help='datetime object',
                        type=str)
    parser.add_argument("-d", '--date',
                        help='datetime object',
                        type=str)
    parser.add_argument("-l", '--layer',
                        help='integer',
                        type=int)
    parser.add_argument("-u", '--height',
                        help='height above ground in meters',
                        type=int)
    parser.add_argument("-i", '--slice',
                        help='integer',
                        type=int)

    args = parser.parse_args()
    if args.task == "download":
        download(north, south, east, west, "0")
    if args.task == "plot":
        print "Plotting!"
        plot(size=25)
    elif args.task == "test":
        test()
        sys.exit(0)
        #sys.exit(test())

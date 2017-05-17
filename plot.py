import argparse
import sys
import os
import string

import numpy as np
#import scipy
import matplotlib
matplotlib.use('Agg') # Disables the need for the monitor
import matplotlib.pyplot as pyplot

verbose = 0

def genData(size, layers, min=-1, max=1):
    x = np.arange(0, size, 1)
    y = np.arange(0, size, 1)

    vector_v = np.random.uniform(min, max, [layers, size, size])
    vector_u = np.random.uniform(min, max, [layers, size, size])

    return vector_v, vector_u

def contour(size=11, layers=1, density=1, minlength=2):
    fig = pyplot.figure()
    ax = fig.add_subplot(111)

    colors = ['b','g','r','c','m']
    x = np.arange(0, size, 1)
    y = np.arange(0, size, 1)

    vector_v = np.random.uniform(-1, 1, [layers, size, size])
    vector_u = np.random.uniform(-1, 1, [layers, size, size])

    for i in range(layers):
        ax.streamplot(x, y, vector_v[i], vector_u[i],
                      color=colors[i],
                      density=density,
                      minlength=minlength,
                      )
        #ax.streamplot(vector_v[i], vector_u[i], x, y, color=colors[i])

    ax.axis([0, size-1, 0, size-1])
    fig.savefig("stream-"+str(density)+"-"+str(minlength)+".png",
                dpi = 500,
                bbox_inches='tight',
                pad_inches=0,
                transparent=True
                )

    return 1 # Success

def stream(size=11, layers=2, density=2, minLength=2, fileTag="0"):
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.axis([0, size-1, 0, size-1]) # Axis

    colors = ['b','g','r','c','m']

    # Generate Data
    x = np.arange(0, size, 1)
    y = np.arange(0, size, 1)

    vector_v = np.random.uniform(-1, 1, [layers, size, size])
    vector_u = np.random.uniform(-1, 1, [layers, size, size])
    # End Generate Data


    # Plot Over Each Layer
    print "Producing a graph with: size:{0}x{1}, layers:{2}, density:{3}, minLength:{4}".format(size, size, layers, density, minLength)

    print "Plotting Layer:",
    for i in range(layers):
        print "{0},".format(i),
        ax.streamplot(x, y, vector_v[i], vector_u[i],
                      color=colors[i],
                      density=density,
                      minlength=minLength,
                      )


    fileName = "stream" + str(size) + "x" + str(size) + "-" + str(layers) + "-" + str(density) + "-" + str(minLength) + "-" + fileTag
    fig.savefig(fileName,
                dpi = 500,
                bbox_inches='tight',
                pad_inches=0,
                transparent=True
                )
    # Output
    return 1 # Success

def quiver(size=50, layers=5):
    fig = pyplot.figure()
    ax = fig.add_subplot(111)

    colors = ['b','g','r','c','m']

    vector_v = np.random.uniform(-1, 1, [layers, size, size])
    vector_u = np.random.uniform(-1, 1, [layers, size, size])

    for i in range(5):
        ax.quiver(vector_v[i], vector_u[i], color=colors[i])


    fig.savefig("vector.png",
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
    parser.add_argument("-f", '--fileNameTag',
                        help='Appends it to the end of a filename so it can be unique when you plot it',
                        type=str,
                        default="0")
    parser.add_argument("-d", '--depths',
                        help='integer - amount of depths/layers',
                        type=int,
                        default=3)
    parser.add_argument("-s", '--size',
                        help='int - size of the domain (s,s)',
                        type=int,
                        default=15)
    parser.add_argument("-p", '--density',
                        help='int - density of the plot (higher values mean more lines)',
                        type=int,
                        default=1)
    parser.add_argument("-l", '--length',
                        help='int - length or min length',
                        type=int,
                        default=1)
    args = parser.parse_args()

    if args.task == "quiver":
        quiver(size      = args.size,
               layers    = args.depths,
               fileTag   = args.fileNameTag)
    if args.task == "stream":
        stream(size = args.size,
               layers = args.depths,
               density = args.density,
               minLength = args.length,
               fileTag = args.fileNameTag)

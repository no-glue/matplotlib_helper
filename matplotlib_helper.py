#/usr/bin/env python

import csv
import numpy
import matplotlib.pyplot as plt

class MatplotlibHelper(object):
    def plot_multiple_xy(self, files, out, skipColumns, terminal, xlabel, ylabel):
        fig = plt.figure()
        subplot = fig.add_subplot(1, 1, 1, xlabel = xlabel, ylabel = ylabel)
        for i, f in enumerate(files):
            reader = csv.reader(open(f, "rb"), delimiter='\t')
            values = list(reader)
            print values
            array = numpy.array(values).astype("string")
            skipped = array[:, int(skipColumns):]
            print skipped
            floats = skipped.astype("float")
            subplot.plot(floats[:,1], floats[:,0], "o-", label = f)
            for xy in zip(floats[:, 1], floats[:, 0]):
              subplot.annotate("(%s, %s)" % xy, xy = xy, textcoords="offset points")
        fig.savefig(out)

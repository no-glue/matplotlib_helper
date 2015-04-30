#!/usr/bin/env python

import argparse
import sys
import matplotlib_helper

if __name__ == "__main__":
  argv = sys.argv[1:]
  parser = argparse.ArgumentParser()
  parser.add_argument("-files", nargs='+')
  parser.add_argument("-out")
  parser.add_argument("-skipColumns")
  parser.add_argument("-terminal")
  parser.add_argument("-xlabel")
  parser.add_argument("-ylabel")
  args = parser.parse_args(argv)

  plot = matplotlib_helper.MatplotlibHelper()
  plot.plot_multiple_xy(args.files, args.out, args.skipColumns, args.terminal, args.xlabel, args.ylabel)

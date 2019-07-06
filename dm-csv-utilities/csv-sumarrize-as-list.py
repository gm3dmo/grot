#!/usr/bin/env python

import os
import sys
import csv


def main():

  f = sys.argv[1]
  infile = csv.DictReader(open(f))

  number_of_records = 10

  for row in infile:
     for item in row:
        if sys.stdout.isatty():
            l = (f'{item} = \033[7m\033[31m{row[item]}\033[0m')
        else:
            l = (f'{item} = {row[item]}')
        print(l)


if __name__ == "__main__":
    main()
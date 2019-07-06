#!/usr/bin/env python

import os
import sys
import csv
import logging
from csvdm import openCSVFile, summarizeCSV


def main():

  logging.basicConfig(level=logging.DEBUG)

  f = sys.argv[1]
  csv_dict = openCSVFile(f)
  summarizeCSV(csv_dict)


if __name__ == "__main__":
    main()
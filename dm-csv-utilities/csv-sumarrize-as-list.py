#!/usr/bin/env python

import os
import sys
import csv
import logging


def openCSVFile(f):
    csv_dict = csv.DictReader(open(f))
    #logging.debug(dir(csv_dict))
    logging.debug(f"""CSV Dialect: {csv_dict.dialect}""")
    logging.debug(f"""Field names: {csv_dict.fieldnames}""")
    return csv_dict


def summarizeCSV(csv_dict, num_rows_to_summarize=1, separator='='):
    """Generate a view of each column in a csv file printed line by line:

    fruit,count
    apple,2

    will be printed as:

    fruit = apple
    count = 2

    """
    num_rows_to_summarize = 2 + num_rows_to_summarize
    if sys.stdout.isatty():
        hl_on  = """\033[7m\033[31m"""
        hl_off = """\033[0m')"""
    else:
        hl_on = ""
        hl_off = ""
    for row in csv_dict:
        if csv_dict.line_num >= num_rows_to_summarize:
            break
        else:
            for item in row:
                l = (f'{item} {separator} {hl_on}{row[item]}{hl_off}')
                print(l)
            logging.debug(f"""line number of csv: {csv_dict.line_num}""")
            print()


def main():

  logging.basicConfig(level=logging.DEBUG)

  f = sys.argv[1]
  csv_dict = openCSVFile(f)
  summarizeCSV(csv_dict)


if __name__ == "__main__":
    main()
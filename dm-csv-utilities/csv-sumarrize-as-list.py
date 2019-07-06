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


def main():

  logging.basicConfig(level=logging.DEBUG)
  f = sys.argv[1]
  csv_dict = openCSVFile(f)

  num_rows_to_summarize = 10

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
            l = (f'{item} = {hl_on}{row[item]}{hl_off}')
            print(l)
        logging.debug(f"""line number of csv: {csv_dict.line_num}""")
        print()


if __name__ == "__main__":
    main()
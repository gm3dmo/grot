#!/usr/bin/env python

import os
import sys
import csv

def openCSVFile(f):
    csv_dict = csv.DictReader(open(f))
    print(dir(csv_dict))
    print(csv_dict.fieldnames)
    print(csv_dict.dialect)
    print(csv_dict.line_num)
    print(csv_dict.reader)
    print(csv_dict.restkey)
    print(csv_dict.restval)
    return csv_dict


def main():

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
        print()


if __name__ == "__main__":
    main()
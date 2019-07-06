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


def summarizeCSV(csv_dict, num_rows_to_summarize=1, separator=' = ', scramble=True):
    """Generate a view of each column in a csv file printed line by line:

fruit,count
apple,2

will be printed as:

fruit = apple
count = 2

*separator* changes what is printed to separate the row name from the variable.

*num_rows_to_summarize* is the number of rows from the csv you want to print out
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
            if scramble == True:
                things_to_scramble = [ 'Day' ]
                row = scrambleValues(things_to_scramble, row)
            for item in row:
                l = (f'{item}{separator}{hl_on}{row[item]}{hl_off}')
                print(l)
            logging.debug(f"""line number of csv: {csv_dict.line_num}""")
            print()


def lowercaseList(list):
     """convert the items in a list to lowercase"""
     return [x.lower() for x in list]


def scrambleValues(columns_to_scramble, row, replacement_value='*****'):
    """Takes a list of column headings that need to be scrambled and replaces the valued in them with """
    logging.debug(f"scrambling: {columns_to_scramble}")
    columns_to_scramble = lowercaseList(columns_to_scramble)
    logging.debug(columns_to_scramble)
    for column in row:
        if column.lower() in columns_to_scramble:
            row[column]  = replacement_value
            logging.debug(f"scrambling {column}")
    return row


if __name__ == "__main__":
    main()

"""
Author: Aaron W.
"""
import csv
import operator


def read_option(cfg_file, option):
    result = {}
    with open(cfg_file, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter='=', escapechar='\\', quoting=csv.QUOTE_NONE)
        for row in reader:
            if not row or row[0].startswith('#'):
                continue
            if len(row) != 2:
                continue
            result[row[0]] = row[1]
    return result.get(option)


def read_options(cfg_file):
    result = {}
    with open(cfg_file, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter='=', escapechar='\\', quoting=csv.QUOTE_NONE)
        for row in reader:
            if not row or row[0].startswith('#'):
                continue
            if len(row) != 2:
                continue
            result[row[0]] = row[1]
    return result


def set_option(ini_file, option, val):
    pre = read_options(ini_file)
    pre[option] = val
    with open(ini_file, "wb") as csvfile:
        writer = csv.writer(csvfile, delimiter='=', escapechar='\\', quoting=csv.QUOTE_NONE)
        for key, value in sorted(pre.items(), key=operator.itemgetter(0)):
            writer.writerow([key, value])


def set_options(ini_file, dic):
    pre = read_options(ini_file)
    for k in dic:
        pre[k] = dic[k]
    with open(ini_file, "wb") as csvfile:
        writer = csv.writer(csvfile, delimiter='=', escapechar='\\', quoting=csv.QUOTE_NONE)
        for key, value in sorted(pre.items(), key=operator.itemgetter(0)):
            writer.writerow([key, value])

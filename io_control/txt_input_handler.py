"""
Author: Aaron W.
"""


def read_file_and_convert_to_list(file_path, ignore_comment=True, ignore_empty=True):
    try:
        trans = []
        with open(file_path) as f:
            lines = f.read().splitlines()
            for line in lines:
                if not line and ignore_empty:
                    continue
                if line.startswith('#') and ignore_comment:
                    continue
                trans.append(line)
        return trans
    except IOError:
        print "Not able to read file!"
        return []

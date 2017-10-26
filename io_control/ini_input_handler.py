"""
Author: Aaron W.
"""
from ConfigParser import ConfigParser
from ConfigParser import ParsingError, NoSectionError, NoOptionError
import os


def read_option(ini_file, section, option):
    parser = ConfigParser()
    parser.optionxform = str
    try:
        parser.read(ini_file)
        return parser.get(section, option)
    except ParsingError:
        print "Not a good INI format!"
        return None
    except (NoOptionError, NoSectionError):
        print "Not such section/option!"
        return None


def set_option(ini_file, section, option, val):
    parser = ConfigParser()
    parser.optionxform = str
    try:
        if not os.path.isfile(ini_file):
            print("config file missing, creating one!")
            with open(ini_file, 'w') as f:
                f.write("[" + section + "]")
        print("opening config file: " + ini_file)
        parser.read(ini_file)
        if not parser.has_section(section):
            print("no such section, adding")
            parser.add_section(section)
        print("setting value of option " + option + " under section " + section + " to be: " + val)
        parser.set(section, option, val)
        with open(ini_file, 'w+') as optfile:
            parser.write(optfile)
    except ParsingError:
        print "The given ini file is not in a good INI format!"


def read_options_as_dict(ini_file, section):
    parser = ConfigParser()
    parser.optionxform = str
    try:
        ret = {}
        parser.read(ini_file)
        opts = parser.options(section)
        for opt in opts:
            ret[opt] = parser.get(section, opt)
        return ret
    except ParsingError:
        print "Not a good INI format!"
        return {}
    except NoSectionError:
        print "Not such section!"
        return {}


def set_options_from_dict(ini_file, section, dic):
    parser = ConfigParser()
    parser.optionxform = str
    try:
        if not os.path.isfile(ini_file):
            print("config file missing, creating one!")
            with open(ini_file, 'w') as f:
                f.write("[" + section + "]")
        print("opening config file: " + ini_file)
        parser.read(ini_file)
        if not parser.has_section(section):
            print("no such section, adding")
            parser.add_section(section)
        for cob in dic:
            print("setting value of option {} under section {} to be {}".format(cob, section, dic[cob]))
            parser.set(section, cob, dic[cob])
        with open(ini_file, 'w+') as optfile:
            parser.write(optfile)
    except ParsingError:
        print "The given ini file is not in a good INI format!"

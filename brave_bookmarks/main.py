import argparse
import json
import os
import pprint
from pathlib import Path

MARKS_PARSER = argparse.ArgumentParser(description='List brave bookmarks')

MARK_PARSER = argparse.ArgumentParser(description='Show information about a brave bookmark')
MARK_PARSER.add_argument("name")

def documentation():
    print("Use `bravemarks` to list bookmarks in brave and `bravemark` to show information about a bookmark")


BOOKMARKS_PATH =  Path(os.path.expanduser("~")) / ".config" / "BraveSoftware" / "Brave-Browser" / "Default" / "Bookmarks"


def load_data():
    with open(BOOKMARKS_PATH) as f:
        return json.loads(f.read())


def bookmarks():
    MARKS_PARSER.parse_args()
    data = load_data()

    for x in data["roots"].values():
        for c in x["children"]:
            if c["type"]  != "url":
                raise Exception('Unknown bookmark type {c["type"]} for bookmark {c["bookmark"]}')
            print(c["name"])

def find_mark(data, name):
    for x in data["roots"].values():
        for c in x["children"]:
            if c["type"]  != "url":
                raise Exception('Unknown bookmark type {c["type"]} for bookmark {c["bookmark"]}')
            if c["name"] == name:
                return c
    else:
        raise Exception('fCould not find bookmark {name} in bookmarks. Run bravemarks to list all bookmarks')




def bookmark():
    arg = MARK_PARSER.parse_args()
    data = load_data()
    mark = find_mark(data, arg.name)
    print(mark["url"])

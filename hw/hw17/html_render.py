#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    content = ""
    indent = 4

    def __init__(self):
        pass

    def append(self, content):
        self.content = self.content + ("    %s\n" % content)

    def render(self, file_out, ind=" "):
        savefile = open(file_out, "w")
        savefile.write("<>", self.content, "</>")
        savefile.close()



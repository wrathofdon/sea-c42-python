#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    open_tag = "<>"
    close_tag = "</>"
    contents = [open_tag, close_tag]

    def __init__(self):
        self.open_tag = "<>"
        self.close_tag = "</>"
        self.contents = [open_tag, close_tag]

    def append(self, content):
        self.content = self.content + ("    %s\n" % content)

    def render(self, file_out, ind=" "):
        file_out.write(self.content)


class Html(Element):
    def __init__(self, name="", content=""):
        self.name = name
        self.children = [content] if content else []

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out, indent="     "):
        file_out.write("%s <%s>" % (self.indent, self.name))
        for child in self.children:
            if(type(child) == str):
                file_out.write(self.indent + IND_LEVEL + child)
        else:
            child.render(file_out, self.indent + IND_LEVEL)
        file_out.write("%s</%s>" % (self.indent, self.name))

file_out.write("<DOCTYPE html>\n")
Element.render(self, file_out, "")

Body:
Element.__init__(self, name="body", content=content)

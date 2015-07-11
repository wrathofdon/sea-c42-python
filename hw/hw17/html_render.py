#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


TAB = "    "
# Designates standard tab size

class Element(object):

    def __init__(self, tag="", content="", indent=0, kwargs={}):
        # kwargs are necessary to add key value pairs to tags
        self.tag1 = tag
        self.tag2 = tag
        # separate open and close tags so I can add styles via kwargs
        for name, value in kwargs.items():
            self.tag1 = self.tag1 + ' %s="%s"' % (name, value)
            print(name, value)
            # if a style is requested, only the first tag is changed
        self.children = [content] if content else []
        self.indent = TAB * indent

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out):
        file_out.write("\n%s<%s>" % (self.indent, self.tag1))
        for child in self.children:
            if(type(child) == str):
                file_out.write("\n" + self.indent + TAB + child)
            else:
                child.render(file_out)
        file_out.write("\n%s</%s>" % (self.indent, self.tag2))


class Html(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, "html", content, 0, kwargs)

    def render(self, file_out):
        # HTML needs its own render function to add the "DOCTYPE" tag
        file_out.write("<!DOCTYPE html>")
        file_out.write("\n%s<%s>" % (self.indent, self.tag1))
        for child in self.children:
            if(type(child) == str):
                file_out.write("\n" + self.indent + TAB + child)
            else:
                child.render(file_out)
        file_out.write("\n%s</%s>" % (self.indent, self.tag2))


class Body(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, "body", content, 1, kwargs)


class P(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, "p", content, 2, kwargs)


class Head(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, "head", content, 1, kwargs)


class OneLineClass(Element):

    def render(self, file_out):
    # OneLineClass has unique render function to minimize line breaks
        file_out.write("\n%s<%s>%s</%s>" % (self.indent, self.tag1, \
            self.children[0], self.tag2))


class Title(OneLineClass):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, "title", content, 2, kwargs)


class Hr(Element):

    def __init__(self):
        Element.__init__(self, "", "", 2)
        # takes no arguments to avoid letting people muck up the hr/br tag

    def render(self, file_out):
        # unique render function
        file_out.write("\n" + self.indent + "<hr />")


class Br(Hr):

    def render(self, file_out):
        file_out.write("\n" + self.indent + "<br />")


class A(OneLineClass):

    def __init__(self, link="", content="", **kwargs):
        kwargs.update({"href": link})
        Element.__init__(self, "a", content, 2, kwargs)
        print("Link")

#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


TAB = "    "

class Element(object):

    def __init__(self, tag="", content="", indent=0, kwargs={}):
        self.tag1 = tag
        self.tag2 = tag
        for name, value in kwargs.items():
            self.tag1 = self.tag1 + ' %s="%s"' % (name, value)
            print(name, value)
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


class Title(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, "title", content, 2, kwargs)

    def render(self, file_out):
        file_out.write("\n%s<%s>%s</%s>" % (self.indent, self.tag1, \
            self.children[0], self.tag2))



"""


page = hr.Html()

head = hr.Head()
head.append(hr.Title(u"PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
              style=u"text-align: center; font-style: oblique;"))

page.append(body)

render(page, u"test_html_output4.html")
"""

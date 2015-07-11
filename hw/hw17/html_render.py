#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


IND_LVL = "    "


class Element(object):

    def __init__(self, tag="", content="", indent=0):
        self.tag = tag
        self.children = [content] if content else []
        self.indent = IND_LVL * indent
        print(self.tag)

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out):
        file_out.write("\n%s<%s>" % (self.indent, self.tag))
        for child in self.children:
            if(type(child) == str):
                file_out.write("\n" + self.indent + IND_LVL + child)
            else:
                child.render(file_out)
        file_out.write("\n%s</%s>" % (self.indent, self.tag))


class Html(Element):

    def __init__(self, tag="", content="", indent=0):
        Element.__init__(self, "html", "", 0)

    def render(self, file_out):
        file_out.write("<!DOCTYPE html>")
        file_out.write("\n%s<%s>" % (self.indent, self.tag))
        for child in self.children:
            if(type(child) == str):
                file_out.write("\n" + self.indent + IND_LVL + child)
            else:
                child.render(file_out)
        file_out.write("\n%s</%s>" % (self.indent, self.tag))


class Body(Element):

    def __init__(self, tag="", content="", indent=0):
        Element.__init__(self, "body", "", 1)


class P(Element):

    def __init__(self, content="", indent=0):
        Element.__init__(self, "p", content, 2)


class Head(Element):

    def __init__(self, content="", indent=0):
        Element.__init__(self, "head", content, 1)
        print("Head")


class Title(Element):

    def __init__(self, content="", indent=0):
        Element.__init__(self, "title", content, 2)
        print("Title")

    def render(self, file_out):
        file_out.write("\n%s<%s>%s</%s>" % (self.indent, self.tag, \
            self.children[0], self.tag))



"""
page = hr.Html()

head = hr.Head()
head.append(hr.Title(u"PythonClass = Revision 1087:"))

page.append(head)

body = hr.Body()

body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))
body.append(hr.P(u"And here is another piece of text -- you should be able to add any number"))

page.append(body)

render(page, u"test_html_output3.html")
"""

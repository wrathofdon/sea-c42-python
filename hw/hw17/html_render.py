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
        Element.__init__(self, "html", "<DOCTYPE html>", 1)


class Body(Element):

    def __init__(self, tag="", content="", indent=0):
        Element.__init__(self, "html", "", 2)


class P(Element):

    def __init__(self, tag="", content="", indent=0):
        Element.__init__(self, "p", "", 2)

"""file_out.write("<DOCTYPE html>\n")
Element.render(self, file_out, "")

# ## Step 2
# ##########

page = hr.Html()

body = hr.Body()

body.append(hr.P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))

body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

page.append(body)

render(page, "test_html_output2.html")



# # Step 6
# #########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title(u"PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
#               style=u"text-align: center; font-style: oblique;"))

# body.append(hr.Hr())

# body.append(u"And this is a ")
# body.append( hr.A(u"http://google.com", "link") )
# body.append(u"to google")

# page.append(body)

# render(page, u"test_html_output6.html")


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
Element.__init__(self, name="body", content=content)"""

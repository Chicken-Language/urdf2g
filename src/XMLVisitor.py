# -*- coding: utf-8 -*-
import antlr4

from gen.xml.XMLParser import XMLParser
from gen.xml.XMLParserVisitor import XMLParserVisitor

OPEN = 0
CLOSE = 1
EL_NAME = ['robot', 'link', 'joint', 'parent', 'child']


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []


class XMLVisitor(XMLParserVisitor):
    def __init__(self):
        super(XMLVisitor, self).__init__()
        self.graph = Graph()

    def visitElement(self, ctx: XMLParser.ElementContext):
        # the idea of soup is from BeautifulSoup4
        soup_name = ctx.Name(OPEN).getText()
        if soup_name in EL_NAME:
            # self.graph.nodes.append(soup_name)
            print(soup_name)
            for ch in ctx.attribute():
                self.visit(ch)

            if not ctx.content() is None:
                self.visit(ctx.content())

    def visitAttribute(self, ctx: XMLParser.AttributeContext):
        soup_attr = ctx.Name().getText()
        soup_string = ctx.STRING().getText()
        print(soup_attr, soup_string)

    def visitContent(self, ctx:XMLParser.ContentContext):
        for i in range(len(ctx.element())):
            self.visit(ctx.element(i))

# -*- coding: utf-8 -*-
import antlr4

from gen.xml.XMLParser import XMLParser
from gen.xml.XMLParserVisitor import XMLParserVisitor

OPEN = 0
CLOSE = 1
EL_NAME = ['robot', 'link', 'joint']


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []


class XMLVisitor(XMLParserVisitor):
    def __init__(self):
        super(XMLVisitor, self).__init__()
        self.graph = Graph()
        self.type = ''

    def visitElement(self, ctx: XMLParser.ElementContext):
        # the idea of soup is from BeautifulSoup4
        soup_name = ctx.Name(OPEN).getText()
        name = ''
        if soup_name in EL_NAME:
            self.type = soup_name
            attr_dicts = {}
            for attr in ctx.attribute():
                attr_dict = self.visit(attr)
                name = attr_dict.get('name', name)
                attr_dicts.update(attr_dict)
            self.graph.nodes.append({soup_name: attr_dicts})

        if not ctx.content() is None:
            if self.type == 'joint':
                link_node = self.visit(ctx.content())
                link_node.update({'joint': name})
                self.graph.edges.append(link_node)
            else:
                self.visit(ctx.content())

    def visitAttribute(self, ctx: XMLParser.AttributeContext):
        soup_attr = ctx.Name().getText()
        soup_string = ctx.STRING().getText()
        return {soup_attr: soup_string}

    def visitContent(self, ctx:XMLParser.ContentContext):

        if self.type == 'joint':
            edge = {}
            for el in ctx.element():
                # print(el.Name(0).getText(), el.attribute(0).STRING().getText())
                if el.Name(0).getText() == 'parent':
                    # print(el.attribute(0).STRING().getText())
                    edge['parent'] = el.attribute(0).STRING().getText()
                elif el.Name(0).getText() == 'child':
                    edge['child'] = el.attribute(0).STRING().getText()
            return edge
        else:
            for i in range(len(ctx.element())):
                self.visit(ctx.element(i))

# -*- coding: utf-8 -*-
import sys

import antlr4
import graphviz

from src.error import XMLErrorListener
from src.XMLVisitor import XMLVisitor

from gen.xml.XMLLexer import XMLLexer
from gen.xml.XMLParser import XMLParser


def load_tree(ins, is_file=False):
    if is_file:
        try:
            input_ = antlr4.FileStream(ins)
        except Exception as e:
            print(e)
    else:
        try:
            input_ = antlr4.InputStream(ins)
        except Exception as e:
            print(e)

    lexer = XMLLexer(input_)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = XMLParser(tokens)
    parser.buildParseTrees = True

    listener = XMLErrorListener()
    parser.removeErrorListeners()  # Remove the default ConsoleErrorListener
    parser.addErrorListener(listener)  # Add back a custom error listener

    return parser.document()


def urdf2g(input, file_out=None, is_file=False, stdout=True):
    lines = ""
    tree = load_tree(input, is_file)
    visitor = XMLVisitor()
    visitor.visit(tree)

    lines += "digraph G {\n"

    for node_dict in visitor.graph.nodes:
        if 'link' in node_dict:
            lines += node_dict['link']['name'] + "[shape=box] ;\n"
        elif 'joint' in node_dict:
            lines += node_dict['joint']['name'] + "[color=blue; shape=ellipse] ;\n"

    for link_dict in visitor.graph.edges:
        lines += link_dict['parent'] + " -> " + link_dict['joint'] + ";\n"
        lines += link_dict['joint'] + " -> " + link_dict['child'] + ";\n"

    lines += "}\n"

    if stdout:
        print(lines)

    if file_out:
        with open(file_out, 'w') as fw:
            fw.writelines(lines)

    if stdout:
        dot = graphviz.Source(lines)
        dot.render('output', format='svg')



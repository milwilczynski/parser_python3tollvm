from unittest import TestCase
import io
from unittest import *
import pytest
from antlr4 import *
from antlr4.error.ErrorListener import *
from antlr4.tree.Trees import Trees
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from Python3Listener import Python3Listener

'''
class Python3ErrorListener(ErrorListener):
    def __init__(self, output):
        self.output = output
        self._symbol = ''

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offendingSymbol.text
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("rule stack: {}".format(str(stack)))
        print("line {} : {} at {} : {}".format(str(line),
                                               str(column),
                                               str(offendingSymbol).replace(" ", u'\u23B5'),
                                               msg.replace(" ", u'\u23B5')))

    @property
    def symbol(self):
        return self._symbol


class Python3ParserTests(TestCase):

    def setup():
        input = FileStream("/test_grammar.py")
        lexer = Python3Lexer(input)
        stream = CommonTokenStream(lexer)

        # print out the token parsing
        stream.fill()
        print("TOKENS")
        for token in stream.tokens:
            if token.text != '<EOF>':
                type_name = Python3Parser.symbolicNames[token.type]
                tabs = 5 - len(type_name) // 4
                sep = "\t" * tabs
                print("    %s%s%s" % (type_name, sep,
                                      token.text.replace(" ", u'\u23B5').replace("\n", u'\u2936')))
        parser = Python3Parser(stream)

        Python3ParserTests.output = io.StringIO()
        Python3ParserTests.error = io.StringIO()

        parser.removeErrorListeners()
        Python3ParserTests.errorListener = Python3ErrorListener(Python3ParserTests.error)
        parser.addErrorListener(Python3ParserTests.errorListener)
        return parser
'''


class Python3ErrorListener(ErrorListener):
    def __init__(self, output):
        self.output = output
        self._symbol = ''

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offendingSymbol.text
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("rule stack: {}".format(str(stack)))
        print("line {} : {} at {} : {}".format(str(line),
                                               str(column),
                                               str(offendingSymbol).replace(" ", u'\u23B5'),
                                               msg.replace(" ", u'\u23B5')))

    @property
    def symbol(self):
        return self._symbol


class Python3ParserTests(TestCase):

    def setup(self, path):
        input = FileStream(path)
        lexer = Python3Lexer(input)
        stream = CommonTokenStream(lexer)

        # print out the token parsing
        stream.fill()
        print("TOKENS")
        for token in stream.tokens:
            if token.text != '<EOF>':
                type_name = Python3Parser.symbolicNames[token.type]
                tabs = 5 - len(type_name) // 4
                sep = "\t" * tabs
                print("    %s%s%s" % (type_name, sep,
                                      token.text.replace(" ", u'\u23B5').replace("\n", u'\u2936')))
        parser = Python3Parser(stream)

        self.output = io.StringIO()
        self.error = io.StringIO()

        parser.removeErrorListeners()
        self.errorListener = Python3ErrorListener(self.error)
        parser.addErrorListener(self.errorListener)
        return parser

    def main(self):
       # input = FileStream("in.py") #read the first argument as a filestream
        lexer = Python3Lexer(input) #call your lexer
        stream = CommonTokenStream(lexer)
        #parser = Python3Parser(stream)
        parser = self.setup("in.py")
        listener = Python3Listener()
        tree = parser.file_input()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        self.assertEqual(len(self.errorListener.symbol), 0)
        #Python3ParserTests.assertEqual(len(Python3ParserTests.errorListener.symbol), 0)
        #print(Trees.toStringTree(tree, Python3Listener, parser))

        print(tree)



if __name__ == "__main__":
    Python3ParserTests().main()


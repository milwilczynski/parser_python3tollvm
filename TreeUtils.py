import os

from antlr4.Utils import *
from antlr4.tree.Trees import Trees


class TreeUtils:
    indents = " "
    level = 0
    eol = os.linesep

    def __init__(self):
        pass

    def toPrettyTree(self, tree, ruleNames):
        self.level = 0
        return self.process(tree, ruleNames)

    def process(self, tree, ruleNames):
        if tree.getChildCount() == 0:
            return escapeWhitespace(Trees.getNodeText(tree, ruleNames), False)
        sb = ""
        sb = sb + (self.lead(self.level))
        self.level = self.level + 1
        s = escapeWhitespace(Trees.getNodeText(tree, ruleNames), False)
        sb = sb + s + ' '
        for i in range(0, tree.getChildCount()):
            sb = sb + self.process(tree.getChild(i), ruleNames)

        self.level = self.level - 1
        sb = sb + (self.lead(self.level))

        return sb

    def lead(self, level):
        sb = ""
        if level > 0:
            sb = sb + self.eol
            for cnt in range(0, level):
                sb = sb + self.indents
        return sb

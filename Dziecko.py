from Python3Visitor import Python3Visitor
from Python3Parser import Python3Parser

class Testo(Python3Visitor):
    pass

    def visitFile_input(self, ctx: Python3Parser.File_inputContext):
        return self.visitChildren(ctx)

    def visitIf_stmt(self, ctx: Python3Parser.If_stmtContext):
        print("if visitor dziecko")
        return self.visitChildren(ctx)

    def visitStmt(self, ctx: Python3Parser.StmtContext):
        print("stmt visit dziecko")
        return self.visitChildren(ctx)

    def visitTerm(self, ctx: Python3Parser.TermContext):
        print("siema")
        return self.visitChildren(ctx)

    def visitAtom(self, ctx: Python3Parser.AtomContext):
        print("atomdziecko")
        return  self.visitChildren(ctx)
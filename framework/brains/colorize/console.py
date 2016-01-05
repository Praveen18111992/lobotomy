from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.jvm import JavaLexer
from pygments.lexers.dalvik import SmaliLexer


class ColorizeConsole(object):

    def __init__(self):
        super(ColorizeConsole, self).__init__()

    @staticmethod
    def colorize_decompiled_method(method):

        """
        Args:
            method:

        Prints highlighted decompiled method
        """
        print(highlight(method, formatter=TerminalFormatter(bg="dark"), lexer=JavaLexer()))

    @staticmethod
    def colorize_disas_method(method):

        """
        Args:
            method:

        Prints highlighted diassembled method
        """
        print(highlight(method, formatter=TerminalFormatter(bg="dark"), lexer=SmaliLexer()))


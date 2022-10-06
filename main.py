import sys
from antlr4 import *
from mainLexer import mainLexer



def main(argv):
    while True:
        text = InputStream(input(">"))
        lexer = mainLexer(text)
        for item in lexer.getAllTokens():
            print('item : ', item.text)


if __name__ == "__main__":
    main(sys.argv)

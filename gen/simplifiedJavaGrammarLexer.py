# Generated from C:/Users/jose1/Documents/UFPI/6� per�odo/Compiladores/trabFinal/javaSimplificado\simplifiedJavaGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,38,273,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,1,
        1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,22,
        1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,
        1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,3,29,195,8,29,1,30,4,30,198,8,30,11,30,12,30,
        199,1,31,4,31,203,8,31,11,31,12,31,204,1,31,1,31,4,31,209,8,31,11,
        31,12,31,210,1,32,1,32,5,32,215,8,32,10,32,12,32,218,9,32,1,32,1,
        32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,231,8,33,1,
        34,1,34,5,34,235,8,34,10,34,12,34,238,9,34,1,35,4,35,241,8,35,11,
        35,12,35,242,1,35,1,35,1,36,1,36,1,36,1,36,5,36,251,8,36,10,36,12,
        36,254,9,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,5,37,264,8,37,
        10,37,12,37,267,9,37,1,37,1,37,1,37,1,37,1,37,2,252,265,0,38,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,
        51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,
        73,37,75,38,1,0,6,1,0,48,57,1,0,46,46,1,0,34,34,2,0,65,90,97,122,
        4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,284,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,
        23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,
        33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,
        43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,
        53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,
        63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,
        73,1,0,0,0,0,75,1,0,0,0,1,77,1,0,0,0,3,79,1,0,0,0,5,81,1,0,0,0,7,
        83,1,0,0,0,9,85,1,0,0,0,11,90,1,0,0,0,13,94,1,0,0,0,15,99,1,0,0,
        0,17,103,1,0,0,0,19,105,1,0,0,0,21,111,1,0,0,0,23,113,1,0,0,0,25,
        119,1,0,0,0,27,126,1,0,0,0,29,132,1,0,0,0,31,138,1,0,0,0,33,145,
        1,0,0,0,35,148,1,0,0,0,37,153,1,0,0,0,39,156,1,0,0,0,41,159,1,0,
        0,0,43,161,1,0,0,0,45,163,1,0,0,0,47,166,1,0,0,0,49,169,1,0,0,0,
        51,171,1,0,0,0,53,173,1,0,0,0,55,175,1,0,0,0,57,177,1,0,0,0,59,194,
        1,0,0,0,61,197,1,0,0,0,63,202,1,0,0,0,65,212,1,0,0,0,67,230,1,0,
        0,0,69,232,1,0,0,0,71,240,1,0,0,0,73,246,1,0,0,0,75,259,1,0,0,0,
        77,78,5,40,0,0,78,2,1,0,0,0,79,80,5,44,0,0,80,4,1,0,0,0,81,82,5,
        41,0,0,82,6,1,0,0,0,83,84,5,58,0,0,84,8,1,0,0,0,85,86,5,118,0,0,
        86,87,5,111,0,0,87,88,5,105,0,0,88,89,5,100,0,0,89,10,1,0,0,0,90,
        91,5,101,0,0,91,92,5,110,0,0,92,93,5,100,0,0,93,12,1,0,0,0,94,95,
        5,109,0,0,95,96,5,97,0,0,96,97,5,105,0,0,97,98,5,110,0,0,98,14,1,
        0,0,0,99,100,5,118,0,0,100,101,5,97,0,0,101,102,5,114,0,0,102,16,
        1,0,0,0,103,104,5,59,0,0,104,18,1,0,0,0,105,106,5,99,0,0,106,107,
        5,111,0,0,107,108,5,110,0,0,108,109,5,115,0,0,109,110,5,116,0,0,
        110,20,1,0,0,0,111,112,5,61,0,0,112,22,1,0,0,0,113,114,5,119,0,0,
        114,115,5,104,0,0,115,116,5,105,0,0,116,117,5,108,0,0,117,118,5,
        101,0,0,118,24,1,0,0,0,119,120,5,98,0,0,120,121,5,114,0,0,121,122,
        5,101,0,0,122,123,5,97,0,0,123,124,5,107,0,0,124,125,5,59,0,0,125,
        26,1,0,0,0,126,127,5,112,0,0,127,128,5,114,0,0,128,129,5,105,0,0,
        129,130,5,110,0,0,130,131,5,116,0,0,131,28,1,0,0,0,132,133,5,115,
        0,0,133,134,5,99,0,0,134,135,5,97,0,0,135,136,5,110,0,0,136,137,
        5,102,0,0,137,30,1,0,0,0,138,139,5,114,0,0,139,140,5,101,0,0,140,
        141,5,116,0,0,141,142,5,117,0,0,142,143,5,114,0,0,143,144,5,110,
        0,0,144,32,1,0,0,0,145,146,5,105,0,0,146,147,5,102,0,0,147,34,1,
        0,0,0,148,149,5,101,0,0,149,150,5,108,0,0,150,151,5,115,0,0,151,
        152,5,101,0,0,152,36,1,0,0,0,153,154,5,62,0,0,154,155,5,61,0,0,155,
        38,1,0,0,0,156,157,5,60,0,0,157,158,5,61,0,0,158,40,1,0,0,0,159,
        160,5,62,0,0,160,42,1,0,0,0,161,162,5,60,0,0,162,44,1,0,0,0,163,
        164,5,61,0,0,164,165,5,61,0,0,165,46,1,0,0,0,166,167,5,33,0,0,167,
        168,5,61,0,0,168,48,1,0,0,0,169,170,5,43,0,0,170,50,1,0,0,0,171,
        172,5,45,0,0,172,52,1,0,0,0,173,174,5,42,0,0,174,54,1,0,0,0,175,
        176,5,47,0,0,176,56,1,0,0,0,177,178,5,33,0,0,178,58,1,0,0,0,179,
        180,5,105,0,0,180,181,5,110,0,0,181,195,5,116,0,0,182,183,5,115,
        0,0,183,184,5,116,0,0,184,195,5,114,0,0,185,186,5,102,0,0,186,187,
        5,108,0,0,187,188,5,111,0,0,188,189,5,97,0,0,189,195,5,116,0,0,190,
        191,5,98,0,0,191,192,5,111,0,0,192,193,5,111,0,0,193,195,5,108,0,
        0,194,179,1,0,0,0,194,182,1,0,0,0,194,185,1,0,0,0,194,190,1,0,0,
        0,195,60,1,0,0,0,196,198,7,0,0,0,197,196,1,0,0,0,198,199,1,0,0,0,
        199,197,1,0,0,0,199,200,1,0,0,0,200,62,1,0,0,0,201,203,7,0,0,0,202,
        201,1,0,0,0,203,204,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,
        206,1,0,0,0,206,208,7,1,0,0,207,209,7,0,0,0,208,207,1,0,0,0,209,
        210,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,64,1,0,0,0,212,216,
        7,2,0,0,213,215,8,2,0,0,214,213,1,0,0,0,215,218,1,0,0,0,216,214,
        1,0,0,0,216,217,1,0,0,0,217,219,1,0,0,0,218,216,1,0,0,0,219,220,
        7,2,0,0,220,66,1,0,0,0,221,222,5,84,0,0,222,223,5,114,0,0,223,224,
        5,117,0,0,224,231,5,101,0,0,225,226,5,70,0,0,226,227,5,97,0,0,227,
        228,5,108,0,0,228,229,5,115,0,0,229,231,5,101,0,0,230,221,1,0,0,
        0,230,225,1,0,0,0,231,68,1,0,0,0,232,236,7,3,0,0,233,235,7,4,0,0,
        234,233,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,
        237,70,1,0,0,0,238,236,1,0,0,0,239,241,7,5,0,0,240,239,1,0,0,0,241,
        242,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,244,1,0,0,0,244,
        245,6,35,0,0,245,72,1,0,0,0,246,247,5,47,0,0,247,248,5,47,0,0,248,
        252,1,0,0,0,249,251,9,0,0,0,250,249,1,0,0,0,251,254,1,0,0,0,252,
        253,1,0,0,0,252,250,1,0,0,0,253,255,1,0,0,0,254,252,1,0,0,0,255,
        256,5,10,0,0,256,257,1,0,0,0,257,258,6,36,0,0,258,74,1,0,0,0,259,
        260,5,47,0,0,260,261,5,42,0,0,261,265,1,0,0,0,262,264,9,0,0,0,263,
        262,1,0,0,0,264,267,1,0,0,0,265,266,1,0,0,0,265,263,1,0,0,0,266,
        268,1,0,0,0,267,265,1,0,0,0,268,269,5,42,0,0,269,270,5,47,0,0,270,
        271,1,0,0,0,271,272,6,37,0,0,272,76,1,0,0,0,11,0,194,199,204,210,
        216,230,236,242,252,265,1,6,0,0
    ]

class simplifiedJavaGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    TYPE = 30
    INT = 31
    FLOAT = 32
    STRING = 33
    BOOLEAN = 34
    ID = 35
    WS = 36
    CommentInOneLine = 37
    CommentOnMultipleLines = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "','", "')'", "':'", "'void'", "'end'", "'main'", "'var'", 
            "';'", "'const'", "'='", "'while'", "'break;'", "'print'", "'scanf'", 
            "'return'", "'if'", "'else'", "'>='", "'<='", "'>'", "'<'", 
            "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "INT", "FLOAT", "STRING", "BOOLEAN", "ID", "WS", "CommentInOneLine", 
            "CommentOnMultipleLines" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "TYPE", "INT", "FLOAT", "STRING", 
                  "BOOLEAN", "ID", "WS", "CommentInOneLine", "CommentOnMultipleLines" ]

    grammarFileName = "simplifiedJavaGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .SparqlParserListener import SparqlParserListener
else:
    from SparqlParserListener import SparqlParserListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\u00a4\u05f4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\4")
        buf.write(u"8\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@")
        buf.write(u"\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\t")
        buf.write(u"I\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R")
        buf.write(u"\tR\4S\tS\4T\tT\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4")
        buf.write(u"[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\t")
        buf.write(u"c\4d\td\4e\te\4f\tf\4g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l")
        buf.write(u"\tl\4m\tm\4n\tn\4o\to\4p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4")
        buf.write(u"u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4z\tz\4{\t{\4|\t|\4}\t}")
        buf.write(u"\4~\t~\4\177\t\177\4\u0080\t\u0080\4\u0081\t\u0081\4")
        buf.write(u"\u0082\t\u0082\4\u0083\t\u0083\4\u0084\t\u0084\4\u0085")
        buf.write(u"\t\u0085\4\u0086\t\u0086\3\2\3\2\3\2\3\2\3\2\5\2\u0112")
        buf.write(u"\n\2\3\2\3\2\3\2\3\2\5\2\u0118\n\2\3\2\5\2\u011b\n\2")
        buf.write(u"\3\3\3\3\7\3\u011f\n\3\f\3\16\3\u0122\13\3\3\4\3\4\3")
        buf.write(u"\4\3\5\3\5\3\5\3\5\3\6\3\6\7\6\u012d\n\6\f\6\16\6\u0130")
        buf.write(u"\13\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u013c")
        buf.write(u"\n\b\3\b\6\b\u013f\n\b\r\b\16\b\u0140\3\b\5\b\u0144\n")
        buf.write(u"\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u014d\n\t\3\n\3\n")
        buf.write(u"\3\n\7\n\u0152\n\n\f\n\16\n\u0155\13\n\3\n\3\n\3\n\3")
        buf.write(u"\n\7\n\u015b\n\n\f\n\16\n\u015e\13\n\3\n\3\n\3\n\5\n")
        buf.write(u"\u0163\n\n\3\n\3\n\5\n\u0167\n\n\3\13\3\13\6\13\u016b")
        buf.write(u"\n\13\r\13\16\13\u016c\3\13\5\13\u0170\n\13\3\13\7\13")
        buf.write(u"\u0173\n\13\f\13\16\13\u0176\13\13\3\13\5\13\u0179\n")
        buf.write(u"\13\3\13\3\13\3\f\3\f\7\f\u017f\n\f\f\f\16\f\u0182\13")
        buf.write(u"\f\3\f\3\f\3\f\3\r\3\r\5\r\u0189\n\r\3\r\3\r\3\16\5\16")
        buf.write(u"\u018e\n\16\3\16\3\16\3\17\5\17\u0193\n\17\3\17\5\17")
        buf.write(u"\u0196\n\17\3\17\5\17\u0199\n\17\3\17\5\17\u019c\n\17")
        buf.write(u"\3\20\3\20\3\20\6\20\u01a1\n\20\r\20\16\20\u01a2\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\5\21\u01ab\n\21\3\21\3\21\3")
        buf.write(u"\21\5\21\u01b0\n\21\3\22\3\22\6\22\u01b4\n\22\r\22\16")
        buf.write(u"\22\u01b5\3\23\3\23\3\24\3\24\3\24\6\24\u01bd\n\24\r")
        buf.write(u"\24\16\24\u01be\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5")
        buf.write(u"\25\u01c8\n\25\3\26\3\26\5\26\u01cc\n\26\3\26\3\26\5")
        buf.write(u"\26\u01d0\n\26\5\26\u01d2\n\26\3\27\3\27\3\27\3\30\3")
        buf.write(u"\30\3\30\3\31\3\31\5\31\u01dc\n\31\3\32\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\7\32\u01e4\n\32\f\32\16\32\u01e7\13\32\3\32")
        buf.write(u"\3\32\5\32\u01eb\n\32\5\32\u01ed\n\32\3\33\3\33\3\33")
        buf.write(u"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u01fa\n")
        buf.write(u"\33\3\34\3\34\5\34\u01fe\n\34\3\34\3\34\3\34\5\34\u0203")
        buf.write(u"\n\34\3\35\3\35\5\35\u0207\n\35\3\35\3\35\3\36\3\36\5")
        buf.write(u"\36\u020d\n\36\3\36\3\36\3\37\3\37\5\37\u0213\n\37\3")
        buf.write(u"\37\3\37\3 \3 \5 \u0219\n \3 \3 \3 \3 \3!\3!\5!\u0221")
        buf.write(u"\n!\3!\3!\3!\3!\3\"\3\"\5\"\u0229\n\"\3\"\3\"\3\"\3\"")
        buf.write(u"\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\5&\u023d\n")
        buf.write(u"&\3&\3&\5&\u0241\n&\3&\5&\u0244\n&\3&\7&\u0247\n&\f&")
        buf.write(u"\16&\u024a\13&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\5")
        buf.write(u")\u0257\n)\3)\3)\3*\3*\5*\u025d\n*\3*\5*\u0260\n*\3+")
        buf.write(u"\3+\3+\3,\3,\3,\3,\5,\u0269\n,\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(u".\3/\5/\u0274\n/\3/\7/\u0277\n/\f/\16/\u027a\13/\3\60")
        buf.write(u"\3\60\5\60\u027e\n\60\3\60\5\60\u0281\n\60\3\61\3\61")
        buf.write(u"\3\61\3\61\5\61\u0287\n\61\3\61\3\61\3\62\3\62\3\62\5")
        buf.write(u"\62\u028e\n\62\7\62\u0290\n\62\f\62\16\62\u0293\13\62")
        buf.write(u"\3\63\3\63\3\63\5\63\u0298\n\63\3\63\3\63\3\64\5\64\u029d")
        buf.write(u"\n\64\3\64\7\64\u02a0\n\64\f\64\16\64\u02a3\13\64\3\65")
        buf.write(u"\3\65\5\65\u02a7\n\65\3\65\5\65\u02aa\n\65\3\66\3\66")
        buf.write(u"\3\66\5\66\u02af\n\66\7\66\u02b1\n\66\f\66\16\66\u02b4")
        buf.write(u"\13\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u02be")
        buf.write(u"\n\67\38\38\38\39\39\39\39\3:\3:\5:\u02c9\n:\3:\3:\3")
        buf.write(u":\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3=\3=\5=\u02da\n=\3>")
        buf.write(u"\3>\3>\7>\u02df\n>\f>\16>\u02e2\13>\3>\3>\3?\3?\7?\u02e8")
        buf.write(u"\n?\f?\16?\u02eb\13?\3?\3?\3?\7?\u02f0\n?\f?\16?\u02f3")
        buf.write(u"\13?\3?\3?\3@\3@\7@\u02f9\n@\f@\16@\u02fc\13@\3@\3@\3")
        buf.write(u"A\3A\3A\3A\3A\5A\u0305\nA\3B\3B\3B\3C\3C\3C\7C\u030d")
        buf.write(u"\nC\fC\16C\u0310\13C\3D\3D\3D\3E\3E\3E\3E\3E\3E\5E\u031b")
        buf.write(u"\nE\3F\3F\3F\3G\3G\5G\u0322\nG\3G\3G\5G\u0326\nG\3G\3")
        buf.write(u"G\3H\3H\3H\7H\u032d\nH\fH\16H\u0330\13H\3I\3I\5I\u0334")
        buf.write(u"\nI\3I\3I\3J\3J\3J\5J\u033b\nJ\7J\u033d\nJ\fJ\16J\u0340")
        buf.write(u"\13J\3K\3K\3K\3K\3K\3K\5K\u0348\nK\3L\5L\u034b\nL\3M")
        buf.write(u"\3M\3M\3M\3M\3M\5M\u0353\nM\7M\u0355\nM\fM\16M\u0358")
        buf.write(u"\13M\3N\3N\5N\u035c\nN\3O\3O\3O\7O\u0361\nO\fO\16O\u0364")
        buf.write(u"\13O\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u036e\nQ\3R\5R\u0371")
        buf.write(u"\nR\3S\3S\5S\u0375\nS\3S\3S\3S\5S\u037a\nS\7S\u037c\n")
        buf.write(u"S\fS\16S\u037f\13S\3T\3T\5T\u0383\nT\3T\3T\3U\3U\3V\3")
        buf.write(u"V\3W\3W\3W\7W\u038e\nW\fW\16W\u0391\13W\3X\3X\3Y\3Y\3")
        buf.write(u"Z\3Z\3Z\7Z\u039a\nZ\fZ\16Z\u039d\13Z\3[\3[\3[\7[\u03a2")
        buf.write(u"\n[\f[\16[\u03a5\13[\3\\\3\\\5\\\u03a9\n\\\3]\5]\u03ac")
        buf.write(u"\n]\3]\3]\3^\3^\3_\3_\3_\3_\3_\3_\3_\3_\5_\u03ba\n_\3")
        buf.write(u"`\3`\3`\3`\3`\7`\u03c1\n`\f`\16`\u03c4\13`\5`\u03c6\n")
        buf.write(u"`\3`\5`\u03c9\n`\3a\5a\u03cc\na\3a\3a\5a\u03d0\na\3b")
        buf.write(u"\3b\3c\3c\5c\u03d6\nc\3d\3d\3d\3d\3e\3e\5e\u03de\ne\3")
        buf.write(u"f\3f\3f\3f\3g\3g\6g\u03e6\ng\rg\16g\u03e7\3g\3g\3h\3")
        buf.write(u"h\6h\u03ee\nh\rh\16h\u03ef\3h\3h\3i\3i\5i\u03f6\ni\3")
        buf.write(u"j\3j\5j\u03fa\nj\3k\3k\5k\u03fe\nk\3l\3l\5l\u0402\nl")
        buf.write(u"\3m\3m\3n\3n\3n\3n\3n\3n\5n\u040c\nn\3o\3o\3o\3p\3p\3")
        buf.write(u"p\3p\3p\3p\3p\3p\5p\u0419\np\3p\3p\3p\3p\3p\3p\3p\3p")
        buf.write(u"\3p\3p\3p\3p\3p\5p\u0428\np\3p\3p\3p\5p\u042d\np\3p\3")
        buf.write(u"p\3p\3p\3p\3p\3p\7p\u0436\np\fp\16p\u0439\13p\3q\3q\5")
        buf.write(u"q\u043d\nq\3q\3q\5q\u0441\nq\3r\5r\u0444\nr\3r\3r\3s")
        buf.write(u"\3s\3s\3s\3s\3s\3s\3s\3s\3s\5s\u0452\ns\3t\3t\3t\3t\3")
        buf.write(u"t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t")
        buf.write(u"\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write(u"t\3t\5t\u047d\nt\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t")
        buf.write(u"\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\5t\u049a")
        buf.write(u"\nt\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write(u"t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t")
        buf.write(u"\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write(u"t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t")
        buf.write(u"\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write(u"t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t")
        buf.write(u"\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write(u"t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\5t\u0523\nt")
        buf.write(u"\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write(u"t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t")
        buf.write(u"\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write(u"t\3t\3t\3t\3t\3t\3t\5t\u0560\nt\3u\3u\3u\3u\3u\3u\3u")
        buf.write(u"\5u\u0569\nu\3u\3u\3v\3v\3v\3v\3v\3v\3v\5v\u0574\nv\3")
        buf.write(u"v\3v\3w\3w\3w\3w\3w\3w\3w\3w\3w\5w\u0581\nw\3w\3w\3x")
        buf.write(u"\3x\3x\3y\3y\3y\3y\3z\3z\3z\5z\u058f\nz\3z\3z\5z\u0593")
        buf.write(u"\nz\3z\3z\3z\3z\5z\u0599\nz\3z\3z\3z\3z\3z\3z\5z\u05a1")
        buf.write(u"\nz\3z\3z\3z\3z\3z\3z\5z\u05a9\nz\3z\3z\3z\3z\3z\3z\5")
        buf.write(u"z\u05b1\nz\3z\3z\3z\3z\3z\3z\5z\u05b9\nz\3z\3z\3z\3z")
        buf.write(u"\3z\3z\5z\u05c1\nz\3z\3z\3z\3z\3z\5z\u05c8\nz\3z\3z\5")
        buf.write(u"z\u05cc\nz\3{\3{\5{\u05d0\n{\3|\3|\3|\3|\5|\u05d6\n|")
        buf.write(u"\3}\3}\3}\5}\u05db\n}\3~\3~\3\177\3\177\3\u0080\3\u0080")
        buf.write(u"\3\u0081\3\u0081\3\u0082\3\u0082\3\u0083\3\u0083\5\u0083")
        buf.write(u"\u05e9\n\u0083\3\u0084\3\u0084\3\u0085\3\u0085\5\u0085")
        buf.write(u"\u05ef\n\u0085\3\u0086\3\u0086\3\u0086\3\u0086\2\3\u00de")
        buf.write(u"\u0087\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(u",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write(u"\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write(u"\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4")
        buf.write(u"\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6")
        buf.write(u"\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6\u00c8")
        buf.write(u"\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da")
        buf.write(u"\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec")
        buf.write(u"\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe")
        buf.write(u"\u0100\u0102\u0104\u0106\u0108\u010a\2\20\3\2\7\b\3\2")
        buf.write(u"\21\22\4\2\u0099\u0099\u009b\u009c\3\2yz\4\2\u009b\u009b")
        buf.write(u"\u009f\u009f\3\2\u0099\u009a\4\2\u008b\u008d\u00a0\u00a2")
        buf.write(u"\4\2\u0099\u009a\u009e\u009e\3\2|~\3\2\177\u0081\3\2")
        buf.write(u"\u0082\u0084\3\2\'(\3\2\u0085\u0088\3\2vw\u066b\2\u011a")
        buf.write(u"\3\2\2\2\4\u0120\3\2\2\2\6\u0123\3\2\2\2\b\u0126\3\2")
        buf.write(u"\2\2\n\u012a\3\2\2\2\f\u0134\3\2\2\2\16\u0139\3\2\2\2")
        buf.write(u"\20\u014c\3\2\2\2\22\u014e\3\2\2\2\24\u0168\3\2\2\2\26")
        buf.write(u"\u017c\3\2\2\2\30\u0186\3\2\2\2\32\u018d\3\2\2\2\34\u0192")
        buf.write(u"\3\2\2\2\36\u019d\3\2\2\2 \u01af\3\2\2\2\"\u01b1\3\2")
        buf.write(u"\2\2$\u01b7\3\2\2\2&\u01b9\3\2\2\2(\u01c7\3\2\2\2*\u01d1")
        buf.write(u"\3\2\2\2,\u01d3\3\2\2\2.\u01d6\3\2\2\2\60\u01db\3\2\2")
        buf.write(u"\2\62\u01dd\3\2\2\2\64\u01f9\3\2\2\2\66\u01fb\3\2\2\2")
        buf.write(u"8\u0204\3\2\2\2:\u020a\3\2\2\2<\u0210\3\2\2\2>\u0216")
        buf.write(u"\3\2\2\2@\u021e\3\2\2\2B\u0226\3\2\2\2D\u022e\3\2\2\2")
        buf.write(u"F\u0232\3\2\2\2H\u0236\3\2\2\2J\u023c\3\2\2\2L\u024e")
        buf.write(u"\3\2\2\2N\u0251\3\2\2\2P\u0254\3\2\2\2R\u025f\3\2\2\2")
        buf.write(u"T\u0261\3\2\2\2V\u0268\3\2\2\2X\u026a\3\2\2\2Z\u026e")
        buf.write(u"\3\2\2\2\\\u0273\3\2\2\2^\u027b\3\2\2\2`\u0282\3\2\2")
        buf.write(u"\2b\u028a\3\2\2\2d\u0294\3\2\2\2f\u029c\3\2\2\2h\u02a4")
        buf.write(u"\3\2\2\2j\u02ab\3\2\2\2l\u02bd\3\2\2\2n\u02bf\3\2\2\2")
        buf.write(u"p\u02c2\3\2\2\2r\u02c6\3\2\2\2t\u02cd\3\2\2\2v\u02d4")
        buf.write(u"\3\2\2\2x\u02d9\3\2\2\2z\u02db\3\2\2\2|\u02e5\3\2\2\2")
        buf.write(u"~\u02f6\3\2\2\2\u0080\u0304\3\2\2\2\u0082\u0306\3\2\2")
        buf.write(u"\2\u0084\u0309\3\2\2\2\u0086\u0311\3\2\2\2\u0088\u031a")
        buf.write(u"\3\2\2\2\u008a\u031c\3\2\2\2\u008c\u031f\3\2\2\2\u008e")
        buf.write(u"\u0329\3\2\2\2\u0090\u0331\3\2\2\2\u0092\u0337\3\2\2")
        buf.write(u"\2\u0094\u0347\3\2\2\2\u0096\u034a\3\2\2\2\u0098\u034c")
        buf.write(u"\3\2\2\2\u009a\u035b\3\2\2\2\u009c\u035d\3\2\2\2\u009e")
        buf.write(u"\u0365\3\2\2\2\u00a0\u036d\3\2\2\2\u00a2\u0370\3\2\2")
        buf.write(u"\2\u00a4\u0374\3\2\2\2\u00a6\u0382\3\2\2\2\u00a8\u0386")
        buf.write(u"\3\2\2\2\u00aa\u0388\3\2\2\2\u00ac\u038a\3\2\2\2\u00ae")
        buf.write(u"\u0392\3\2\2\2\u00b0\u0394\3\2\2\2\u00b2\u0396\3\2\2")
        buf.write(u"\2\u00b4\u039e\3\2\2\2\u00b6\u03a6\3\2\2\2\u00b8\u03ab")
        buf.write(u"\3\2\2\2\u00ba\u03af\3\2\2\2\u00bc\u03b9\3\2\2\2\u00be")
        buf.write(u"\u03c8\3\2\2\2\u00c0\u03cb\3\2\2\2\u00c2\u03d1\3\2\2")
        buf.write(u"\2\u00c4\u03d5\3\2\2\2\u00c6\u03d7\3\2\2\2\u00c8\u03dd")
        buf.write(u"\3\2\2\2\u00ca\u03df\3\2\2\2\u00cc\u03e3\3\2\2\2\u00ce")
        buf.write(u"\u03eb\3\2\2\2\u00d0\u03f5\3\2\2\2\u00d2\u03f9\3\2\2")
        buf.write(u"\2\u00d4\u03fd\3\2\2\2\u00d6\u0401\3\2\2\2\u00d8\u0403")
        buf.write(u"\3\2\2\2\u00da\u040b\3\2\2\2\u00dc\u040d\3\2\2\2\u00de")
        buf.write(u"\u0418\3\2\2\2\u00e0\u043c\3\2\2\2\u00e2\u0443\3\2\2")
        buf.write(u"\2\u00e4\u0451\3\2\2\2\u00e6\u055f\3\2\2\2\u00e8\u0561")
        buf.write(u"\3\2\2\2\u00ea\u056c\3\2\2\2\u00ec\u0577\3\2\2\2\u00ee")
        buf.write(u"\u0584\3\2\2\2\u00f0\u0587\3\2\2\2\u00f2\u05cb\3\2\2")
        buf.write(u"\2\u00f4\u05cd\3\2\2\2\u00f6\u05d1\3\2\2\2\u00f8\u05da")
        buf.write(u"\3\2\2\2\u00fa\u05dc\3\2\2\2\u00fc\u05de\3\2\2\2\u00fe")
        buf.write(u"\u05e0\3\2\2\2\u0100\u05e2\3\2\2\2\u0102\u05e4\3\2\2")
        buf.write(u"\2\u0104\u05e8\3\2\2\2\u0106\u05ea\3\2\2\2\u0108\u05ee")
        buf.write(u"\3\2\2\2\u010a\u05f0\3\2\2\2\u010c\u0111\5\4\3\2\u010d")
        buf.write(u"\u0112\5\n\6\2\u010e\u0112\5\22\n\2\u010f\u0112\5\24")
        buf.write(u"\13\2\u0110\u0112\5\26\f\2\u0111\u010d\3\2\2\2\u0111")
        buf.write(u"\u010e\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0110\3\2\2")
        buf.write(u"\2\u0111\u0112\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114")
        buf.write(u"\5\60\31\2\u0114\u0115\7\2\2\3\u0115\u011b\3\2\2\2\u0116")
        buf.write(u"\u0118\5\62\32\2\u0117\u0116\3\2\2\2\u0117\u0118\3\2")
        buf.write(u"\2\2\u0118\u0119\3\2\2\2\u0119\u011b\7\2\2\3\u011a\u010c")
        buf.write(u"\3\2\2\2\u011a\u0117\3\2\2\2\u011b\3\3\2\2\2\u011c\u011f")
        buf.write(u"\5\6\4\2\u011d\u011f\5\b\5\2\u011e\u011c\3\2\2\2\u011e")
        buf.write(u"\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2")
        buf.write(u"\2\u0120\u0121\3\2\2\2\u0121\5\3\2\2\2\u0122\u0120\3")
        buf.write(u"\2\2\2\u0123\u0124\7\4\2\2\u0124\u0125\7u\2\2\u0125\7")
        buf.write(u"\3\2\2\2\u0126\u0127\7\5\2\2\u0127\u0128\7v\2\2\u0128")
        buf.write(u"\u0129\7u\2\2\u0129\t\3\2\2\2\u012a\u012e\5\16\b\2\u012b")
        buf.write(u"\u012d\5\30\r\2\u012c\u012b\3\2\2\2\u012d\u0130\3\2\2")
        buf.write(u"\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0131")
        buf.write(u"\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132\5\32\16\2\u0132")
        buf.write(u"\u0133\5\34\17\2\u0133\13\3\2\2\2\u0134\u0135\5\16\b")
        buf.write(u"\2\u0135\u0136\5\32\16\2\u0136\u0137\5\34\17\2\u0137")
        buf.write(u"\u0138\5\60\31\2\u0138\r\3\2\2\2\u0139\u013b\7\6\2\2")
        buf.write(u"\u013a\u013c\t\2\2\2\u013b\u013a\3\2\2\2\u013b\u013c")
        buf.write(u"\3\2\2\2\u013c\u0143\3\2\2\2\u013d\u013f\5\20\t\2\u013e")
        buf.write(u"\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u013e\3\2\2")
        buf.write(u"\2\u0140\u0141\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0144")
        buf.write(u"\7\u009b\2\2\u0143\u013e\3\2\2\2\u0143\u0142\3\2\2\2")
        buf.write(u"\u0144\17\3\2\2\2\u0145\u014d\5\u00d8m\2\u0146\u0147")
        buf.write(u"\7\u0091\2\2\u0147\u0148\5\u00dep\2\u0148\u0149\7:\2")
        buf.write(u"\2\u0149\u014a\5\u00d8m\2\u014a\u014b\7\u0092\2\2\u014b")
        buf.write(u"\u014d\3\2\2\2\u014c\u0145\3\2\2\2\u014c\u0146\3\2\2")
        buf.write(u"\2\u014d\21\3\2\2\2\u014e\u0166\7\t\2\2\u014f\u0153\5")
        buf.write(u"\u0090I\2\u0150\u0152\5\30\r\2\u0151\u0150\3\2\2\2\u0152")
        buf.write(u"\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2")
        buf.write(u"\2\u0154\u0156\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u0157")
        buf.write(u"\5\32\16\2\u0157\u0158\5\34\17\2\u0158\u0167\3\2\2\2")
        buf.write(u"\u0159\u015b\5\30\r\2\u015a\u0159\3\2\2\2\u015b\u015e")
        buf.write(u"\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write(u"\u015f\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\7\16\2")
        buf.write(u"\2\u0160\u0162\7\u0093\2\2\u0161\u0163\5b\62\2\u0162")
        buf.write(u"\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2")
        buf.write(u"\2\u0164\u0165\7\u0094\2\2\u0165\u0167\5\34\17\2\u0166")
        buf.write(u"\u014f\3\2\2\2\u0166\u015c\3\2\2\2\u0167\23\3\2\2\2\u0168")
        buf.write(u"\u016f\7\n\2\2\u0169\u016b\5\u00d6l\2\u016a\u0169\3\2")
        buf.write(u"\2\2\u016b\u016c\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d")
        buf.write(u"\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u0170\7\u009b\2\2")
        buf.write(u"\u016f\u016a\3\2\2\2\u016f\u016e\3\2\2\2\u0170\u0174")
        buf.write(u"\3\2\2\2\u0171\u0173\5\30\r\2\u0172\u0171\3\2\2\2\u0173")
        buf.write(u"\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2")
        buf.write(u"\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0179")
        buf.write(u"\5\32\16\2\u0178\u0177\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write(u"\u017a\3\2\2\2\u017a\u017b\5\34\17\2\u017b\25\3\2\2\2")
        buf.write(u"\u017c\u0180\7\13\2\2\u017d\u017f\5\30\r\2\u017e\u017d")
        buf.write(u"\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180")
        buf.write(u"\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0180\3\2\2")
        buf.write(u"\2\u0183\u0184\5\32\16\2\u0184\u0185\5\34\17\2\u0185")
        buf.write(u"\27\3\2\2\2\u0186\u0188\7\f\2\2\u0187\u0189\7\r\2\2\u0188")
        buf.write(u"\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\3\2\2")
        buf.write(u"\2\u018a\u018b\5\u0104\u0083\2\u018b\31\3\2\2\2\u018c")
        buf.write(u"\u018e\7\16\2\2\u018d\u018c\3\2\2\2\u018d\u018e\3\2\2")
        buf.write(u"\2\u018e\u018f\3\2\2\2\u018f\u0190\5d\63\2\u0190\33\3")
        buf.write(u"\2\2\2\u0191\u0193\5\36\20\2\u0192\u0191\3\2\2\2\u0192")
        buf.write(u"\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0196\5\"\22")
        buf.write(u"\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0198")
        buf.write(u"\3\2\2\2\u0197\u0199\5&\24\2\u0198\u0197\3\2\2\2\u0198")
        buf.write(u"\u0199\3\2\2\2\u0199\u019b\3\2\2\2\u019a\u019c\5*\26")
        buf.write(u"\2\u019b\u019a\3\2\2\2\u019b\u019c\3\2\2\2\u019c\35\3")
        buf.write(u"\2\2\2\u019d\u019e\7;\2\2\u019e\u01a0\7\20\2\2\u019f")
        buf.write(u"\u01a1\5 \21\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2")
        buf.write(u"\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\37\3")
        buf.write(u"\2\2\2\u01a4\u01b0\5\u00e6t\2\u01a5\u01b0\5\u008aF\2")
        buf.write(u"\u01a6\u01a7\7\u0091\2\2\u01a7\u01aa\5\u00dep\2\u01a8")
        buf.write(u"\u01a9\7:\2\2\u01a9\u01ab\5\u00d8m\2\u01aa\u01a8\3\2")
        buf.write(u"\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad")
        buf.write(u"\7\u0092\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01b0\5\u00d8")
        buf.write(u"m\2\u01af\u01a4\3\2\2\2\u01af\u01a5\3\2\2\2\u01af\u01a6")
        buf.write(u"\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0!\3\2\2\2\u01b1\u01b3")
        buf.write(u"\7<\2\2\u01b2\u01b4\5$\23\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write(u"\u01b5\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2")
        buf.write(u"\2\u01b6#\3\2\2\2\u01b7\u01b8\5\u0088E\2\u01b8%\3\2\2")
        buf.write(u"\2\u01b9\u01ba\7\17\2\2\u01ba\u01bc\7\20\2\2\u01bb\u01bd")
        buf.write(u"\5(\25\2\u01bc\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be")
        buf.write(u"\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\'\3\2\2\2\u01c0")
        buf.write(u"\u01c1\t\3\2\2\u01c1\u01c2\7\u0091\2\2\u01c2\u01c3\5")
        buf.write(u"\u00dep\2\u01c3\u01c4\7\u0092\2\2\u01c4\u01c8\3\2\2\2")
        buf.write(u"\u01c5\u01c8\5\u0088E\2\u01c6\u01c8\5\u00d8m\2\u01c7")
        buf.write(u"\u01c0\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c6\3\2\2")
        buf.write(u"\2\u01c8)\3\2\2\2\u01c9\u01cb\5,\27\2\u01ca\u01cc\5.")
        buf.write(u"\30\2\u01cb\u01ca\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01d2")
        buf.write(u"\3\2\2\2\u01cd\u01cf\5.\30\2\u01ce\u01d0\5,\27\2\u01cf")
        buf.write(u"\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2\3\2\2")
        buf.write(u"\2\u01d1\u01c9\3\2\2\2\u01d1\u01cd\3\2\2\2\u01d2+\3\2")
        buf.write(u"\2\2\u01d3\u01d4\7\23\2\2\u01d4\u01d5\7|\2\2\u01d5-\3")
        buf.write(u"\2\2\2\u01d6\u01d7\7\24\2\2\u01d7\u01d8\7|\2\2\u01d8")
        buf.write(u"/\3\2\2\2\u01d9\u01da\7\25\2\2\u01da\u01dc\5x=\2\u01db")
        buf.write(u"\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\61\3\2\2\2\u01dd")
        buf.write(u"\u01ec\5\4\3\2\u01de\u01e5\5\64\33\2\u01df\u01e0\7\u0097")
        buf.write(u"\2\2\u01e0\u01e1\5\4\3\2\u01e1\u01e2\5\64\33\2\u01e2")
        buf.write(u"\u01e4\3\2\2\2\u01e3\u01df\3\2\2\2\u01e4\u01e7\3\2\2")
        buf.write(u"\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01ea")
        buf.write(u"\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01e9\7\u0097\2\2")
        buf.write(u"\u01e9\u01eb\5\4\3\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb")
        buf.write(u"\3\2\2\2\u01eb\u01ed\3\2\2\2\u01ec\u01de\3\2\2\2\u01ec")
        buf.write(u"\u01ed\3\2\2\2\u01ed\63\3\2\2\2\u01ee\u01fa\5\66\34\2")
        buf.write(u"\u01ef\u01fa\58\35\2\u01f0\u01fa\5:\36\2\u01f1\u01fa")
        buf.write(u"\5> \2\u01f2\u01fa\5@!\2\u01f3\u01fa\5B\"\2\u01f4\u01fa")
        buf.write(u"\5<\37\2\u01f5\u01fa\5D#\2\u01f6\u01fa\5F$\2\u01f7\u01fa")
        buf.write(u"\5H%\2\u01f8\u01fa\5J&\2\u01f9\u01ee\3\2\2\2\u01f9\u01ef")
        buf.write(u"\3\2\2\2\u01f9\u01f0\3\2\2\2\u01f9\u01f1\3\2\2\2\u01f9")
        buf.write(u"\u01f2\3\2\2\2\u01f9\u01f3\3\2\2\2\u01f9\u01f4\3\2\2")
        buf.write(u"\2\u01f9\u01f5\3\2\2\2\u01f9\u01f6\3\2\2\2\u01f9\u01f7")
        buf.write(u"\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fa\65\3\2\2\2\u01fb\u01fd")
        buf.write(u"\7)\2\2\u01fc\u01fe\7\63\2\2\u01fd\u01fc\3\2\2\2\u01fd")
        buf.write(u"\u01fe\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0202\5\u0104")
        buf.write(u"\u0083\2\u0200\u0201\78\2\2\u0201\u0203\5T+\2\u0202\u0200")
        buf.write(u"\3\2\2\2\u0202\u0203\3\2\2\2\u0203\67\3\2\2\2\u0204\u0206")
        buf.write(u"\7*\2\2\u0205\u0207\7\63\2\2\u0206\u0205\3\2\2\2\u0206")
        buf.write(u"\u0207\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0209\5V,\2")
        buf.write(u"\u02099\3\2\2\2\u020a\u020c\7+\2\2\u020b\u020d\7\63\2")
        buf.write(u"\2\u020c\u020b\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020e")
        buf.write(u"\3\2\2\2\u020e\u020f\5V,\2\u020f;\3\2\2\2\u0210\u0212")
        buf.write(u"\7/\2\2\u0211\u0213\7\63\2\2\u0212\u0211\3\2\2\2\u0212")
        buf.write(u"\u0213\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215\5T+\2")
        buf.write(u"\u0215=\3\2\2\2\u0216\u0218\7,\2\2\u0217\u0219\7\63\2")
        buf.write(u"\2\u0218\u0217\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021a")
        buf.write(u"\3\2\2\2\u021a\u021b\5R*\2\u021b\u021c\79\2\2\u021c\u021d")
        buf.write(u"\5R*\2\u021d?\3\2\2\2\u021e\u0220\7-\2\2\u021f\u0221")
        buf.write(u"\7\63\2\2\u0220\u021f\3\2\2\2\u0220\u0221\3\2\2\2\u0221")
        buf.write(u"\u0222\3\2\2\2\u0222\u0223\5R*\2\u0223\u0224\79\2\2\u0224")
        buf.write(u"\u0225\5R*\2\u0225A\3\2\2\2\u0226\u0228\7.\2\2\u0227")
        buf.write(u"\u0229\7\63\2\2\u0228\u0227\3\2\2\2\u0228\u0229\3\2\2")
        buf.write(u"\2\u0229\u022a\3\2\2\2\u022a\u022b\5R*\2\u022b\u022c")
        buf.write(u"\79\2\2\u022c\u022d\5R*\2\u022dC\3\2\2\2\u022e\u022f")
        buf.write(u"\7\61\2\2\u022f\u0230\7\66\2\2\u0230\u0231\5Z.\2\u0231")
        buf.write(u"E\3\2\2\2\u0232\u0233\7\60\2\2\u0233\u0234\7\66\2\2\u0234")
        buf.write(u"\u0235\5Z.\2\u0235G\3\2\2\2\u0236\u0237\7\60\2\2\u0237")
        buf.write(u"\u0238\7\16\2\2\u0238\u0239\5X-\2\u0239I\3\2\2\2\u023a")
        buf.write(u"\u023b\7\67\2\2\u023b\u023d\5\u0104\u0083\2\u023c\u023a")
        buf.write(u"\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u0243\3\2\2\2\u023e")
        buf.write(u"\u0240\5L\'\2\u023f\u0241\5N(\2\u0240\u023f\3\2\2\2\u0240")
        buf.write(u"\u0241\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0244\5N(\2")
        buf.write(u"\u0243\u023e\3\2\2\2\u0243\u0242\3\2\2\2\u0244\u0248")
        buf.write(u"\3\2\2\2\u0245\u0247\5P)\2\u0246\u0245\3\2\2\2\u0247")
        buf.write(u"\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2")
        buf.write(u"\2\u0249\u024b\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024c")
        buf.write(u"\7\16\2\2\u024c\u024d\5d\63\2\u024dK\3\2\2\2\u024e\u024f")
        buf.write(u"\7\60\2\2\u024f\u0250\5X-\2\u0250M\3\2\2\2\u0251\u0252")
        buf.write(u"\7\61\2\2\u0252\u0253\5X-\2\u0253O\3\2\2\2\u0254\u0256")
        buf.write(u"\7\62\2\2\u0255\u0257\7\r\2\2\u0256\u0255\3\2\2\2\u0256")
        buf.write(u"\u0257\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0259\5\u0104")
        buf.write(u"\u0083\2\u0259Q\3\2\2\2\u025a\u0260\7\64\2\2\u025b\u025d")
        buf.write(u"\7\27\2\2\u025c\u025b\3\2\2\2\u025c\u025d\3\2\2\2\u025d")
        buf.write(u"\u025e\3\2\2\2\u025e\u0260\5\u0104\u0083\2\u025f\u025a")
        buf.write(u"\3\2\2\2\u025f\u025c\3\2\2\2\u0260S\3\2\2\2\u0261\u0262")
        buf.write(u"\7\27\2\2\u0262\u0263\5\u0104\u0083\2\u0263U\3\2\2\2")
        buf.write(u"\u0264\u0269\5T+\2\u0265\u0269\7\64\2\2\u0266\u0269\7")
        buf.write(u"\r\2\2\u0267\u0269\7\65\2\2\u0268\u0264\3\2\2\2\u0268")
        buf.write(u"\u0265\3\2\2\2\u0268\u0266\3\2\2\2\u0268\u0267\3\2\2")
        buf.write(u"\2\u0269W\3\2\2\2\u026a\u026b\7\u0093\2\2\u026b\u026c")
        buf.write(u"\5\\/\2\u026c\u026d\7\u0094\2\2\u026dY\3\2\2\2\u026e")
        buf.write(u"\u026f\7\u0093\2\2\u026f\u0270\5\\/\2\u0270\u0271\7\u0094")
        buf.write(u"\2\2\u0271[\3\2\2\2\u0272\u0274\5b\62\2\u0273\u0272\3")
        buf.write(u"\2\2\2\u0273\u0274\3\2\2\2\u0274\u0278\3\2\2\2\u0275")
        buf.write(u"\u0277\5^\60\2\u0276\u0275\3\2\2\2\u0277\u027a\3\2\2")
        buf.write(u"\2\u0278\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279]\3\2")
        buf.write(u"\2\2\u027a\u0278\3\2\2\2\u027b\u027d\5`\61\2\u027c\u027e")
        buf.write(u"\7\u0098\2\2\u027d\u027c\3\2\2\2\u027d\u027e\3\2\2\2")
        buf.write(u"\u027e\u0280\3\2\2\2\u027f\u0281\5b\62\2\u0280\u027f")
        buf.write(u"\3\2\2\2\u0280\u0281\3\2\2\2\u0281_\3\2\2\2\u0282\u0283")
        buf.write(u"\7\27\2\2\u0283\u0284\5\u00d6l\2\u0284\u0286\7\u0093")
        buf.write(u"\2\2\u0285\u0287\5b\62\2\u0286\u0285\3\2\2\2\u0286\u0287")
        buf.write(u"\3\2\2\2\u0287\u0288\3\2\2\2\u0288\u0289\7\u0094\2\2")
        buf.write(u"\u0289a\3\2\2\2\u028a\u0291\5\u0094K\2\u028b\u028d\7")
        buf.write(u"\u0098\2\2\u028c\u028e\5\u0094K\2\u028d\u028c\3\2\2\2")
        buf.write(u"\u028d\u028e\3\2\2\2\u028e\u0290\3\2\2\2\u028f\u028b")
        buf.write(u"\3\2\2\2\u0290\u0293\3\2\2\2\u0291\u028f\3\2\2\2\u0291")
        buf.write(u"\u0292\3\2\2\2\u0292c\3\2\2\2\u0293\u0291\3\2\2\2\u0294")
        buf.write(u"\u0297\7\u0093\2\2\u0295\u0298\5\f\7\2\u0296\u0298\5")
        buf.write(u"f\64\2\u0297\u0295\3\2\2\2\u0297\u0296\3\2\2\2\u0298")
        buf.write(u"\u0299\3\2\2\2\u0299\u029a\7\u0094\2\2\u029ae\3\2\2\2")
        buf.write(u"\u029b\u029d\5j\66\2\u029c\u029b\3\2\2\2\u029c\u029d")
        buf.write(u"\3\2\2\2\u029d\u02a1\3\2\2\2\u029e\u02a0\5h\65\2\u029f")
        buf.write(u"\u029e\3\2\2\2\u02a0\u02a3\3\2\2\2\u02a1\u029f\3\2\2")
        buf.write(u"\2\u02a1\u02a2\3\2\2\2\u02a2g\3\2\2\2\u02a3\u02a1\3\2")
        buf.write(u"\2\2\u02a4\u02a6\5l\67\2\u02a5\u02a7\7\u0098\2\2\u02a6")
        buf.write(u"\u02a5\3\2\2\2\u02a6\u02a7\3\2\2\2\u02a7\u02a9\3\2\2")
        buf.write(u"\2\u02a8\u02aa\5j\66\2\u02a9\u02a8\3\2\2\2\u02a9\u02aa")
        buf.write(u"\3\2\2\2\u02aai\3\2\2\2\u02ab\u02b2\5\u00a0Q\2\u02ac")
        buf.write(u"\u02ae\7\u0098\2\2\u02ad\u02af\5\u00a0Q\2\u02ae\u02ad")
        buf.write(u"\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u02b1\3\2\2\2\u02b0")
        buf.write(u"\u02ac\3\2\2\2\u02b1\u02b4\3\2\2\2\u02b2\u02b0\3\2\2")
        buf.write(u"\2\u02b2\u02b3\3\2\2\2\u02b3k\3\2\2\2\u02b4\u02b2\3\2")
        buf.write(u"\2\2\u02b5\u02be\5\u0084C\2\u02b6\u02be\5n8\2\u02b7\u02be")
        buf.write(u"\5\u0082B\2\u02b8\u02be\5p9\2\u02b9\u02be\5r:\2\u02ba")
        buf.write(u"\u02be\5\u0086D\2\u02bb\u02be\5t;\2\u02bc\u02be\5v<\2")
        buf.write(u"\u02bd\u02b5\3\2\2\2\u02bd\u02b6\3\2\2\2\u02bd\u02b7")
        buf.write(u"\3\2\2\2\u02bd\u02b8\3\2\2\2\u02bd\u02b9\3\2\2\2\u02bd")
        buf.write(u"\u02ba\3\2\2\2\u02bd\u02bb\3\2\2\2\u02bd\u02bc\3\2\2")
        buf.write(u"\2\u02bem\3\2\2\2\u02bf\u02c0\7\26\2\2\u02c0\u02c1\5")
        buf.write(u"d\63\2\u02c1o\3\2\2\2\u02c2\u02c3\7\27\2\2\u02c3\u02c4")
        buf.write(u"\5\u00d6l\2\u02c4\u02c5\5d\63\2\u02c5q\3\2\2\2\u02c6")
        buf.write(u"\u02c8\7?\2\2\u02c7\u02c9\7\63\2\2\u02c8\u02c7\3\2\2")
        buf.write(u"\2\u02c8\u02c9\3\2\2\2\u02c9\u02ca\3\2\2\2\u02ca\u02cb")
        buf.write(u"\5\u00d6l\2\u02cb\u02cc\5d\63\2\u02ccs\3\2\2\2\u02cd")
        buf.write(u"\u02ce\7@\2\2\u02ce\u02cf\7\u0091\2\2\u02cf\u02d0\5\u00de")
        buf.write(u"p\2\u02d0\u02d1\7:\2\2\u02d1\u02d2\5\u00d8m\2\u02d2\u02d3")
        buf.write(u"\7\u0092\2\2\u02d3u\3\2\2\2\u02d4\u02d5\7\25\2\2\u02d5")
        buf.write(u"\u02d6\5x=\2\u02d6w\3\2\2\2\u02d7\u02da\5z>\2\u02d8\u02da")
        buf.write(u"\5|?\2\u02d9\u02d7\3\2\2\2\u02d9\u02d8\3\2\2\2\u02da")
        buf.write(u"y\3\2\2\2\u02db\u02dc\5\u00d8m\2\u02dc\u02e0\7\u0093")
        buf.write(u"\2\2\u02dd\u02df\5\u0080A\2\u02de\u02dd\3\2\2\2\u02df")
        buf.write(u"\u02e2\3\2\2\2\u02e0\u02de\3\2\2\2\u02e0\u02e1\3\2\2")
        buf.write(u"\2\u02e1\u02e3\3\2\2\2\u02e2\u02e0\3\2\2\2\u02e3\u02e4")
        buf.write(u"\7\u0094\2\2\u02e4{\3\2\2\2\u02e5\u02e9\7\u0091\2\2\u02e6")
        buf.write(u"\u02e8\5\u00d8m\2\u02e7\u02e6\3\2\2\2\u02e8\u02eb\3\2")
        buf.write(u"\2\2\u02e9\u02e7\3\2\2\2\u02e9\u02ea\3\2\2\2\u02ea\u02ec")
        buf.write(u"\3\2\2\2\u02eb\u02e9\3\2\2\2\u02ec\u02ed\7\u0092\2\2")
        buf.write(u"\u02ed\u02f1\7\u0093\2\2\u02ee\u02f0\5~@\2\u02ef\u02ee")
        buf.write(u"\3\2\2\2\u02f0\u02f3\3\2\2\2\u02f1\u02ef\3\2\2\2\u02f1")
        buf.write(u"\u02f2\3\2\2\2\u02f2\u02f4\3\2\2\2\u02f3\u02f1\3\2\2")
        buf.write(u"\2\u02f4\u02f5\7\u0094\2\2\u02f5}\3\2\2\2\u02f6\u02fa")
        buf.write(u"\7\u0091\2\2\u02f7\u02f9\5\u0080A\2\u02f8\u02f7\3\2\2")
        buf.write(u"\2\u02f9\u02fc\3\2\2\2\u02fa\u02f8\3\2\2\2\u02fa\u02fb")
        buf.write(u"\3\2\2\2\u02fb\u02fd\3\2\2\2\u02fc\u02fa\3\2\2\2\u02fd")
        buf.write(u"\u02fe\7\u0092\2\2\u02fe\177\3\2\2\2\u02ff\u0305\5\u0104")
        buf.write(u"\u0083\2\u0300\u0305\5\u00f6|\2\u0301\u0305\5\u00f8}")
        buf.write(u"\2\u0302\u0305\5\u0100\u0081\2\u0303\u0305\7=\2\2\u0304")
        buf.write(u"\u02ff\3\2\2\2\u0304\u0300\3\2\2\2\u0304\u0301\3\2\2")
        buf.write(u"\2\u0304\u0302\3\2\2\2\u0304\u0303\3\2\2\2\u0305\u0081")
        buf.write(u"\3\2\2\2\u0306\u0307\7A\2\2\u0307\u0308\5d\63\2\u0308")
        buf.write(u"\u0083\3\2\2\2\u0309\u030e\5d\63\2\u030a\u030b\7\30\2")
        buf.write(u"\2\u030b\u030d\5d\63\2\u030c\u030a\3\2\2\2\u030d\u0310")
        buf.write(u"\3\2\2\2\u030e\u030c\3\2\2\2\u030e\u030f\3\2\2\2\u030f")
        buf.write(u"\u0085\3\2\2\2\u0310\u030e\3\2\2\2\u0311\u0312\7\31\2")
        buf.write(u"\2\u0312\u0313\5\u0088E\2\u0313\u0087\3\2\2\2\u0314\u0315")
        buf.write(u"\7\u0091\2\2\u0315\u0316\5\u00dep\2\u0316\u0317\7\u0092")
        buf.write(u"\2\2\u0317\u031b\3\2\2\2\u0318\u031b\5\u00e6t\2\u0319")
        buf.write(u"\u031b\5\u008aF\2\u031a\u0314\3\2\2\2\u031a\u0318\3\2")
        buf.write(u"\2\2\u031a\u0319\3\2\2\2\u031b\u0089\3\2\2\2\u031c\u031d")
        buf.write(u"\5\u0104\u0083\2\u031d\u031e\5\u008cG\2\u031e\u008b\3")
        buf.write(u"\2\2\2\u031f\u0325\7\u0091\2\2\u0320\u0322\7\7\2\2\u0321")
        buf.write(u"\u0320\3\2\2\2\u0321\u0322\3\2\2\2\u0322\u0323\3\2\2")
        buf.write(u"\2\u0323\u0326\5\u008eH\2\u0324\u0326\3\2\2\2\u0325\u0321")
        buf.write(u"\3\2\2\2\u0325\u0324\3\2\2\2\u0326\u0327\3\2\2\2\u0327")
        buf.write(u"\u0328\7\u0092\2\2\u0328\u008d\3\2\2\2\u0329\u032e\5")
        buf.write(u"\u00dep\2\u032a\u032b\7\u009d\2\2\u032b\u032d\5\u00de")
        buf.write(u"p\2\u032c\u032a\3\2\2\2\u032d\u0330\3\2\2\2\u032e\u032c")
        buf.write(u"\3\2\2\2\u032e\u032f\3\2\2\2\u032f\u008f\3\2\2\2\u0330")
        buf.write(u"\u032e\3\2\2\2\u0331\u0333\7\u0093\2\2\u0332\u0334\5")
        buf.write(u"\u0092J\2\u0333\u0332\3\2\2\2\u0333\u0334\3\2\2\2\u0334")
        buf.write(u"\u0335\3\2\2\2\u0335\u0336\7\u0094\2\2\u0336\u0091\3")
        buf.write(u"\2\2\2\u0337\u033e\5\u0094K\2\u0338\u033a\7\u0098\2\2")
        buf.write(u"\u0339\u033b\5\u0092J\2\u033a\u0339\3\2\2\2\u033a\u033b")
        buf.write(u"\3\2\2\2\u033b\u033d\3\2\2\2\u033c\u0338\3\2\2\2\u033d")
        buf.write(u"\u0340\3\2\2\2\u033e\u033c\3\2\2\2\u033e\u033f\3\2\2")
        buf.write(u"\2\u033f\u0093\3\2\2\2\u0340\u033e\3\2\2\2\u0341\u0342")
        buf.write(u"\5\u00d4k\2\u0342\u0343\5\u0098M\2\u0343\u0348\3\2\2")
        buf.write(u"\2\u0344\u0345\5\u00c4c\2\u0345\u0346\5\u0096L\2\u0346")
        buf.write(u"\u0348\3\2\2\2\u0347\u0341\3\2\2\2\u0347\u0344\3\2\2")
        buf.write(u"\2\u0348\u0095\3\2\2\2\u0349\u034b\5\u0098M\2\u034a\u0349")
        buf.write(u"\3\2\2\2\u034a\u034b\3\2\2\2\u034b\u0097\3\2\2\2\u034c")
        buf.write(u"\u034d\5\u009aN\2\u034d\u0356\5\u009cO\2\u034e\u0352")
        buf.write(u"\7\u0097\2\2\u034f\u0350\5\u009aN\2\u0350\u0351\5\u009c")
        buf.write(u"O\2\u0351\u0353\3\2\2\2\u0352\u034f\3\2\2\2\u0352\u0353")
        buf.write(u"\3\2\2\2\u0353\u0355\3\2\2\2\u0354\u034e\3\2\2\2\u0355")
        buf.write(u"\u0358\3\2\2\2\u0356\u0354\3\2\2\2\u0356\u0357\3\2\2")
        buf.write(u"\2\u0357\u0099\3\2\2\2\u0358\u0356\3\2\2\2\u0359\u035c")
        buf.write(u"\5\u00d6l\2\u035a\u035c\7\32\2\2\u035b\u0359\3\2\2\2")
        buf.write(u"\u035b\u035a\3\2\2\2\u035c\u009b\3\2\2\2\u035d\u0362")
        buf.write(u"\5\u009eP\2\u035e\u035f\7\u009d\2\2\u035f\u0361\5\u009e")
        buf.write(u"P\2\u0360\u035e\3\2\2\2\u0361\u0364\3\2\2\2\u0362\u0360")
        buf.write(u"\3\2\2\2\u0362\u0363\3\2\2\2\u0363\u009d\3\2\2\2\u0364")
        buf.write(u"\u0362\3\2\2\2\u0365\u0366\5\u00d0i\2\u0366\u009f\3\2")
        buf.write(u"\2\2\u0367\u0368\5\u00d4k\2\u0368\u0369\5\u00a4S\2\u0369")
        buf.write(u"\u036e\3\2\2\2\u036a\u036b\5\u00c8e\2\u036b\u036c\5\u00a2")
        buf.write(u"R\2\u036c\u036e\3\2\2\2\u036d\u0367\3\2\2\2\u036d\u036a")
        buf.write(u"\3\2\2\2\u036e\u00a1\3\2\2\2\u036f\u0371\5\u00a4S\2\u0370")
        buf.write(u"\u036f\3\2\2\2\u0370\u0371\3\2\2\2\u0371\u00a3\3\2\2")
        buf.write(u"\2\u0372\u0375\5\u00a8U\2\u0373\u0375\5\u00aaV\2\u0374")
        buf.write(u"\u0372\3\2\2\2\u0374\u0373\3\2\2\2\u0375\u0376\3\2\2")
        buf.write(u"\2\u0376\u037d\5\u00acW\2\u0377\u0379\7\u0097\2\2\u0378")
        buf.write(u"\u037a\5\u00a6T\2\u0379\u0378\3\2\2\2\u0379\u037a\3\2")
        buf.write(u"\2\2\u037a\u037c\3\2\2\2\u037b\u0377\3\2\2\2\u037c\u037f")
        buf.write(u"\3\2\2\2\u037d\u037b\3\2\2\2\u037d\u037e\3\2\2\2\u037e")
        buf.write(u"\u00a5\3\2\2\2\u037f\u037d\3\2\2\2\u0380\u0383\5\u00a8")
        buf.write(u"U\2\u0381\u0383\5\u00aaV\2\u0382\u0380\3\2\2\2\u0382")
        buf.write(u"\u0381\3\2\2\2\u0383\u0384\3\2\2\2\u0384\u0385\5\u009c")
        buf.write(u"O\2\u0385\u00a7\3\2\2\2\u0386\u0387\5\u00b0Y\2\u0387")
        buf.write(u"\u00a9\3\2\2\2\u0388\u0389\5\u00d8m\2\u0389\u00ab\3\2")
        buf.write(u"\2\2\u038a\u038f\5\u00aeX\2\u038b\u038c\7\u009d\2\2\u038c")
        buf.write(u"\u038e\5\u00aeX\2\u038d\u038b\3\2\2\2\u038e\u0391\3\2")
        buf.write(u"\2\2\u038f\u038d\3\2\2\2\u038f\u0390\3\2\2\2\u0390\u00ad")
        buf.write(u"\3\2\2\2\u0391\u038f\3\2\2\2\u0392\u0393\5\u00d2j\2\u0393")
        buf.write(u"\u00af\3\2\2\2\u0394\u0395\5\u00b2Z\2\u0395\u00b1\3\2")
        buf.write(u"\2\2\u0396\u039b\5\u00b4[\2\u0397\u0398\7\u00a3\2\2\u0398")
        buf.write(u"\u039a\5\u00b4[\2\u0399\u0397\3\2\2\2\u039a\u039d\3\2")
        buf.write(u"\2\2\u039b\u0399\3\2\2\2\u039b\u039c\3\2\2\2\u039c\u00b3")
        buf.write(u"\3\2\2\2\u039d\u039b\3\2\2\2\u039e\u03a3\5\u00b8]\2\u039f")
        buf.write(u"\u03a0\7\u009f\2\2\u03a0\u03a2\5\u00b8]\2\u03a1\u039f")
        buf.write(u"\3\2\2\2\u03a2\u03a5\3\2\2\2\u03a3\u03a1\3\2\2\2\u03a3")
        buf.write(u"\u03a4\3\2\2\2\u03a4\u00b5\3\2\2\2\u03a5\u03a3\3\2\2")
        buf.write(u"\2\u03a6\u03a8\5\u00bc_\2\u03a7\u03a9\5\u00ba^\2\u03a8")
        buf.write(u"\u03a7\3\2\2\2\u03a8\u03a9\3\2\2\2\u03a9\u00b7\3\2\2")
        buf.write(u"\2\u03aa\u03ac\7\u0090\2\2\u03ab\u03aa\3\2\2\2\u03ab")
        buf.write(u"\u03ac\3\2\2\2\u03ac\u03ad\3\2\2\2\u03ad\u03ae\5\u00b6")
        buf.write(u"\\\2\u03ae\u00b9\3\2\2\2\u03af\u03b0\t\4\2\2\u03b0\u00bb")
        buf.write(u"\3\2\2\2\u03b1\u03ba\5\u0104\u0083\2\u03b2\u03ba\7\32")
        buf.write(u"\2\2\u03b3\u03b4\7\u009e\2\2\u03b4\u03ba\5\u00be`\2\u03b5")
        buf.write(u"\u03b6\7\u0091\2\2\u03b6\u03b7\5\u00b0Y\2\u03b7\u03b8")
        buf.write(u"\7\u0092\2\2\u03b8\u03ba\3\2\2\2\u03b9\u03b1\3\2\2\2")
        buf.write(u"\u03b9\u03b2\3\2\2\2\u03b9\u03b3\3\2\2\2\u03b9\u03b5")
        buf.write(u"\3\2\2\2\u03ba\u00bd\3\2\2\2\u03bb\u03c9\5\u00c0a\2\u03bc")
        buf.write(u"\u03c5\7\u0091\2\2\u03bd\u03c2\5\u00c0a\2\u03be\u03bf")
        buf.write(u"\7\u00a3\2\2\u03bf\u03c1\5\u00c0a\2\u03c0\u03be\3\2\2")
        buf.write(u"\2\u03c1\u03c4\3\2\2\2\u03c2\u03c0\3\2\2\2\u03c2\u03c3")
        buf.write(u"\3\2\2\2\u03c3\u03c6\3\2\2\2\u03c4\u03c2\3\2\2\2\u03c5")
        buf.write(u"\u03bd\3\2\2\2\u03c5\u03c6\3\2\2\2\u03c6\u03c7\3\2\2")
        buf.write(u"\2\u03c7\u03c9\7\u0092\2\2\u03c8\u03bb\3\2\2\2\u03c8")
        buf.write(u"\u03bc\3\2\2\2\u03c9\u00bf\3\2\2\2\u03ca\u03cc\7\u0090")
        buf.write(u"\2\2\u03cb\u03ca\3\2\2\2\u03cb\u03cc\3\2\2\2\u03cc\u03cf")
        buf.write(u"\3\2\2\2\u03cd\u03d0\5\u0104\u0083\2\u03ce\u03d0\7\32")
        buf.write(u"\2\2\u03cf\u03cd\3\2\2\2\u03cf\u03ce\3\2\2\2\u03d0\u00c1")
        buf.write(u"\3\2\2\2\u03d1\u03d2\7|\2\2\u03d2\u00c3\3\2\2\2\u03d3")
        buf.write(u"\u03d6\5\u00ccg\2\u03d4\u03d6\5\u00c6d\2\u03d5\u03d3")
        buf.write(u"\3\2\2\2\u03d5\u03d4\3\2\2\2\u03d6\u00c5\3\2\2\2\u03d7")
        buf.write(u"\u03d8\7\u0095\2\2\u03d8\u03d9\5\u0098M\2\u03d9\u03da")
        buf.write(u"\7\u0096\2\2\u03da\u00c7\3\2\2\2\u03db\u03de\5\u00ce")
        buf.write(u"h\2\u03dc\u03de\5\u00caf\2\u03dd\u03db\3\2\2\2\u03dd")
        buf.write(u"\u03dc\3\2\2\2\u03de\u00c9\3\2\2\2\u03df\u03e0\7\u0095")
        buf.write(u"\2\2\u03e0\u03e1\5\u00a4S\2\u03e1\u03e2\7\u0096\2\2\u03e2")
        buf.write(u"\u00cb\3\2\2\2\u03e3\u03e5\7\u0091\2\2\u03e4\u03e6\5")
        buf.write(u"\u00d0i\2\u03e5\u03e4\3\2\2\2\u03e6\u03e7\3\2\2\2\u03e7")
        buf.write(u"\u03e5\3\2\2\2\u03e7\u03e8\3\2\2\2\u03e8\u03e9\3\2\2")
        buf.write(u"\2\u03e9\u03ea\7\u0092\2\2\u03ea\u00cd\3\2\2\2\u03eb")
        buf.write(u"\u03ed\7\u0091\2\2\u03ec\u03ee\5\u00d2j\2\u03ed\u03ec")
        buf.write(u"\3\2\2\2\u03ee\u03ef\3\2\2\2\u03ef\u03ed\3\2\2\2\u03ef")
        buf.write(u"\u03f0\3\2\2\2\u03f0\u03f1\3\2\2\2\u03f1\u03f2\7\u0092")
        buf.write(u"\2\2\u03f2\u00cf\3\2\2\2\u03f3\u03f6\5\u00d4k\2\u03f4")
        buf.write(u"\u03f6\5\u00c4c\2\u03f5\u03f3\3\2\2\2\u03f5\u03f4\3\2")
        buf.write(u"\2\2\u03f6\u00d1\3\2\2\2\u03f7\u03fa\5\u00d4k\2\u03f8")
        buf.write(u"\u03fa\5\u00c8e\2\u03f9\u03f7\3\2\2\2\u03f9\u03f8\3\2")
        buf.write(u"\2\2\u03fa\u00d3\3\2\2\2\u03fb\u03fe\5\u00d8m\2\u03fc")
        buf.write(u"\u03fe\5\u00dan\2\u03fd\u03fb\3\2\2\2\u03fd\u03fc\3\2")
        buf.write(u"\2\2\u03fe\u00d5\3\2\2\2\u03ff\u0402\5\u00d8m\2\u0400")
        buf.write(u"\u0402\5\u0104\u0083\2\u0401\u03ff\3\2\2\2\u0401\u0400")
        buf.write(u"\3\2\2\2\u0402\u00d7\3\2\2\2\u0403\u0404\t\5\2\2\u0404")
        buf.write(u"\u00d9\3\2\2\2\u0405\u040c\5\u0104\u0083\2\u0406\u040c")
        buf.write(u"\5\u00f6|\2\u0407\u040c\5\u00f8}\2\u0408\u040c\5\u0100")
        buf.write(u"\u0081\2\u0409\u040c\5\u0108\u0085\2\u040a\u040c\5\u00dc")
        buf.write(u"o\2\u040b\u0405\3\2\2\2\u040b\u0406\3\2\2\2\u040b\u0407")
        buf.write(u"\3\2\2\2\u040b\u0408\3\2\2\2\u040b\u0409\3\2\2\2\u040b")
        buf.write(u"\u040a\3\2\2\2\u040c\u00db\3\2\2\2\u040d\u040e\7\u0091")
        buf.write(u"\2\2\u040e\u040f\7\u0092\2\2\u040f\u00dd\3\2\2\2\u0410")
        buf.write(u"\u0411\bp\1\2\u0411\u0412\t\6\2\2\u0412\u0419\5\u00de")
        buf.write(u"p\f\u0413\u0414\t\7\2\2\u0414\u0419\5\u00dep\13\u0415")
        buf.write(u"\u0416\7\u009e\2\2\u0416\u0419\5\u00dep\n\u0417\u0419")
        buf.write(u"\5\u00e4s\2\u0418\u0410\3\2\2\2\u0418\u0413\3\2\2\2\u0418")
        buf.write(u"\u0415\3\2\2\2\u0418\u0417\3\2\2\2\u0419\u0437\3\2\2")
        buf.write(u"\2\u041a\u041b\f\t\2\2\u041b\u041c\t\6\2\2\u041c\u0436")
        buf.write(u"\5\u00dep\n\u041d\u041e\f\b\2\2\u041e\u041f\t\7\2\2\u041f")
        buf.write(u"\u0436\5\u00dep\t\u0420\u0421\f\5\2\2\u0421\u0422\t\b")
        buf.write(u"\2\2\u0422\u0436\5\u00dep\6\u0423\u0424\f\7\2\2\u0424")
        buf.write(u"\u0436\5\u00e0q\2\u0425\u0427\f\6\2\2\u0426\u0428\7q")
        buf.write(u"\2\2\u0427\u0426\3\2\2\2\u0427\u0428\3\2\2\2\u0428\u0429")
        buf.write(u"\3\2\2\2\u0429\u042a\7r\2\2\u042a\u042c\7\u0091\2\2\u042b")
        buf.write(u"\u042d\5\u008eH\2\u042c\u042b\3\2\2\2\u042c\u042d\3\2")
        buf.write(u"\2\2\u042d\u042e\3\2\2\2\u042e\u0436\7\u0092\2\2\u042f")
        buf.write(u"\u0430\f\4\2\2\u0430\u0431\7\u008e\2\2\u0431\u0436\5")
        buf.write(u"\u00dep\2\u0432\u0433\f\3\2\2\u0433\u0434\7\u008f\2\2")
        buf.write(u"\u0434\u0436\5\u00dep\2\u0435\u041a\3\2\2\2\u0435\u041d")
        buf.write(u"\3\2\2\2\u0435\u0420\3\2\2\2\u0435\u0423\3\2\2\2\u0435")
        buf.write(u"\u0425\3\2\2\2\u0435\u042f\3\2\2\2\u0435\u0432\3\2\2")
        buf.write(u"\2\u0436\u0439\3\2\2\2\u0437\u0435\3\2\2\2\u0437\u0438")
        buf.write(u"\3\2\2\2\u0438\u00df\3\2\2\2\u0439\u0437\3\2\2\2\u043a")
        buf.write(u"\u043d\5\u00fc\177\2\u043b\u043d\5\u00fe\u0080\2\u043c")
        buf.write(u"\u043a\3\2\2\2\u043c\u043b\3\2\2\2\u043d\u0440\3\2\2")
        buf.write(u"\2\u043e\u043f\t\6\2\2\u043f\u0441\5\u00e2r\2\u0440\u043e")
        buf.write(u"\3\2\2\2\u0440\u0441\3\2\2\2\u0441\u00e1\3\2\2\2\u0442")
        buf.write(u"\u0444\t\t\2\2\u0443\u0442\3\2\2\2\u0443\u0444\3\2\2")
        buf.write(u"\2\u0444\u0445\3\2\2\2\u0445\u0446\5\u00e4s\2\u0446\u00e3")
        buf.write(u"\3\2\2\2\u0447\u0448\7\u0091\2\2\u0448\u0449\5\u00de")
        buf.write(u"p\2\u0449\u044a\7\u0092\2\2\u044a\u0452\3\2\2\2\u044b")
        buf.write(u"\u0452\5\u00e6t\2\u044c\u0452\5\u00f4{\2\u044d\u0452")
        buf.write(u"\5\u00f6|\2\u044e\u0452\5\u00f8}\2\u044f\u0452\5\u0100")
        buf.write(u"\u0081\2\u0450\u0452\5\u00d8m\2\u0451\u0447\3\2\2\2\u0451")
        buf.write(u"\u044b\3\2\2\2\u0451\u044c\3\2\2\2\u0451\u044d\3\2\2")
        buf.write(u"\2\u0451\u044e\3\2\2\2\u0451\u044f\3\2\2\2\u0451\u0450")
        buf.write(u"\3\2\2\2\u0452\u00e5\3\2\2\2\u0453\u0560\5\u00f2z\2\u0454")
        buf.write(u"\u0455\7\33\2\2\u0455\u0456\7\u0091\2\2\u0456\u0457\5")
        buf.write(u"\u00dep\2\u0457\u0458\7\u0092\2\2\u0458\u0560\3\2\2\2")
        buf.write(u"\u0459\u045a\7\34\2\2\u045a\u045b\7\u0091\2\2\u045b\u045c")
        buf.write(u"\5\u00dep\2\u045c\u045d\7\u0092\2\2\u045d\u0560\3\2\2")
        buf.write(u"\2\u045e\u045f\7\35\2\2\u045f\u0460\7\u0091\2\2\u0460")
        buf.write(u"\u0461\5\u00dep\2\u0461\u0462\7\u009d\2\2\u0462\u0463")
        buf.write(u"\5\u00dep\2\u0463\u0464\7\u0092\2\2\u0464\u0560\3\2\2")
        buf.write(u"\2\u0465\u0466\7\36\2\2\u0466\u0467\7\u0091\2\2\u0467")
        buf.write(u"\u0468\5\u00dep\2\u0468\u0469\7\u0092\2\2\u0469\u0560")
        buf.write(u"\3\2\2\2\u046a\u046b\7\37\2\2\u046b\u046c\7\u0091\2\2")
        buf.write(u"\u046c\u046d\5\u00d8m\2\u046d\u046e\7\u0092\2\2\u046e")
        buf.write(u"\u0560\3\2\2\2\u046f\u0470\7B\2\2\u0470\u0471\7\u0091")
        buf.write(u"\2\2\u0471\u0472\5\u00dep\2\u0472\u0473\7\u0092\2\2\u0473")
        buf.write(u"\u0560\3\2\2\2\u0474\u0475\7C\2\2\u0475\u0476\7\u0091")
        buf.write(u"\2\2\u0476\u0477\5\u00dep\2\u0477\u0478\7\u0092\2\2\u0478")
        buf.write(u"\u0560\3\2\2\2\u0479\u047a\7D\2\2\u047a\u047c\7\u0091")
        buf.write(u"\2\2\u047b\u047d\5\u00dep\2\u047c\u047b\3\2\2\2\u047c")
        buf.write(u"\u047d\3\2\2\2\u047d\u047e\3\2\2\2\u047e\u0560\7\u0092")
        buf.write(u"\2\2\u047f\u0480\7E\2\2\u0480\u0481\7\u0091\2\2\u0481")
        buf.write(u"\u0560\7\u0092\2\2\u0482\u0483\7F\2\2\u0483\u0484\7\u0091")
        buf.write(u"\2\2\u0484\u0485\5\u00dep\2\u0485\u0486\7\u0092\2\2\u0486")
        buf.write(u"\u0560\3\2\2\2\u0487\u0488\7G\2\2\u0488\u0489\7\u0091")
        buf.write(u"\2\2\u0489\u048a\5\u00dep\2\u048a\u048b\7\u0092\2\2\u048b")
        buf.write(u"\u0560\3\2\2\2\u048c\u048d\7H\2\2\u048d\u048e\7\u0091")
        buf.write(u"\2\2\u048e\u048f\5\u00dep\2\u048f\u0490\7\u0092\2\2\u0490")
        buf.write(u"\u0560\3\2\2\2\u0491\u0492\7I\2\2\u0492\u0493\7\u0091")
        buf.write(u"\2\2\u0493\u0494\5\u00dep\2\u0494\u0495\7\u0092\2\2\u0495")
        buf.write(u"\u0560\3\2\2\2\u0496\u0497\7J\2\2\u0497\u0499\7\u0091")
        buf.write(u"\2\2\u0498\u049a\5\u008eH\2\u0499\u0498\3\2\2\2\u0499")
        buf.write(u"\u049a\3\2\2\2\u049a\u049b\3\2\2\2\u049b\u0560\7\u0092")
        buf.write(u"\2\2\u049c\u0560\5\u00eav\2\u049d\u049e\7K\2\2\u049e")
        buf.write(u"\u049f\7\u0091\2\2\u049f\u04a0\5\u00dep\2\u04a0\u04a1")
        buf.write(u"\7\u0092\2\2\u04a1\u0560\3\2\2\2\u04a2\u0560\5\u00ec")
        buf.write(u"w\2\u04a3\u04a4\7L\2\2\u04a4\u04a5\7\u0091\2\2\u04a5")
        buf.write(u"\u04a6\5\u00dep\2\u04a6\u04a7\7\u0092\2\2\u04a7\u0560")
        buf.write(u"\3\2\2\2\u04a8\u04a9\7M\2\2\u04a9\u04aa\7\u0091\2\2\u04aa")
        buf.write(u"\u04ab\5\u00dep\2\u04ab\u04ac\7\u0092\2\2\u04ac\u0560")
        buf.write(u"\3\2\2\2\u04ad\u04ae\7N\2\2\u04ae\u04af\7\u0091\2\2\u04af")
        buf.write(u"\u04b0\5\u00dep\2\u04b0\u04b1\7\u0092\2\2\u04b1\u0560")
        buf.write(u"\3\2\2\2\u04b2\u04b3\7O\2\2\u04b3\u04b4\7\u0091\2\2\u04b4")
        buf.write(u"\u04b5\5\u00dep\2\u04b5\u04b6\7\u009d\2\2\u04b6\u04b7")
        buf.write(u"\5\u00dep\2\u04b7\u04b8\7\u0092\2\2\u04b8\u0560\3\2\2")
        buf.write(u"\2\u04b9\u04ba\7P\2\2\u04ba\u04bb\7\u0091\2\2\u04bb\u04bc")
        buf.write(u"\5\u00dep\2\u04bc\u04bd\7\u009d\2\2\u04bd\u04be\5\u00de")
        buf.write(u"p\2\u04be\u04bf\7\u0092\2\2\u04bf\u0560\3\2\2\2\u04c0")
        buf.write(u"\u04c1\7Q\2\2\u04c1\u04c2\7\u0091\2\2\u04c2\u04c3\5\u00de")
        buf.write(u"p\2\u04c3\u04c4\7\u009d\2\2\u04c4\u04c5\5\u00dep\2\u04c5")
        buf.write(u"\u04c6\7\u0092\2\2\u04c6\u0560\3\2\2\2\u04c7\u04c8\7")
        buf.write(u"R\2\2\u04c8\u04c9\7\u0091\2\2\u04c9\u04ca\5\u00dep\2")
        buf.write(u"\u04ca\u04cb\7\u009d\2\2\u04cb\u04cc\5\u00dep\2\u04cc")
        buf.write(u"\u04cd\7\u0092\2\2\u04cd\u0560\3\2\2\2\u04ce\u04cf\7")
        buf.write(u"S\2\2\u04cf\u04d0\7\u0091\2\2\u04d0\u04d1\5\u00dep\2")
        buf.write(u"\u04d1\u04d2\7\u009d\2\2\u04d2\u04d3\5\u00dep\2\u04d3")
        buf.write(u"\u04d4\7\u0092\2\2\u04d4\u0560\3\2\2\2\u04d5\u04d6\7")
        buf.write(u"U\2\2\u04d6\u04d7\7\u0091\2\2\u04d7\u04d8\5\u00dep\2")
        buf.write(u"\u04d8\u04d9\7\u0092\2\2\u04d9\u0560\3\2\2\2\u04da\u04db")
        buf.write(u"\7V\2\2\u04db\u04dc\7\u0091\2\2\u04dc\u04dd\5\u00dep")
        buf.write(u"\2\u04dd\u04de\7\u0092\2\2\u04de\u0560\3\2\2\2\u04df")
        buf.write(u"\u04e0\7W\2\2\u04e0\u04e1\7\u0091\2\2\u04e1\u04e2\5\u00de")
        buf.write(u"p\2\u04e2\u04e3\7\u0092\2\2\u04e3\u0560\3\2\2\2\u04e4")
        buf.write(u"\u04e5\7X\2\2\u04e5\u04e6\7\u0091\2\2\u04e6\u04e7\5\u00de")
        buf.write(u"p\2\u04e7\u04e8\7\u0092\2\2\u04e8\u0560\3\2\2\2\u04e9")
        buf.write(u"\u04ea\7Y\2\2\u04ea\u04eb\7\u0091\2\2\u04eb\u04ec\5\u00de")
        buf.write(u"p\2\u04ec\u04ed\7\u0092\2\2\u04ed\u0560\3\2\2\2\u04ee")
        buf.write(u"\u04ef\7Z\2\2\u04ef\u04f0\7\u0091\2\2\u04f0\u04f1\5\u00de")
        buf.write(u"p\2\u04f1\u04f2\7\u0092\2\2\u04f2\u0560\3\2\2\2\u04f3")
        buf.write(u"\u04f4\7[\2\2\u04f4\u04f5\7\u0091\2\2\u04f5\u04f6\5\u00de")
        buf.write(u"p\2\u04f6\u04f7\7\u0092\2\2\u04f7\u0560\3\2\2\2\u04f8")
        buf.write(u"\u04f9\7\\\2\2\u04f9\u04fa\7\u0091\2\2\u04fa\u04fb\5")
        buf.write(u"\u00dep\2\u04fb\u04fc\7\u0092\2\2\u04fc\u0560\3\2\2\2")
        buf.write(u"\u04fd\u04fe\7]\2\2\u04fe\u04ff\7\u0091\2\2\u04ff\u0560")
        buf.write(u"\7\u0092\2\2\u0500\u0501\7^\2\2\u0501\u0502\7\u0091\2")
        buf.write(u"\2\u0502\u0560\7\u0092\2\2\u0503\u0504\7_\2\2\u0504\u0505")
        buf.write(u"\7\u0091\2\2\u0505\u0560\7\u0092\2\2\u0506\u0507\7`\2")
        buf.write(u"\2\u0507\u0508\7\u0091\2\2\u0508\u0509\5\u00dep\2\u0509")
        buf.write(u"\u050a\7\u0092\2\2\u050a\u0560\3\2\2\2\u050b\u050c\7")
        buf.write(u"a\2\2\u050c\u050d\7\u0091\2\2\u050d\u050e\5\u00dep\2")
        buf.write(u"\u050e\u050f\7\u0092\2\2\u050f\u0560\3\2\2\2\u0510\u0511")
        buf.write(u"\7b\2\2\u0511\u0512\7\u0091\2\2\u0512\u0513\5\u00dep")
        buf.write(u"\2\u0513\u0514\7\u0092\2\2\u0514\u0560\3\2\2\2\u0515")
        buf.write(u"\u0516\7c\2\2\u0516\u0517\7\u0091\2\2\u0517\u0518\5\u00de")
        buf.write(u"p\2\u0518\u0519\7\u0092\2\2\u0519\u0560\3\2\2\2\u051a")
        buf.write(u"\u051b\7d\2\2\u051b\u051c\7\u0091\2\2\u051c\u051d\5\u00de")
        buf.write(u"p\2\u051d\u051e\7\u0092\2\2\u051e\u0560\3\2\2\2\u051f")
        buf.write(u"\u0520\7e\2\2\u0520\u0522\7\u0091\2\2\u0521\u0523\5\u008e")
        buf.write(u"H\2\u0522\u0521\3\2\2\2\u0522\u0523\3\2\2\2\u0523\u0524")
        buf.write(u"\3\2\2\2\u0524\u0560\7\u0092\2\2\u0525\u0526\7f\2\2\u0526")
        buf.write(u"\u0527\7\u0091\2\2\u0527\u0528\5\u00dep\2\u0528\u0529")
        buf.write(u"\7\u009d\2\2\u0529\u052a\5\u00dep\2\u052a\u052b\7\u009d")
        buf.write(u"\2\2\u052b\u052c\5\u00dep\2\u052c\u052d\7\u0092\2\2\u052d")
        buf.write(u"\u0560\3\2\2\2\u052e\u052f\7g\2\2\u052f\u0530\7\u0091")
        buf.write(u"\2\2\u0530\u0531\5\u00dep\2\u0531\u0532\7\u009d\2\2\u0532")
        buf.write(u"\u0533\5\u00dep\2\u0533\u0534\7\u0092\2\2\u0534\u0560")
        buf.write(u"\3\2\2\2\u0535\u0536\7h\2\2\u0536\u0537\7\u0091\2\2\u0537")
        buf.write(u"\u0538\5\u00dep\2\u0538\u0539\7\u009d\2\2\u0539\u053a")
        buf.write(u"\5\u00dep\2\u053a\u053b\7\u0092\2\2\u053b\u0560\3\2\2")
        buf.write(u"\2\u053c\u053d\7 \2\2\u053d\u053e\7\u0091\2\2\u053e\u053f")
        buf.write(u"\5\u00dep\2\u053f\u0540\7\u009d\2\2\u0540\u0541\5\u00de")
        buf.write(u"p\2\u0541\u0542\7\u0092\2\2\u0542\u0560\3\2\2\2\u0543")
        buf.write(u"\u0544\7!\2\2\u0544\u0545\7\u0091\2\2\u0545\u0546\5\u00de")
        buf.write(u"p\2\u0546\u0547\7\u0092\2\2\u0547\u0560\3\2\2\2\u0548")
        buf.write(u"\u0549\7\"\2\2\u0549\u054a\7\u0091\2\2\u054a\u054b\5")
        buf.write(u"\u00dep\2\u054b\u054c\7\u0092\2\2\u054c\u0560\3\2\2\2")
        buf.write(u"\u054d\u054e\7#\2\2\u054e\u054f\7\u0091\2\2\u054f\u0550")
        buf.write(u"\5\u00dep\2\u0550\u0551\7\u0092\2\2\u0551\u0560\3\2\2")
        buf.write(u"\2\u0552\u0553\7$\2\2\u0553\u0554\7\u0091\2\2\u0554\u0555")
        buf.write(u"\5\u00dep\2\u0555\u0556\7\u0092\2\2\u0556\u0560\3\2\2")
        buf.write(u"\2\u0557\u0558\7i\2\2\u0558\u0559\7\u0091\2\2\u0559\u055a")
        buf.write(u"\5\u00dep\2\u055a\u055b\7\u0092\2\2\u055b\u0560\3\2\2")
        buf.write(u"\2\u055c\u0560\5\u00e8u\2\u055d\u0560\5\u00eex\2\u055e")
        buf.write(u"\u0560\5\u00f0y\2\u055f\u0453\3\2\2\2\u055f\u0454\3\2")
        buf.write(u"\2\2\u055f\u0459\3\2\2\2\u055f\u045e\3\2\2\2\u055f\u0465")
        buf.write(u"\3\2\2\2\u055f\u046a\3\2\2\2\u055f\u046f\3\2\2\2\u055f")
        buf.write(u"\u0474\3\2\2\2\u055f\u0479\3\2\2\2\u055f\u047f\3\2\2")
        buf.write(u"\2\u055f\u0482\3\2\2\2\u055f\u0487\3\2\2\2\u055f\u048c")
        buf.write(u"\3\2\2\2\u055f\u0491\3\2\2\2\u055f\u0496\3\2\2\2\u055f")
        buf.write(u"\u049c\3\2\2\2\u055f\u049d\3\2\2\2\u055f\u04a2\3\2\2")
        buf.write(u"\2\u055f\u04a3\3\2\2\2\u055f\u04a8\3\2\2\2\u055f\u04ad")
        buf.write(u"\3\2\2\2\u055f\u04b2\3\2\2\2\u055f\u04b9\3\2\2\2\u055f")
        buf.write(u"\u04c0\3\2\2\2\u055f\u04c7\3\2\2\2\u055f\u04ce\3\2\2")
        buf.write(u"\2\u055f\u04d5\3\2\2\2\u055f\u04da\3\2\2\2\u055f\u04df")
        buf.write(u"\3\2\2\2\u055f\u04e4\3\2\2\2\u055f\u04e9\3\2\2\2\u055f")
        buf.write(u"\u04ee\3\2\2\2\u055f\u04f3\3\2\2\2\u055f\u04f8\3\2\2")
        buf.write(u"\2\u055f\u04fd\3\2\2\2\u055f\u0500\3\2\2\2\u055f\u0503")
        buf.write(u"\3\2\2\2\u055f\u0506\3\2\2\2\u055f\u050b\3\2\2\2\u055f")
        buf.write(u"\u0510\3\2\2\2\u055f\u0515\3\2\2\2\u055f\u051a\3\2\2")
        buf.write(u"\2\u055f\u051f\3\2\2\2\u055f\u0525\3\2\2\2\u055f\u052e")
        buf.write(u"\3\2\2\2\u055f\u0535\3\2\2\2\u055f\u053c\3\2\2\2\u055f")
        buf.write(u"\u0543\3\2\2\2\u055f\u0548\3\2\2\2\u055f\u054d\3\2\2")
        buf.write(u"\2\u055f\u0552\3\2\2\2\u055f\u0557\3\2\2\2\u055f\u055c")
        buf.write(u"\3\2\2\2\u055f\u055d\3\2\2\2\u055f\u055e\3\2\2\2\u0560")
        buf.write(u"\u00e7\3\2\2\2\u0561\u0562\7%\2\2\u0562\u0563\7\u0091")
        buf.write(u"\2\2\u0563\u0564\5\u00dep\2\u0564\u0565\7\u009d\2\2\u0565")
        buf.write(u"\u0568\5\u00dep\2\u0566\u0567\7\u009d\2\2\u0567\u0569")
        buf.write(u"\5\u00dep\2\u0568\u0566\3\2\2\2\u0568\u0569\3\2\2\2\u0569")
        buf.write(u"\u056a\3\2\2\2\u056a\u056b\7\u0092\2\2\u056b\u00e9\3")
        buf.write(u"\2\2\2\u056c\u056d\7&\2\2\u056d\u056e\7\u0091\2\2\u056e")
        buf.write(u"\u056f\5\u00dep\2\u056f\u0570\7\u009d\2\2\u0570\u0573")
        buf.write(u"\5\u00dep\2\u0571\u0572\7\u009d\2\2\u0572\u0574\5\u00de")
        buf.write(u"p\2\u0573\u0571\3\2\2\2\u0573\u0574\3\2\2\2\u0574\u0575")
        buf.write(u"\3\2\2\2\u0575\u0576\7\u0092\2\2\u0576\u00eb\3\2\2\2")
        buf.write(u"\u0577\u0578\7T\2\2\u0578\u0579\7\u0091\2\2\u0579\u057a")
        buf.write(u"\5\u00dep\2\u057a\u057b\7\u009d\2\2\u057b\u057c\5\u00de")
        buf.write(u"p\2\u057c\u057d\7\u009d\2\2\u057d\u0580\5\u00dep\2\u057e")
        buf.write(u"\u057f\7\u009d\2\2\u057f\u0581\5\u00dep\2\u0580\u057e")
        buf.write(u"\3\2\2\2\u0580\u0581\3\2\2\2\u0581\u0582\3\2\2\2\u0582")
        buf.write(u"\u0583\7\u0092\2\2\u0583\u00ed\3\2\2\2\u0584\u0585\7")
        buf.write(u"s\2\2\u0585\u0586\5d\63\2\u0586\u00ef\3\2\2\2\u0587\u0588")
        buf.write(u"\7q\2\2\u0588\u0589\7s\2\2\u0589\u058a\5d\63\2\u058a")
        buf.write(u"\u00f1\3\2\2\2\u058b\u058c\7j\2\2\u058c\u058e\7\u0091")
        buf.write(u"\2\2\u058d\u058f\7\7\2\2\u058e\u058d\3\2\2\2\u058e\u058f")
        buf.write(u"\3\2\2\2\u058f\u0592\3\2\2\2\u0590\u0593\7\u009b\2\2")
        buf.write(u"\u0591\u0593\5\u00dep\2\u0592\u0590\3\2\2\2\u0592\u0591")
        buf.write(u"\3\2\2\2\u0593\u0594\3\2\2\2\u0594\u05cc\7\u0092\2\2")
        buf.write(u"\u0595\u0596\7k\2\2\u0596\u0598\7\u0091\2\2\u0597\u0599")
        buf.write(u"\7\7\2\2\u0598\u0597\3\2\2\2\u0598\u0599\3\2\2\2\u0599")
        buf.write(u"\u059a\3\2\2\2\u059a\u059b\5\u00dep\2\u059b\u059c\7\u0092")
        buf.write(u"\2\2\u059c\u05cc\3\2\2\2\u059d\u059e\7l\2\2\u059e\u05a0")
        buf.write(u"\7\u0091\2\2\u059f\u05a1\7\7\2\2\u05a0\u059f\3\2\2\2")
        buf.write(u"\u05a0\u05a1\3\2\2\2\u05a1\u05a2\3\2\2\2\u05a2\u05a3")
        buf.write(u"\5\u00dep\2\u05a3\u05a4\7\u0092\2\2\u05a4\u05cc\3\2\2")
        buf.write(u"\2\u05a5\u05a6\7m\2\2\u05a6\u05a8\7\u0091\2\2\u05a7\u05a9")
        buf.write(u"\7\7\2\2\u05a8\u05a7\3\2\2\2\u05a8\u05a9\3\2\2\2\u05a9")
        buf.write(u"\u05aa\3\2\2\2\u05aa\u05ab\5\u00dep\2\u05ab\u05ac\7\u0092")
        buf.write(u"\2\2\u05ac\u05cc\3\2\2\2\u05ad\u05ae\7n\2\2\u05ae\u05b0")
        buf.write(u"\7\u0091\2\2\u05af\u05b1\7\7\2\2\u05b0\u05af\3\2\2\2")
        buf.write(u"\u05b0\u05b1\3\2\2\2\u05b1\u05b2\3\2\2\2\u05b2\u05b3")
        buf.write(u"\5\u00dep\2\u05b3\u05b4\7\u0092\2\2\u05b4\u05cc\3\2\2")
        buf.write(u"\2\u05b5\u05b6\7o\2\2\u05b6\u05b8\7\u0091\2\2\u05b7\u05b9")
        buf.write(u"\7\7\2\2\u05b8\u05b7\3\2\2\2\u05b8\u05b9\3\2\2\2\u05b9")
        buf.write(u"\u05ba\3\2\2\2\u05ba\u05bb\5\u00dep\2\u05bb\u05bc\7\u0092")
        buf.write(u"\2\2\u05bc\u05cc\3\2\2\2\u05bd\u05be\7p\2\2\u05be\u05c0")
        buf.write(u"\7\u0091\2\2\u05bf\u05c1\7\7\2\2\u05c0\u05bf\3\2\2\2")
        buf.write(u"\u05c0\u05c1\3\2\2\2\u05c1\u05c2\3\2\2\2\u05c2\u05c7")
        buf.write(u"\5\u00dep\2\u05c3\u05c4\7\u0097\2\2\u05c4\u05c5\7t\2")
        buf.write(u"\2\u05c5\u05c6\7\u00a0\2\2\u05c6\u05c8\5\u0102\u0082")
        buf.write(u"\2\u05c7\u05c3\3\2\2\2\u05c7\u05c8\3\2\2\2\u05c8\u05c9")
        buf.write(u"\3\2\2\2\u05c9\u05ca\7\u0092\2\2\u05ca\u05cc\3\2\2\2")
        buf.write(u"\u05cb\u058b\3\2\2\2\u05cb\u0595\3\2\2\2\u05cb\u059d")
        buf.write(u"\3\2\2\2\u05cb\u05a5\3\2\2\2\u05cb\u05ad\3\2\2\2\u05cb")
        buf.write(u"\u05b5\3\2\2\2\u05cb\u05bd\3\2\2\2\u05cc\u00f3\3\2\2")
        buf.write(u"\2\u05cd\u05cf\5\u0104\u0083\2\u05ce\u05d0\5\u008cG\2")
        buf.write(u"\u05cf\u05ce\3\2\2\2\u05cf\u05d0\3\2\2\2\u05d0\u00f5")
        buf.write(u"\3\2\2\2\u05d1\u05d5\5\u0102\u0082\2\u05d2\u05d6\7{\2")
        buf.write(u"\2\u05d3\u05d4\7\u008a\2\2\u05d4\u05d6\5\u0104\u0083")
        buf.write(u"\2\u05d5\u05d2\3\2\2\2\u05d5\u05d3\3\2\2\2\u05d5\u05d6")
        buf.write(u"\3\2\2\2\u05d6\u00f7\3\2\2\2\u05d7\u05db\5\u00fa~\2\u05d8")
        buf.write(u"\u05db\5\u00fc\177\2\u05d9\u05db\5\u00fe\u0080\2\u05da")
        buf.write(u"\u05d7\3\2\2\2\u05da\u05d8\3\2\2\2\u05da\u05d9\3\2\2")
        buf.write(u"\2\u05db\u00f9\3\2\2\2\u05dc\u05dd\t\n\2\2\u05dd\u00fb")
        buf.write(u"\3\2\2\2\u05de\u05df\t\13\2\2\u05df\u00fd\3\2\2\2\u05e0")
        buf.write(u"\u05e1\t\f\2\2\u05e1\u00ff\3\2\2\2\u05e2\u05e3\t\r\2")
        buf.write(u"\2\u05e3\u0101\3\2\2\2\u05e4\u05e5\t\16\2\2\u05e5\u0103")
        buf.write(u"\3\2\2\2\u05e6\u05e9\7u\2\2\u05e7\u05e9\5\u0106\u0084")
        buf.write(u"\2\u05e8\u05e6\3\2\2\2\u05e8\u05e7\3\2\2\2\u05e9\u0105")
        buf.write(u"\3\2\2\2\u05ea\u05eb\t\17\2\2\u05eb\u0107\3\2\2\2\u05ec")
        buf.write(u"\u05ef\7x\2\2\u05ed\u05ef\5\u010a\u0086\2\u05ee\u05ec")
        buf.write(u"\3\2\2\2\u05ee\u05ed\3\2\2\2\u05ef\u0109\3\2\2\2\u05f0")
        buf.write(u"\u05f1\7\u0095\2\2\u05f1\u05f2\7\u0096\2\2\u05f2\u010b")
        buf.write(u"\3\2\2\2\u0096\u0111\u0117\u011a\u011e\u0120\u012e\u013b")
        buf.write(u"\u0140\u0143\u014c\u0153\u015c\u0162\u0166\u016c\u016f")
        buf.write(u"\u0174\u0178\u0180\u0188\u018d\u0192\u0195\u0198\u019b")
        buf.write(u"\u01a2\u01aa\u01af\u01b5\u01be\u01c7\u01cb\u01cf\u01d1")
        buf.write(u"\u01db\u01e5\u01ea\u01ec\u01f9\u01fd\u0202\u0206\u020c")
        buf.write(u"\u0212\u0218\u0220\u0228\u023c\u0240\u0243\u0248\u0256")
        buf.write(u"\u025c\u025f\u0268\u0273\u0278\u027d\u0280\u0286\u028d")
        buf.write(u"\u0291\u0297\u029c\u02a1\u02a6\u02a9\u02ae\u02b2\u02bd")
        buf.write(u"\u02c8\u02d9\u02e0\u02e9\u02f1\u02fa\u0304\u030e\u031a")
        buf.write(u"\u0321\u0325\u032e\u0333\u033a\u033e\u0347\u034a\u0352")
        buf.write(u"\u0356\u035b\u0362\u036d\u0370\u0374\u0379\u037d\u0382")
        buf.write(u"\u038f\u039b\u03a3\u03a8\u03ab\u03b9\u03c2\u03c5\u03c8")
        buf.write(u"\u03cb\u03cf\u03d5\u03dd\u03e7\u03ef\u03f5\u03f9\u03fd")
        buf.write(u"\u0401\u040b\u0418\u0427\u042c\u0435\u0437\u043c\u0440")
        buf.write(u"\u0443\u0451\u047c\u0499\u0522\u055f\u0568\u0573\u0580")
        buf.write(u"\u058e\u0592\u0598\u05a0\u05a8\u05b0\u05b8\u05c0\u05c7")
        buf.write(u"\u05cb\u05cf\u05d5\u05da\u05e8\u05ee")
        return buf.getvalue()


class SparqlParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'a'", u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'^^'", 
                     u"'<='", u"'>='", u"'!='", u"'&&'", u"'||'", u"'^'", 
                     u"'('", u"')'", u"'{'", u"'}'", u"'['", u"']'", u"';'", 
                     u"'.'", u"'+'", u"'-'", u"'*'", u"'?'", u"','", u"'!'", 
                     u"'/'", u"'='", u"'<'", u"'>'", u"'|'" ]

    symbolicNames = [ u"<INVALID>", u"WS", u"BASE", u"PREFIX", u"SELECT", 
                      u"DISTINCT", u"REDUCED", u"CONSTRUCT", u"DESCRIBE", 
                      u"ASK", u"FROM", u"NAMED", u"WHERE", u"ORDER", u"BY", 
                      u"ASC", u"DESC", u"LIMIT", u"OFFSET", u"VALUES", u"OPTIONAL", 
                      u"GRAPH", u"UNION", u"FILTER", u"A", u"STR", u"LANG", 
                      u"LANGMATCHES", u"DATATYPE", u"BOUND", u"SAMETERM", 
                      u"ISIRI", u"ISURI", u"ISBLANK", u"ISLITERAL", u"REGEX", 
                      u"SUBSTR", u"TRUE", u"FALSE", u"LOAD", u"CLEAR", u"DROP", 
                      u"ADD", u"MOVE", u"COPY", u"CREATE", u"DELETE", u"INSERT", 
                      u"USING", u"SILENT", u"DEFAULT", u"ALL", u"DATA", 
                      u"WITH", u"INTO", u"TO", u"AS", u"GROUP", u"HAVING", 
                      u"UNDEF", u"BINDINGS", u"SERVICE", u"BIND", u"MINUS", 
                      u"IRI", u"URI", u"BNODE", u"RAND", u"ABS", u"CEIL", 
                      u"FLOOR", u"ROUND", u"CONCAT", u"STRLEN", u"UCASE", 
                      u"LCASE", u"ENCODE_FOR_URI", u"CONTAINS", u"STRSTARTS", 
                      u"STRENDS", u"STRBEFORE", u"STRAFTER", u"REPLACE", 
                      u"YEAR", u"MONTH", u"DAY", u"HOURS", u"MINUTES", u"SECONDS", 
                      u"TIMEZONE", u"TZ", u"NOW", u"UUID", u"STRUUID", u"MD5", 
                      u"SHA1", u"SHA256", u"SHA384", u"SHA512", u"COALESCE", 
                      u"IF", u"STRLANG", u"STRDT", u"ISNUMERIC", u"COUNT", 
                      u"SUM", u"MIN", u"MAX", u"AVG", u"SAMPLE", u"GROUP_CONCAT", 
                      u"NOT", u"IN", u"EXISTS", u"SEPARATOR", u"IRIREF", 
                      u"PNAME_NS", u"PNAME_LN", u"BLANK_NODE_LABEL", u"VAR1", 
                      u"VAR2", u"LANGTAG", u"INTEGER", u"DECIMAL", u"DOUBLE", 
                      u"INTEGER_POSITIVE", u"DECIMAL_POSITIVE", u"DOUBLE_POSITIVE", 
                      u"INTEGER_NEGATIVE", u"DECIMAL_NEGATIVE", u"DOUBLE_NEGATIVE", 
                      u"STRING_LITERAL1", u"STRING_LITERAL2", u"STRING_LITERAL_LONG1", 
                      u"STRING_LITERAL_LONG2", u"COMMENT", u"REFERENCE", 
                      u"LESS_EQUAL", u"GREATER_EQUAL", u"NOT_EQUAL", u"AND", 
                      u"OR", u"INVERSE", u"OPEN_BRACE", u"CLOSE_BRACE", 
                      u"OPEN_CURLY_BRACE", u"CLOSE_CURLY_BRACE", u"OPEN_SQUARE_BRACKET", 
                      u"CLOSE_SQUARE_BRACKET", u"SEMICOLON", u"DOT", u"PLUS_SIGN", 
                      u"MINUS_SIGN", u"ASTERISK", u"QUESTION_MARK", u"COMMA", 
                      u"NEGATION", u"DIVIDE", u"EQUAL", u"LESS", u"GREATER", 
                      u"PIPE", u"ANY" ]

    RULE_query = 0
    RULE_prologue = 1
    RULE_baseDecl = 2
    RULE_prefixDecl = 3
    RULE_selectQuery = 4
    RULE_subSelect = 5
    RULE_selectClause = 6
    RULE_selectVariables = 7
    RULE_constructQuery = 8
    RULE_describeQuery = 9
    RULE_askQuery = 10
    RULE_datasetClause = 11
    RULE_whereClause = 12
    RULE_solutionModifier = 13
    RULE_groupClause = 14
    RULE_groupCondition = 15
    RULE_havingClause = 16
    RULE_havingCondition = 17
    RULE_orderClause = 18
    RULE_orderCondition = 19
    RULE_limitOffsetClauses = 20
    RULE_limitClause = 21
    RULE_offsetClause = 22
    RULE_valuesClause = 23
    RULE_updateCommand = 24
    RULE_update = 25
    RULE_load = 26
    RULE_clear = 27
    RULE_drop = 28
    RULE_create = 29
    RULE_add = 30
    RULE_move = 31
    RULE_copy = 32
    RULE_insertData = 33
    RULE_deleteData = 34
    RULE_deleteWhere = 35
    RULE_modify = 36
    RULE_deleteClause = 37
    RULE_insertClause = 38
    RULE_usingClause = 39
    RULE_graphOrDefault = 40
    RULE_graphRef = 41
    RULE_graphRefAll = 42
    RULE_quadPattern = 43
    RULE_quadData = 44
    RULE_quads = 45
    RULE_quadsDetails = 46
    RULE_quadsNotTriples = 47
    RULE_triplesTemplate = 48
    RULE_groupGraphPattern = 49
    RULE_groupGraphPatternSub = 50
    RULE_groupGraphPatternSubList = 51
    RULE_triplesBlock = 52
    RULE_graphPatternNotTriples = 53
    RULE_optionalGraphPattern = 54
    RULE_graphGraphPattern = 55
    RULE_serviceGraphPattern = 56
    RULE_bind = 57
    RULE_inlineData = 58
    RULE_dataBlock = 59
    RULE_inlineDataOneVar = 60
    RULE_inlineDataFull = 61
    RULE_dataBlockValues = 62
    RULE_dataBlockValue = 63
    RULE_minusGraphPattern = 64
    RULE_groupOrUnionGraphPattern = 65
    RULE_xfilter = 66
    RULE_constraint = 67
    RULE_functionCall = 68
    RULE_argList = 69
    RULE_expressionList = 70
    RULE_constructTemplate = 71
    RULE_constructTriples = 72
    RULE_triplesSameSubject = 73
    RULE_propertyList = 74
    RULE_propertyListNotEmpty = 75
    RULE_verb = 76
    RULE_objectList = 77
    RULE_yobject = 78
    RULE_triplesSameSubjectPath = 79
    RULE_propertyListPath = 80
    RULE_propertyListPathNotEmpty = 81
    RULE_propertyListPathNotEmptyList = 82
    RULE_verbPath = 83
    RULE_verbSimple = 84
    RULE_objectListPath = 85
    RULE_objectPath = 86
    RULE_path = 87
    RULE_pathAlternative = 88
    RULE_pathSequence = 89
    RULE_pathElt = 90
    RULE_pathEltOrInverse = 91
    RULE_pathMod = 92
    RULE_pathPrimary = 93
    RULE_pathNegatedPropertySet = 94
    RULE_pathOneInPropertySet = 95
    RULE_integer = 96
    RULE_triplesNode = 97
    RULE_blankNodePropertyList = 98
    RULE_triplesNodePath = 99
    RULE_blankNodePropertyListPath = 100
    RULE_collection = 101
    RULE_collectionPath = 102
    RULE_graphNode = 103
    RULE_graphNodePath = 104
    RULE_varOrTerm = 105
    RULE_varOrIRI = 106
    RULE_var = 107
    RULE_graphTerm = 108
    RULE_nil = 109
    RULE_expression = 110
    RULE_unaryLiteralExpression = 111
    RULE_unaryExpression = 112
    RULE_primaryExpression = 113
    RULE_builtInCall = 114
    RULE_regexExpression = 115
    RULE_subStringExpression = 116
    RULE_strReplaceExpression = 117
    RULE_existsFunction = 118
    RULE_notExistsFunction = 119
    RULE_aggregate = 120
    RULE_iriRefOrFunction = 121
    RULE_rdfLiteral = 122
    RULE_numericLiteral = 123
    RULE_numericLiteralUnsigned = 124
    RULE_numericLiteralPositive = 125
    RULE_numericLiteralNegative = 126
    RULE_booleanLiteral = 127
    RULE_string = 128
    RULE_iri = 129
    RULE_prefixedName = 130
    RULE_blankNode = 131
    RULE_anon = 132

    ruleNames =  [ u"query", u"prologue", u"baseDecl", u"prefixDecl", u"selectQuery", 
                   u"subSelect", u"selectClause", u"selectVariables", u"constructQuery", 
                   u"describeQuery", u"askQuery", u"datasetClause", u"whereClause", 
                   u"solutionModifier", u"groupClause", u"groupCondition", 
                   u"havingClause", u"havingCondition", u"orderClause", 
                   u"orderCondition", u"limitOffsetClauses", u"limitClause", 
                   u"offsetClause", u"valuesClause", u"updateCommand", u"update", 
                   u"load", u"clear", u"drop", u"create", u"add", u"move", 
                   u"copy", u"insertData", u"deleteData", u"deleteWhere", 
                   u"modify", u"deleteClause", u"insertClause", u"usingClause", 
                   u"graphOrDefault", u"graphRef", u"graphRefAll", u"quadPattern", 
                   u"quadData", u"quads", u"quadsDetails", u"quadsNotTriples", 
                   u"triplesTemplate", u"groupGraphPattern", u"groupGraphPatternSub", 
                   u"groupGraphPatternSubList", u"triplesBlock", u"graphPatternNotTriples", 
                   u"optionalGraphPattern", u"graphGraphPattern", u"serviceGraphPattern", 
                   u"bind", u"inlineData", u"dataBlock", u"inlineDataOneVar", 
                   u"inlineDataFull", u"dataBlockValues", u"dataBlockValue", 
                   u"minusGraphPattern", u"groupOrUnionGraphPattern", u"xfilter", 
                   u"constraint", u"functionCall", u"argList", u"expressionList", 
                   u"constructTemplate", u"constructTriples", u"triplesSameSubject", 
                   u"propertyList", u"propertyListNotEmpty", u"verb", u"objectList", 
                   u"yobject", u"triplesSameSubjectPath", u"propertyListPath", 
                   u"propertyListPathNotEmpty", u"propertyListPathNotEmptyList", 
                   u"verbPath", u"verbSimple", u"objectListPath", u"objectPath", 
                   u"path", u"pathAlternative", u"pathSequence", u"pathElt", 
                   u"pathEltOrInverse", u"pathMod", u"pathPrimary", u"pathNegatedPropertySet", 
                   u"pathOneInPropertySet", u"integer", u"triplesNode", 
                   u"blankNodePropertyList", u"triplesNodePath", u"blankNodePropertyListPath", 
                   u"collection", u"collectionPath", u"graphNode", u"graphNodePath", 
                   u"varOrTerm", u"varOrIRI", u"var", u"graphTerm", u"nil", 
                   u"expression", u"unaryLiteralExpression", u"unaryExpression", 
                   u"primaryExpression", u"builtInCall", u"regexExpression", 
                   u"subStringExpression", u"strReplaceExpression", u"existsFunction", 
                   u"notExistsFunction", u"aggregate", u"iriRefOrFunction", 
                   u"rdfLiteral", u"numericLiteral", u"numericLiteralUnsigned", 
                   u"numericLiteralPositive", u"numericLiteralNegative", 
                   u"booleanLiteral", u"string", u"iri", u"prefixedName", 
                   u"blankNode", u"anon" ]

    EOF = Token.EOF
    WS=1
    BASE=2
    PREFIX=3
    SELECT=4
    DISTINCT=5
    REDUCED=6
    CONSTRUCT=7
    DESCRIBE=8
    ASK=9
    FROM=10
    NAMED=11
    WHERE=12
    ORDER=13
    BY=14
    ASC=15
    DESC=16
    LIMIT=17
    OFFSET=18
    VALUES=19
    OPTIONAL=20
    GRAPH=21
    UNION=22
    FILTER=23
    A=24
    STR=25
    LANG=26
    LANGMATCHES=27
    DATATYPE=28
    BOUND=29
    SAMETERM=30
    ISIRI=31
    ISURI=32
    ISBLANK=33
    ISLITERAL=34
    REGEX=35
    SUBSTR=36
    TRUE=37
    FALSE=38
    LOAD=39
    CLEAR=40
    DROP=41
    ADD=42
    MOVE=43
    COPY=44
    CREATE=45
    DELETE=46
    INSERT=47
    USING=48
    SILENT=49
    DEFAULT=50
    ALL=51
    DATA=52
    WITH=53
    INTO=54
    TO=55
    AS=56
    GROUP=57
    HAVING=58
    UNDEF=59
    BINDINGS=60
    SERVICE=61
    BIND=62
    MINUS=63
    IRI=64
    URI=65
    BNODE=66
    RAND=67
    ABS=68
    CEIL=69
    FLOOR=70
    ROUND=71
    CONCAT=72
    STRLEN=73
    UCASE=74
    LCASE=75
    ENCODE_FOR_URI=76
    CONTAINS=77
    STRSTARTS=78
    STRENDS=79
    STRBEFORE=80
    STRAFTER=81
    REPLACE=82
    YEAR=83
    MONTH=84
    DAY=85
    HOURS=86
    MINUTES=87
    SECONDS=88
    TIMEZONE=89
    TZ=90
    NOW=91
    UUID=92
    STRUUID=93
    MD5=94
    SHA1=95
    SHA256=96
    SHA384=97
    SHA512=98
    COALESCE=99
    IF=100
    STRLANG=101
    STRDT=102
    ISNUMERIC=103
    COUNT=104
    SUM=105
    MIN=106
    MAX=107
    AVG=108
    SAMPLE=109
    GROUP_CONCAT=110
    NOT=111
    IN=112
    EXISTS=113
    SEPARATOR=114
    IRIREF=115
    PNAME_NS=116
    PNAME_LN=117
    BLANK_NODE_LABEL=118
    VAR1=119
    VAR2=120
    LANGTAG=121
    INTEGER=122
    DECIMAL=123
    DOUBLE=124
    INTEGER_POSITIVE=125
    DECIMAL_POSITIVE=126
    DOUBLE_POSITIVE=127
    INTEGER_NEGATIVE=128
    DECIMAL_NEGATIVE=129
    DOUBLE_NEGATIVE=130
    STRING_LITERAL1=131
    STRING_LITERAL2=132
    STRING_LITERAL_LONG1=133
    STRING_LITERAL_LONG2=134
    COMMENT=135
    REFERENCE=136
    LESS_EQUAL=137
    GREATER_EQUAL=138
    NOT_EQUAL=139
    AND=140
    OR=141
    INVERSE=142
    OPEN_BRACE=143
    CLOSE_BRACE=144
    OPEN_CURLY_BRACE=145
    CLOSE_CURLY_BRACE=146
    OPEN_SQUARE_BRACKET=147
    CLOSE_SQUARE_BRACKET=148
    SEMICOLON=149
    DOT=150
    PLUS_SIGN=151
    MINUS_SIGN=152
    ASTERISK=153
    QUESTION_MARK=154
    COMMA=155
    NEGATION=156
    DIVIDE=157
    EQUAL=158
    LESS=159
    GREATER=160
    PIPE=161
    ANY=162

    def __init__(self, input):
        super(SparqlParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class QueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.QueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def prologue(self):
            return self.getTypedRuleContext(SparqlParser.PrologueContext,0)


        def valuesClause(self):
            return self.getTypedRuleContext(SparqlParser.ValuesClauseContext,0)


        def EOF(self):
            return self.getToken(SparqlParser.EOF, 0)

        def selectQuery(self):
            return self.getTypedRuleContext(SparqlParser.SelectQueryContext,0)


        def constructQuery(self):
            return self.getTypedRuleContext(SparqlParser.ConstructQueryContext,0)


        def describeQuery(self):
            return self.getTypedRuleContext(SparqlParser.DescribeQueryContext,0)


        def askQuery(self):
            return self.getTypedRuleContext(SparqlParser.AskQueryContext,0)


        def updateCommand(self):
            return self.getTypedRuleContext(SparqlParser.UpdateCommandContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_query

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterQuery(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitQuery(self)




    def query(self):

        localctx = SparqlParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.state = 280
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.prologue()
                self.state = 271
                token = self._input.LA(1)
                if token in [SparqlParser.SELECT]:
                    self.state = 267
                    self.selectQuery()
                    pass
                elif token in [SparqlParser.CONSTRUCT]:
                    self.state = 268
                    self.constructQuery()
                    pass
                elif token in [SparqlParser.DESCRIBE]:
                    self.state = 269
                    self.describeQuery()
                    pass
                elif token in [SparqlParser.ASK]:
                    self.state = 270
                    self.askQuery()
                    pass
                elif token in [SparqlParser.EOF, SparqlParser.VALUES]:
                    pass
                else:
                    raise NoViableAltException(self)
                self.state = 273
                self.valuesClause()
                self.state = 274
                self.match(SparqlParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 276
                    self.updateCommand()


                self.state = 279
                self.match(SparqlParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrologueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PrologueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def baseDecl(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.BaseDeclContext)
            else:
                return self.getTypedRuleContext(SparqlParser.BaseDeclContext,i)


        def prefixDecl(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.PrefixDeclContext)
            else:
                return self.getTypedRuleContext(SparqlParser.PrefixDeclContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_prologue

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPrologue(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPrologue(self)




    def prologue(self):

        localctx = SparqlParser.PrologueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prologue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.BASE or _la==SparqlParser.PREFIX:
                self.state = 284
                token = self._input.LA(1)
                if token in [SparqlParser.BASE]:
                    self.state = 282
                    self.baseDecl()

                elif token in [SparqlParser.PREFIX]:
                    self.state = 283
                    self.prefixDecl()

                else:
                    raise NoViableAltException(self)

                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BaseDeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.BaseDeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BASE(self):
            return self.getToken(SparqlParser.BASE, 0)

        def IRIREF(self):
            return self.getToken(SparqlParser.IRIREF, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_baseDecl

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterBaseDecl(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitBaseDecl(self)




    def baseDecl(self):

        localctx = SparqlParser.BaseDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_baseDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(SparqlParser.BASE)
            self.state = 290
            self.match(SparqlParser.IRIREF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrefixDeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PrefixDeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(SparqlParser.PREFIX, 0)

        def PNAME_NS(self):
            return self.getToken(SparqlParser.PNAME_NS, 0)

        def IRIREF(self):
            return self.getToken(SparqlParser.IRIREF, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_prefixDecl

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPrefixDecl(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPrefixDecl(self)




    def prefixDecl(self):

        localctx = SparqlParser.PrefixDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_prefixDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(SparqlParser.PREFIX)
            self.state = 293
            self.match(SparqlParser.PNAME_NS)
            self.state = 294
            self.match(SparqlParser.IRIREF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SelectQueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.SelectQueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def selectClause(self):
            return self.getTypedRuleContext(SparqlParser.SelectClauseContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(SparqlParser.WhereClauseContext,0)


        def solutionModifier(self):
            return self.getTypedRuleContext(SparqlParser.SolutionModifierContext,0)


        def datasetClause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.DatasetClauseContext)
            else:
                return self.getTypedRuleContext(SparqlParser.DatasetClauseContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_selectQuery

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterSelectQuery(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitSelectQuery(self)




    def selectQuery(self):

        localctx = SparqlParser.SelectQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_selectQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.selectClause()
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.FROM:
                self.state = 297
                self.datasetClause()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 303
            self.whereClause()
            self.state = 304
            self.solutionModifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubSelectContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.SubSelectContext, self).__init__(parent, invokingState)
            self.parser = parser

        def selectClause(self):
            return self.getTypedRuleContext(SparqlParser.SelectClauseContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(SparqlParser.WhereClauseContext,0)


        def solutionModifier(self):
            return self.getTypedRuleContext(SparqlParser.SolutionModifierContext,0)


        def valuesClause(self):
            return self.getTypedRuleContext(SparqlParser.ValuesClauseContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_subSelect

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterSubSelect(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitSubSelect(self)




    def subSelect(self):

        localctx = SparqlParser.SubSelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_subSelect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.selectClause()
            self.state = 307
            self.whereClause()
            self.state = 308
            self.solutionModifier()
            self.state = 309
            self.valuesClause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SelectClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.SelectClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SparqlParser.SELECT, 0)

        def DISTINCT(self):
            return self.getToken(SparqlParser.DISTINCT, 0)

        def REDUCED(self):
            return self.getToken(SparqlParser.REDUCED, 0)

        def selectVariables(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.SelectVariablesContext)
            else:
                return self.getTypedRuleContext(SparqlParser.SelectVariablesContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_selectClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterSelectClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitSelectClause(self)




    def selectClause(self):

        localctx = SparqlParser.SelectClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_selectClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(SparqlParser.SELECT)
            self.state = 313
            _la = self._input.LA(1)
            if _la==SparqlParser.DISTINCT or _la==SparqlParser.REDUCED:
                self.state = 312
                _la = self._input.LA(1)
                if not(_la==SparqlParser.DISTINCT or _la==SparqlParser.REDUCED):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()


            self.state = 321
            token = self._input.LA(1)
            if token in [SparqlParser.VAR1, SparqlParser.VAR2, SparqlParser.OPEN_BRACE]:
                self.state = 316 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 315
                    self.selectVariables()
                    self.state = 318 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((((_la - 119)) & ~0x3f) == 0 and ((1 << (_la - 119)) & ((1 << (SparqlParser.VAR1 - 119)) | (1 << (SparqlParser.VAR2 - 119)) | (1 << (SparqlParser.OPEN_BRACE - 119)))) != 0)):
                        break


            elif token in [SparqlParser.ASTERISK]:
                self.state = 320
                self.match(SparqlParser.ASTERISK)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SelectVariablesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.SelectVariablesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def AS(self):
            return self.getToken(SparqlParser.AS, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_selectVariables

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterSelectVariables(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitSelectVariables(self)




    def selectVariables(self):

        localctx = SparqlParser.SelectVariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_selectVariables)
        try:
            self.state = 330
            token = self._input.LA(1)
            if token in [SparqlParser.VAR1, SparqlParser.VAR2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.var()

            elif token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 325
                self.expression(0)
                self.state = 326
                self.match(SparqlParser.AS)
                self.state = 327
                self.var()
                self.state = 328
                self.match(SparqlParser.CLOSE_BRACE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstructQueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ConstructQueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCT(self):
            return self.getToken(SparqlParser.CONSTRUCT, 0)

        def constructTemplate(self):
            return self.getTypedRuleContext(SparqlParser.ConstructTemplateContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(SparqlParser.WhereClauseContext,0)


        def solutionModifier(self):
            return self.getTypedRuleContext(SparqlParser.SolutionModifierContext,0)


        def WHERE(self):
            return self.getToken(SparqlParser.WHERE, 0)

        def datasetClause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.DatasetClauseContext)
            else:
                return self.getTypedRuleContext(SparqlParser.DatasetClauseContext,i)


        def triplesTemplate(self):
            return self.getTypedRuleContext(SparqlParser.TriplesTemplateContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_constructQuery

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterConstructQuery(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitConstructQuery(self)




    def constructQuery(self):

        localctx = SparqlParser.ConstructQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(SparqlParser.CONSTRUCT)
            self.state = 356
            token = self._input.LA(1)
            if token in [SparqlParser.OPEN_CURLY_BRACE]:
                self.state = 333
                self.constructTemplate()
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SparqlParser.FROM:
                    self.state = 334
                    self.datasetClause()
                    self.state = 339
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 340
                self.whereClause()
                self.state = 341
                self.solutionModifier()

            elif token in [SparqlParser.FROM, SparqlParser.WHERE]:
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SparqlParser.FROM:
                    self.state = 343
                    self.datasetClause()
                    self.state = 348
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 349
                self.match(SparqlParser.WHERE)
                self.state = 350
                self.match(SparqlParser.OPEN_CURLY_BRACE)
                self.state = 352
                _la = self._input.LA(1)
                if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                    self.state = 351
                    self.triplesTemplate()


                self.state = 354
                self.match(SparqlParser.CLOSE_CURLY_BRACE)
                self.state = 355
                self.solutionModifier()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DescribeQueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.DescribeQueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DESCRIBE(self):
            return self.getToken(SparqlParser.DESCRIBE, 0)

        def solutionModifier(self):
            return self.getTypedRuleContext(SparqlParser.SolutionModifierContext,0)


        def datasetClause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.DatasetClauseContext)
            else:
                return self.getTypedRuleContext(SparqlParser.DatasetClauseContext,i)


        def whereClause(self):
            return self.getTypedRuleContext(SparqlParser.WhereClauseContext,0)


        def varOrIRI(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.VarOrIRIContext)
            else:
                return self.getTypedRuleContext(SparqlParser.VarOrIRIContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_describeQuery

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterDescribeQuery(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitDescribeQuery(self)




    def describeQuery(self):

        localctx = SparqlParser.DescribeQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_describeQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(SparqlParser.DESCRIBE)
            self.state = 365
            token = self._input.LA(1)
            if token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.VAR1, SparqlParser.VAR2]:
                self.state = 360 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 359
                    self.varOrIRI()
                    self.state = 362 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)))) != 0)):
                        break


            elif token in [SparqlParser.ASTERISK]:
                self.state = 364
                self.match(SparqlParser.ASTERISK)

            else:
                raise NoViableAltException(self)

            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.FROM:
                self.state = 367
                self.datasetClause()
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 374
            _la = self._input.LA(1)
            if _la==SparqlParser.WHERE or _la==SparqlParser.OPEN_CURLY_BRACE:
                self.state = 373
                self.whereClause()


            self.state = 376
            self.solutionModifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AskQueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.AskQueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ASK(self):
            return self.getToken(SparqlParser.ASK, 0)

        def whereClause(self):
            return self.getTypedRuleContext(SparqlParser.WhereClauseContext,0)


        def solutionModifier(self):
            return self.getTypedRuleContext(SparqlParser.SolutionModifierContext,0)


        def datasetClause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.DatasetClauseContext)
            else:
                return self.getTypedRuleContext(SparqlParser.DatasetClauseContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_askQuery

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterAskQuery(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitAskQuery(self)




    def askQuery(self):

        localctx = SparqlParser.AskQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_askQuery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(SparqlParser.ASK)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.FROM:
                self.state = 379
                self.datasetClause()
                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 385
            self.whereClause()
            self.state = 386
            self.solutionModifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DatasetClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.DatasetClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(SparqlParser.FROM, 0)

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def NAMED(self):
            return self.getToken(SparqlParser.NAMED, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_datasetClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterDatasetClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitDatasetClause(self)




    def datasetClause(self):

        localctx = SparqlParser.DatasetClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_datasetClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(SparqlParser.FROM)
            self.state = 390
            _la = self._input.LA(1)
            if _la==SparqlParser.NAMED:
                self.state = 389
                self.match(SparqlParser.NAMED)


            self.state = 392
            self.iri()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhereClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.WhereClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def groupGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GroupGraphPatternContext,0)


        def WHERE(self):
            return self.getToken(SparqlParser.WHERE, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_whereClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterWhereClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitWhereClause(self)




    def whereClause(self):

        localctx = SparqlParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whereClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            _la = self._input.LA(1)
            if _la==SparqlParser.WHERE:
                self.state = 394
                self.match(SparqlParser.WHERE)


            self.state = 397
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SolutionModifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.SolutionModifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def groupClause(self):
            return self.getTypedRuleContext(SparqlParser.GroupClauseContext,0)


        def havingClause(self):
            return self.getTypedRuleContext(SparqlParser.HavingClauseContext,0)


        def orderClause(self):
            return self.getTypedRuleContext(SparqlParser.OrderClauseContext,0)


        def limitOffsetClauses(self):
            return self.getTypedRuleContext(SparqlParser.LimitOffsetClausesContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_solutionModifier

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterSolutionModifier(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitSolutionModifier(self)




    def solutionModifier(self):

        localctx = SparqlParser.SolutionModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_solutionModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            _la = self._input.LA(1)
            if _la==SparqlParser.GROUP:
                self.state = 399
                self.groupClause()


            self.state = 403
            _la = self._input.LA(1)
            if _la==SparqlParser.HAVING:
                self.state = 402
                self.havingClause()


            self.state = 406
            _la = self._input.LA(1)
            if _la==SparqlParser.ORDER:
                self.state = 405
                self.orderClause()


            self.state = 409
            _la = self._input.LA(1)
            if _la==SparqlParser.LIMIT or _la==SparqlParser.OFFSET:
                self.state = 408
                self.limitOffsetClauses()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GroupClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(SparqlParser.GROUP, 0)

        def BY(self):
            return self.getToken(SparqlParser.BY, 0)

        def groupCondition(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.GroupConditionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.GroupConditionContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_groupClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGroupClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGroupClause(self)




    def groupClause(self):

        localctx = SparqlParser.GroupClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_groupClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(SparqlParser.GROUP)
            self.state = 412
            self.match(SparqlParser.BY)
            self.state = 414 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 413
                self.groupCondition()
                self.state = 416 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 25)) & ~0x3f) == 0 and ((1 << (_la - 25)) & ((1 << (SparqlParser.STR - 25)) | (1 << (SparqlParser.LANG - 25)) | (1 << (SparqlParser.LANGMATCHES - 25)) | (1 << (SparqlParser.DATATYPE - 25)) | (1 << (SparqlParser.BOUND - 25)) | (1 << (SparqlParser.SAMETERM - 25)) | (1 << (SparqlParser.ISIRI - 25)) | (1 << (SparqlParser.ISURI - 25)) | (1 << (SparqlParser.ISBLANK - 25)) | (1 << (SparqlParser.ISLITERAL - 25)) | (1 << (SparqlParser.REGEX - 25)) | (1 << (SparqlParser.SUBSTR - 25)) | (1 << (SparqlParser.IRI - 25)) | (1 << (SparqlParser.URI - 25)) | (1 << (SparqlParser.BNODE - 25)) | (1 << (SparqlParser.RAND - 25)) | (1 << (SparqlParser.ABS - 25)) | (1 << (SparqlParser.CEIL - 25)) | (1 << (SparqlParser.FLOOR - 25)) | (1 << (SparqlParser.ROUND - 25)) | (1 << (SparqlParser.CONCAT - 25)) | (1 << (SparqlParser.STRLEN - 25)) | (1 << (SparqlParser.UCASE - 25)) | (1 << (SparqlParser.LCASE - 25)) | (1 << (SparqlParser.ENCODE_FOR_URI - 25)) | (1 << (SparqlParser.CONTAINS - 25)) | (1 << (SparqlParser.STRSTARTS - 25)) | (1 << (SparqlParser.STRENDS - 25)) | (1 << (SparqlParser.STRBEFORE - 25)) | (1 << (SparqlParser.STRAFTER - 25)) | (1 << (SparqlParser.REPLACE - 25)) | (1 << (SparqlParser.YEAR - 25)) | (1 << (SparqlParser.MONTH - 25)) | (1 << (SparqlParser.DAY - 25)) | (1 << (SparqlParser.HOURS - 25)) | (1 << (SparqlParser.MINUTES - 25)) | (1 << (SparqlParser.SECONDS - 25)))) != 0) or ((((_la - 89)) & ~0x3f) == 0 and ((1 << (_la - 89)) & ((1 << (SparqlParser.TIMEZONE - 89)) | (1 << (SparqlParser.TZ - 89)) | (1 << (SparqlParser.NOW - 89)) | (1 << (SparqlParser.UUID - 89)) | (1 << (SparqlParser.STRUUID - 89)) | (1 << (SparqlParser.MD5 - 89)) | (1 << (SparqlParser.SHA1 - 89)) | (1 << (SparqlParser.SHA256 - 89)) | (1 << (SparqlParser.SHA384 - 89)) | (1 << (SparqlParser.SHA512 - 89)) | (1 << (SparqlParser.COALESCE - 89)) | (1 << (SparqlParser.IF - 89)) | (1 << (SparqlParser.STRLANG - 89)) | (1 << (SparqlParser.STRDT - 89)) | (1 << (SparqlParser.ISNUMERIC - 89)) | (1 << (SparqlParser.COUNT - 89)) | (1 << (SparqlParser.SUM - 89)) | (1 << (SparqlParser.MIN - 89)) | (1 << (SparqlParser.MAX - 89)) | (1 << (SparqlParser.AVG - 89)) | (1 << (SparqlParser.SAMPLE - 89)) | (1 << (SparqlParser.GROUP_CONCAT - 89)) | (1 << (SparqlParser.NOT - 89)) | (1 << (SparqlParser.EXISTS - 89)) | (1 << (SparqlParser.IRIREF - 89)) | (1 << (SparqlParser.PNAME_NS - 89)) | (1 << (SparqlParser.PNAME_LN - 89)) | (1 << (SparqlParser.VAR1 - 89)) | (1 << (SparqlParser.VAR2 - 89)) | (1 << (SparqlParser.OPEN_BRACE - 89)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupConditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GroupConditionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def builtInCall(self):
            return self.getTypedRuleContext(SparqlParser.BuiltInCallContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SparqlParser.FunctionCallContext,0)


        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def AS(self):
            return self.getToken(SparqlParser.AS, 0)

        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_groupCondition

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGroupCondition(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGroupCondition(self)




    def groupCondition(self):

        localctx = SparqlParser.GroupConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_groupCondition)
        self._la = 0 # Token type
        try:
            self.state = 429
            token = self._input.LA(1)
            if token in [SparqlParser.STR, SparqlParser.LANG, SparqlParser.LANGMATCHES, SparqlParser.DATATYPE, SparqlParser.BOUND, SparqlParser.SAMETERM, SparqlParser.ISIRI, SparqlParser.ISURI, SparqlParser.ISBLANK, SparqlParser.ISLITERAL, SparqlParser.REGEX, SparqlParser.SUBSTR, SparqlParser.IRI, SparqlParser.URI, SparqlParser.BNODE, SparqlParser.RAND, SparqlParser.ABS, SparqlParser.CEIL, SparqlParser.FLOOR, SparqlParser.ROUND, SparqlParser.CONCAT, SparqlParser.STRLEN, SparqlParser.UCASE, SparqlParser.LCASE, SparqlParser.ENCODE_FOR_URI, SparqlParser.CONTAINS, SparqlParser.STRSTARTS, SparqlParser.STRENDS, SparqlParser.STRBEFORE, SparqlParser.STRAFTER, SparqlParser.REPLACE, SparqlParser.YEAR, SparqlParser.MONTH, SparqlParser.DAY, SparqlParser.HOURS, SparqlParser.MINUTES, SparqlParser.SECONDS, SparqlParser.TIMEZONE, SparqlParser.TZ, SparqlParser.NOW, SparqlParser.UUID, SparqlParser.STRUUID, SparqlParser.MD5, SparqlParser.SHA1, SparqlParser.SHA256, SparqlParser.SHA384, SparqlParser.SHA512, SparqlParser.COALESCE, SparqlParser.IF, SparqlParser.STRLANG, SparqlParser.STRDT, SparqlParser.ISNUMERIC, SparqlParser.COUNT, SparqlParser.SUM, SparqlParser.MIN, SparqlParser.MAX, SparqlParser.AVG, SparqlParser.SAMPLE, SparqlParser.GROUP_CONCAT, SparqlParser.NOT, SparqlParser.EXISTS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.builtInCall()

            elif token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.functionCall()

            elif token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 420
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 421
                self.expression(0)
                self.state = 424
                _la = self._input.LA(1)
                if _la==SparqlParser.AS:
                    self.state = 422
                    self.match(SparqlParser.AS)
                    self.state = 423
                    self.var()


                self.state = 426
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.VAR1, SparqlParser.VAR2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 428
                self.var()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HavingClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.HavingClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def HAVING(self):
            return self.getToken(SparqlParser.HAVING, 0)

        def havingCondition(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.HavingConditionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.HavingConditionContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_havingClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterHavingClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitHavingClause(self)




    def havingClause(self):

        localctx = SparqlParser.HavingClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_havingClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(SparqlParser.HAVING)
            self.state = 433 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 432
                self.havingCondition()
                self.state = 435 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 25)) & ~0x3f) == 0 and ((1 << (_la - 25)) & ((1 << (SparqlParser.STR - 25)) | (1 << (SparqlParser.LANG - 25)) | (1 << (SparqlParser.LANGMATCHES - 25)) | (1 << (SparqlParser.DATATYPE - 25)) | (1 << (SparqlParser.BOUND - 25)) | (1 << (SparqlParser.SAMETERM - 25)) | (1 << (SparqlParser.ISIRI - 25)) | (1 << (SparqlParser.ISURI - 25)) | (1 << (SparqlParser.ISBLANK - 25)) | (1 << (SparqlParser.ISLITERAL - 25)) | (1 << (SparqlParser.REGEX - 25)) | (1 << (SparqlParser.SUBSTR - 25)) | (1 << (SparqlParser.IRI - 25)) | (1 << (SparqlParser.URI - 25)) | (1 << (SparqlParser.BNODE - 25)) | (1 << (SparqlParser.RAND - 25)) | (1 << (SparqlParser.ABS - 25)) | (1 << (SparqlParser.CEIL - 25)) | (1 << (SparqlParser.FLOOR - 25)) | (1 << (SparqlParser.ROUND - 25)) | (1 << (SparqlParser.CONCAT - 25)) | (1 << (SparqlParser.STRLEN - 25)) | (1 << (SparqlParser.UCASE - 25)) | (1 << (SparqlParser.LCASE - 25)) | (1 << (SparqlParser.ENCODE_FOR_URI - 25)) | (1 << (SparqlParser.CONTAINS - 25)) | (1 << (SparqlParser.STRSTARTS - 25)) | (1 << (SparqlParser.STRENDS - 25)) | (1 << (SparqlParser.STRBEFORE - 25)) | (1 << (SparqlParser.STRAFTER - 25)) | (1 << (SparqlParser.REPLACE - 25)) | (1 << (SparqlParser.YEAR - 25)) | (1 << (SparqlParser.MONTH - 25)) | (1 << (SparqlParser.DAY - 25)) | (1 << (SparqlParser.HOURS - 25)) | (1 << (SparqlParser.MINUTES - 25)) | (1 << (SparqlParser.SECONDS - 25)))) != 0) or ((((_la - 89)) & ~0x3f) == 0 and ((1 << (_la - 89)) & ((1 << (SparqlParser.TIMEZONE - 89)) | (1 << (SparqlParser.TZ - 89)) | (1 << (SparqlParser.NOW - 89)) | (1 << (SparqlParser.UUID - 89)) | (1 << (SparqlParser.STRUUID - 89)) | (1 << (SparqlParser.MD5 - 89)) | (1 << (SparqlParser.SHA1 - 89)) | (1 << (SparqlParser.SHA256 - 89)) | (1 << (SparqlParser.SHA384 - 89)) | (1 << (SparqlParser.SHA512 - 89)) | (1 << (SparqlParser.COALESCE - 89)) | (1 << (SparqlParser.IF - 89)) | (1 << (SparqlParser.STRLANG - 89)) | (1 << (SparqlParser.STRDT - 89)) | (1 << (SparqlParser.ISNUMERIC - 89)) | (1 << (SparqlParser.COUNT - 89)) | (1 << (SparqlParser.SUM - 89)) | (1 << (SparqlParser.MIN - 89)) | (1 << (SparqlParser.MAX - 89)) | (1 << (SparqlParser.AVG - 89)) | (1 << (SparqlParser.SAMPLE - 89)) | (1 << (SparqlParser.GROUP_CONCAT - 89)) | (1 << (SparqlParser.NOT - 89)) | (1 << (SparqlParser.EXISTS - 89)) | (1 << (SparqlParser.IRIREF - 89)) | (1 << (SparqlParser.PNAME_NS - 89)) | (1 << (SparqlParser.PNAME_LN - 89)) | (1 << (SparqlParser.OPEN_BRACE - 89)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HavingConditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.HavingConditionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def constraint(self):
            return self.getTypedRuleContext(SparqlParser.ConstraintContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_havingCondition

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterHavingCondition(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitHavingCondition(self)




    def havingCondition(self):

        localctx = SparqlParser.HavingConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_havingCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.constraint()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OrderClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.OrderClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(SparqlParser.ORDER, 0)

        def BY(self):
            return self.getToken(SparqlParser.BY, 0)

        def orderCondition(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.OrderConditionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.OrderConditionContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_orderClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterOrderClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitOrderClause(self)




    def orderClause(self):

        localctx = SparqlParser.OrderClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_orderClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(SparqlParser.ORDER)
            self.state = 440
            self.match(SparqlParser.BY)
            self.state = 442 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 441
                self.orderCondition()
                self.state = 444 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SparqlParser.ASC) | (1 << SparqlParser.DESC) | (1 << SparqlParser.STR) | (1 << SparqlParser.LANG) | (1 << SparqlParser.LANGMATCHES) | (1 << SparqlParser.DATATYPE) | (1 << SparqlParser.BOUND) | (1 << SparqlParser.SAMETERM) | (1 << SparqlParser.ISIRI) | (1 << SparqlParser.ISURI) | (1 << SparqlParser.ISBLANK) | (1 << SparqlParser.ISLITERAL) | (1 << SparqlParser.REGEX) | (1 << SparqlParser.SUBSTR))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SparqlParser.IRI - 64)) | (1 << (SparqlParser.URI - 64)) | (1 << (SparqlParser.BNODE - 64)) | (1 << (SparqlParser.RAND - 64)) | (1 << (SparqlParser.ABS - 64)) | (1 << (SparqlParser.CEIL - 64)) | (1 << (SparqlParser.FLOOR - 64)) | (1 << (SparqlParser.ROUND - 64)) | (1 << (SparqlParser.CONCAT - 64)) | (1 << (SparqlParser.STRLEN - 64)) | (1 << (SparqlParser.UCASE - 64)) | (1 << (SparqlParser.LCASE - 64)) | (1 << (SparqlParser.ENCODE_FOR_URI - 64)) | (1 << (SparqlParser.CONTAINS - 64)) | (1 << (SparqlParser.STRSTARTS - 64)) | (1 << (SparqlParser.STRENDS - 64)) | (1 << (SparqlParser.STRBEFORE - 64)) | (1 << (SparqlParser.STRAFTER - 64)) | (1 << (SparqlParser.REPLACE - 64)) | (1 << (SparqlParser.YEAR - 64)) | (1 << (SparqlParser.MONTH - 64)) | (1 << (SparqlParser.DAY - 64)) | (1 << (SparqlParser.HOURS - 64)) | (1 << (SparqlParser.MINUTES - 64)) | (1 << (SparqlParser.SECONDS - 64)) | (1 << (SparqlParser.TIMEZONE - 64)) | (1 << (SparqlParser.TZ - 64)) | (1 << (SparqlParser.NOW - 64)) | (1 << (SparqlParser.UUID - 64)) | (1 << (SparqlParser.STRUUID - 64)) | (1 << (SparqlParser.MD5 - 64)) | (1 << (SparqlParser.SHA1 - 64)) | (1 << (SparqlParser.SHA256 - 64)) | (1 << (SparqlParser.SHA384 - 64)) | (1 << (SparqlParser.SHA512 - 64)) | (1 << (SparqlParser.COALESCE - 64)) | (1 << (SparqlParser.IF - 64)) | (1 << (SparqlParser.STRLANG - 64)) | (1 << (SparqlParser.STRDT - 64)) | (1 << (SparqlParser.ISNUMERIC - 64)) | (1 << (SparqlParser.COUNT - 64)) | (1 << (SparqlParser.SUM - 64)) | (1 << (SparqlParser.MIN - 64)) | (1 << (SparqlParser.MAX - 64)) | (1 << (SparqlParser.AVG - 64)) | (1 << (SparqlParser.SAMPLE - 64)) | (1 << (SparqlParser.GROUP_CONCAT - 64)) | (1 << (SparqlParser.NOT - 64)) | (1 << (SparqlParser.EXISTS - 64)) | (1 << (SparqlParser.IRIREF - 64)) | (1 << (SparqlParser.PNAME_NS - 64)) | (1 << (SparqlParser.PNAME_LN - 64)) | (1 << (SparqlParser.VAR1 - 64)) | (1 << (SparqlParser.VAR2 - 64)))) != 0) or _la==SparqlParser.OPEN_BRACE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OrderConditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.OrderConditionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def ASC(self):
            return self.getToken(SparqlParser.ASC, 0)

        def DESC(self):
            return self.getToken(SparqlParser.DESC, 0)

        def constraint(self):
            return self.getTypedRuleContext(SparqlParser.ConstraintContext,0)


        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_orderCondition

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterOrderCondition(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitOrderCondition(self)




    def orderCondition(self):

        localctx = SparqlParser.OrderConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_orderCondition)
        self._la = 0 # Token type
        try:
            self.state = 453
            token = self._input.LA(1)
            if token in [SparqlParser.ASC, SparqlParser.DESC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                _la = self._input.LA(1)
                if not(_la==SparqlParser.ASC or _la==SparqlParser.DESC):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 447
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 448
                self.expression(0)
                self.state = 449
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STR, SparqlParser.LANG, SparqlParser.LANGMATCHES, SparqlParser.DATATYPE, SparqlParser.BOUND, SparqlParser.SAMETERM, SparqlParser.ISIRI, SparqlParser.ISURI, SparqlParser.ISBLANK, SparqlParser.ISLITERAL, SparqlParser.REGEX, SparqlParser.SUBSTR, SparqlParser.IRI, SparqlParser.URI, SparqlParser.BNODE, SparqlParser.RAND, SparqlParser.ABS, SparqlParser.CEIL, SparqlParser.FLOOR, SparqlParser.ROUND, SparqlParser.CONCAT, SparqlParser.STRLEN, SparqlParser.UCASE, SparqlParser.LCASE, SparqlParser.ENCODE_FOR_URI, SparqlParser.CONTAINS, SparqlParser.STRSTARTS, SparqlParser.STRENDS, SparqlParser.STRBEFORE, SparqlParser.STRAFTER, SparqlParser.REPLACE, SparqlParser.YEAR, SparqlParser.MONTH, SparqlParser.DAY, SparqlParser.HOURS, SparqlParser.MINUTES, SparqlParser.SECONDS, SparqlParser.TIMEZONE, SparqlParser.TZ, SparqlParser.NOW, SparqlParser.UUID, SparqlParser.STRUUID, SparqlParser.MD5, SparqlParser.SHA1, SparqlParser.SHA256, SparqlParser.SHA384, SparqlParser.SHA512, SparqlParser.COALESCE, SparqlParser.IF, SparqlParser.STRLANG, SparqlParser.STRDT, SparqlParser.ISNUMERIC, SparqlParser.COUNT, SparqlParser.SUM, SparqlParser.MIN, SparqlParser.MAX, SparqlParser.AVG, SparqlParser.SAMPLE, SparqlParser.GROUP_CONCAT, SparqlParser.NOT, SparqlParser.EXISTS, SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.constraint()

            elif token in [SparqlParser.VAR1, SparqlParser.VAR2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 452
                self.var()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LimitOffsetClausesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.LimitOffsetClausesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def limitClause(self):
            return self.getTypedRuleContext(SparqlParser.LimitClauseContext,0)


        def offsetClause(self):
            return self.getTypedRuleContext(SparqlParser.OffsetClauseContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_limitOffsetClauses

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterLimitOffsetClauses(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitLimitOffsetClauses(self)




    def limitOffsetClauses(self):

        localctx = SparqlParser.LimitOffsetClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_limitOffsetClauses)
        self._la = 0 # Token type
        try:
            self.state = 463
            token = self._input.LA(1)
            if token in [SparqlParser.LIMIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.limitClause()
                self.state = 457
                _la = self._input.LA(1)
                if _la==SparqlParser.OFFSET:
                    self.state = 456
                    self.offsetClause()



            elif token in [SparqlParser.OFFSET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.offsetClause()
                self.state = 461
                _la = self._input.LA(1)
                if _la==SparqlParser.LIMIT:
                    self.state = 460
                    self.limitClause()



            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LimitClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.LimitClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LIMIT(self):
            return self.getToken(SparqlParser.LIMIT, 0)

        def INTEGER(self):
            return self.getToken(SparqlParser.INTEGER, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_limitClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterLimitClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitLimitClause(self)




    def limitClause(self):

        localctx = SparqlParser.LimitClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_limitClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(SparqlParser.LIMIT)
            self.state = 466
            self.match(SparqlParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OffsetClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.OffsetClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OFFSET(self):
            return self.getToken(SparqlParser.OFFSET, 0)

        def INTEGER(self):
            return self.getToken(SparqlParser.INTEGER, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_offsetClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterOffsetClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitOffsetClause(self)




    def offsetClause(self):

        localctx = SparqlParser.OffsetClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_offsetClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(SparqlParser.OFFSET)
            self.state = 469
            self.match(SparqlParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValuesClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ValuesClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VALUES(self):
            return self.getToken(SparqlParser.VALUES, 0)

        def dataBlock(self):
            return self.getTypedRuleContext(SparqlParser.DataBlockContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_valuesClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterValuesClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitValuesClause(self)




    def valuesClause(self):

        localctx = SparqlParser.ValuesClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_valuesClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            _la = self._input.LA(1)
            if _la==SparqlParser.VALUES:
                self.state = 471
                self.match(SparqlParser.VALUES)
                self.state = 472
                self.dataBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UpdateCommandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.UpdateCommandContext, self).__init__(parent, invokingState)
            self.parser = parser

        def prologue(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.PrologueContext)
            else:
                return self.getTypedRuleContext(SparqlParser.PrologueContext,i)


        def update(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.UpdateContext)
            else:
                return self.getTypedRuleContext(SparqlParser.UpdateContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_updateCommand

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterUpdateCommand(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitUpdateCommand(self)




    def updateCommand(self):

        localctx = SparqlParser.UpdateCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_updateCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.prologue()
            self.state = 490
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SparqlParser.LOAD) | (1 << SparqlParser.CLEAR) | (1 << SparqlParser.DROP) | (1 << SparqlParser.ADD) | (1 << SparqlParser.MOVE) | (1 << SparqlParser.COPY) | (1 << SparqlParser.CREATE) | (1 << SparqlParser.DELETE) | (1 << SparqlParser.INSERT) | (1 << SparqlParser.WITH))) != 0):
                self.state = 476
                self.update()
                self.state = 483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 477
                        self.match(SparqlParser.SEMICOLON)
                        self.state = 478
                        self.prologue()
                        self.state = 479
                        self.update() 
                    self.state = 485
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

                self.state = 488
                _la = self._input.LA(1)
                if _la==SparqlParser.SEMICOLON:
                    self.state = 486
                    self.match(SparqlParser.SEMICOLON)
                    self.state = 487
                    self.prologue()




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UpdateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.UpdateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def load(self):
            return self.getTypedRuleContext(SparqlParser.LoadContext,0)


        def clear(self):
            return self.getTypedRuleContext(SparqlParser.ClearContext,0)


        def drop(self):
            return self.getTypedRuleContext(SparqlParser.DropContext,0)


        def add(self):
            return self.getTypedRuleContext(SparqlParser.AddContext,0)


        def move(self):
            return self.getTypedRuleContext(SparqlParser.MoveContext,0)


        def copy(self):
            return self.getTypedRuleContext(SparqlParser.CopyContext,0)


        def create(self):
            return self.getTypedRuleContext(SparqlParser.CreateContext,0)


        def insertData(self):
            return self.getTypedRuleContext(SparqlParser.InsertDataContext,0)


        def deleteData(self):
            return self.getTypedRuleContext(SparqlParser.DeleteDataContext,0)


        def deleteWhere(self):
            return self.getTypedRuleContext(SparqlParser.DeleteWhereContext,0)


        def modify(self):
            return self.getTypedRuleContext(SparqlParser.ModifyContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_update

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterUpdate(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitUpdate(self)




    def update(self):

        localctx = SparqlParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_update)
        try:
            self.state = 503
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.load()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.clear()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 494
                self.drop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 495
                self.add()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 496
                self.move()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 497
                self.copy()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 498
                self.create()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 499
                self.insertData()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 500
                self.deleteData()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 501
                self.deleteWhere()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 502
                self.modify()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoadContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.LoadContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(SparqlParser.LOAD, 0)

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def SILENT(self):
            return self.getToken(SparqlParser.SILENT, 0)

        def INTO(self):
            return self.getToken(SparqlParser.INTO, 0)

        def graphRef(self):
            return self.getTypedRuleContext(SparqlParser.GraphRefContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_load

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterLoad(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitLoad(self)




    def load(self):

        localctx = SparqlParser.LoadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_load)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(SparqlParser.LOAD)
            self.state = 507
            _la = self._input.LA(1)
            if _la==SparqlParser.SILENT:
                self.state = 506
                self.match(SparqlParser.SILENT)


            self.state = 509
            self.iri()
            self.state = 512
            _la = self._input.LA(1)
            if _la==SparqlParser.INTO:
                self.state = 510
                self.match(SparqlParser.INTO)
                self.state = 511
                self.graphRef()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClearContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ClearContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CLEAR(self):
            return self.getToken(SparqlParser.CLEAR, 0)

        def graphRefAll(self):
            return self.getTypedRuleContext(SparqlParser.GraphRefAllContext,0)


        def SILENT(self):
            return self.getToken(SparqlParser.SILENT, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_clear

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterClear(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitClear(self)




    def clear(self):

        localctx = SparqlParser.ClearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_clear)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(SparqlParser.CLEAR)
            self.state = 516
            _la = self._input.LA(1)
            if _la==SparqlParser.SILENT:
                self.state = 515
                self.match(SparqlParser.SILENT)


            self.state = 518
            self.graphRefAll()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DropContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.DropContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DROP(self):
            return self.getToken(SparqlParser.DROP, 0)

        def graphRefAll(self):
            return self.getTypedRuleContext(SparqlParser.GraphRefAllContext,0)


        def SILENT(self):
            return self.getToken(SparqlParser.SILENT, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_drop

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterDrop(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitDrop(self)




    def drop(self):

        localctx = SparqlParser.DropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_drop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(SparqlParser.DROP)
            self.state = 522
            _la = self._input.LA(1)
            if _la==SparqlParser.SILENT:
                self.state = 521
                self.match(SparqlParser.SILENT)


            self.state = 524
            self.graphRefAll()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.CreateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(SparqlParser.CREATE, 0)

        def graphRef(self):
            return self.getTypedRuleContext(SparqlParser.GraphRefContext,0)


        def SILENT(self):
            return self.getToken(SparqlParser.SILENT, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_create

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterCreate(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitCreate(self)




    def create(self):

        localctx = SparqlParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(SparqlParser.CREATE)
            self.state = 528
            _la = self._input.LA(1)
            if _la==SparqlParser.SILENT:
                self.state = 527
                self.match(SparqlParser.SILENT)


            self.state = 530
            self.graphRef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.AddContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(SparqlParser.ADD, 0)

        def graphOrDefault(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.GraphOrDefaultContext)
            else:
                return self.getTypedRuleContext(SparqlParser.GraphOrDefaultContext,i)


        def TO(self):
            return self.getToken(SparqlParser.TO, 0)

        def SILENT(self):
            return self.getToken(SparqlParser.SILENT, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_add

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterAdd(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitAdd(self)




    def add(self):

        localctx = SparqlParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(SparqlParser.ADD)
            self.state = 534
            _la = self._input.LA(1)
            if _la==SparqlParser.SILENT:
                self.state = 533
                self.match(SparqlParser.SILENT)


            self.state = 536
            self.graphOrDefault()
            self.state = 537
            self.match(SparqlParser.TO)
            self.state = 538
            self.graphOrDefault()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MoveContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.MoveContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MOVE(self):
            return self.getToken(SparqlParser.MOVE, 0)

        def graphOrDefault(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.GraphOrDefaultContext)
            else:
                return self.getTypedRuleContext(SparqlParser.GraphOrDefaultContext,i)


        def TO(self):
            return self.getToken(SparqlParser.TO, 0)

        def SILENT(self):
            return self.getToken(SparqlParser.SILENT, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_move

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterMove(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitMove(self)




    def move(self):

        localctx = SparqlParser.MoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_move)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(SparqlParser.MOVE)
            self.state = 542
            _la = self._input.LA(1)
            if _la==SparqlParser.SILENT:
                self.state = 541
                self.match(SparqlParser.SILENT)


            self.state = 544
            self.graphOrDefault()
            self.state = 545
            self.match(SparqlParser.TO)
            self.state = 546
            self.graphOrDefault()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CopyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.CopyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COPY(self):
            return self.getToken(SparqlParser.COPY, 0)

        def graphOrDefault(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.GraphOrDefaultContext)
            else:
                return self.getTypedRuleContext(SparqlParser.GraphOrDefaultContext,i)


        def TO(self):
            return self.getToken(SparqlParser.TO, 0)

        def SILENT(self):
            return self.getToken(SparqlParser.SILENT, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_copy

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterCopy(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitCopy(self)




    def copy(self):

        localctx = SparqlParser.CopyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_copy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(SparqlParser.COPY)
            self.state = 550
            _la = self._input.LA(1)
            if _la==SparqlParser.SILENT:
                self.state = 549
                self.match(SparqlParser.SILENT)


            self.state = 552
            self.graphOrDefault()
            self.state = 553
            self.match(SparqlParser.TO)
            self.state = 554
            self.graphOrDefault()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InsertDataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.InsertDataContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(SparqlParser.INSERT, 0)

        def DATA(self):
            return self.getToken(SparqlParser.DATA, 0)

        def quadData(self):
            return self.getTypedRuleContext(SparqlParser.QuadDataContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_insertData

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterInsertData(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitInsertData(self)




    def insertData(self):

        localctx = SparqlParser.InsertDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_insertData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(SparqlParser.INSERT)
            self.state = 557
            self.match(SparqlParser.DATA)
            self.state = 558
            self.quadData()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeleteDataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.DeleteDataContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(SparqlParser.DELETE, 0)

        def DATA(self):
            return self.getToken(SparqlParser.DATA, 0)

        def quadData(self):
            return self.getTypedRuleContext(SparqlParser.QuadDataContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_deleteData

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterDeleteData(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitDeleteData(self)




    def deleteData(self):

        localctx = SparqlParser.DeleteDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_deleteData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(SparqlParser.DELETE)
            self.state = 561
            self.match(SparqlParser.DATA)
            self.state = 562
            self.quadData()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeleteWhereContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.DeleteWhereContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(SparqlParser.DELETE, 0)

        def WHERE(self):
            return self.getToken(SparqlParser.WHERE, 0)

        def quadPattern(self):
            return self.getTypedRuleContext(SparqlParser.QuadPatternContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_deleteWhere

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterDeleteWhere(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitDeleteWhere(self)




    def deleteWhere(self):

        localctx = SparqlParser.DeleteWhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_deleteWhere)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(SparqlParser.DELETE)
            self.state = 565
            self.match(SparqlParser.WHERE)
            self.state = 566
            self.quadPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModifyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ModifyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(SparqlParser.WHERE, 0)

        def groupGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GroupGraphPatternContext,0)


        def deleteClause(self):
            return self.getTypedRuleContext(SparqlParser.DeleteClauseContext,0)


        def insertClause(self):
            return self.getTypedRuleContext(SparqlParser.InsertClauseContext,0)


        def WITH(self):
            return self.getToken(SparqlParser.WITH, 0)

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def usingClause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.UsingClauseContext)
            else:
                return self.getTypedRuleContext(SparqlParser.UsingClauseContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_modify

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterModify(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitModify(self)




    def modify(self):

        localctx = SparqlParser.ModifyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_modify)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            _la = self._input.LA(1)
            if _la==SparqlParser.WITH:
                self.state = 568
                self.match(SparqlParser.WITH)
                self.state = 569
                self.iri()


            self.state = 577
            token = self._input.LA(1)
            if token in [SparqlParser.DELETE]:
                self.state = 572
                self.deleteClause()
                self.state = 574
                _la = self._input.LA(1)
                if _la==SparqlParser.INSERT:
                    self.state = 573
                    self.insertClause()



            elif token in [SparqlParser.INSERT]:
                self.state = 576
                self.insertClause()

            else:
                raise NoViableAltException(self)

            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.USING:
                self.state = 579
                self.usingClause()
                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 585
            self.match(SparqlParser.WHERE)
            self.state = 586
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeleteClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.DeleteClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(SparqlParser.DELETE, 0)

        def quadPattern(self):
            return self.getTypedRuleContext(SparqlParser.QuadPatternContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_deleteClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterDeleteClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitDeleteClause(self)




    def deleteClause(self):

        localctx = SparqlParser.DeleteClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_deleteClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(SparqlParser.DELETE)
            self.state = 589
            self.quadPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InsertClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.InsertClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(SparqlParser.INSERT, 0)

        def quadPattern(self):
            return self.getTypedRuleContext(SparqlParser.QuadPatternContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_insertClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterInsertClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitInsertClause(self)




    def insertClause(self):

        localctx = SparqlParser.InsertClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_insertClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(SparqlParser.INSERT)
            self.state = 592
            self.quadPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UsingClauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.UsingClauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def USING(self):
            return self.getToken(SparqlParser.USING, 0)

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def NAMED(self):
            return self.getToken(SparqlParser.NAMED, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_usingClause

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterUsingClause(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitUsingClause(self)




    def usingClause(self):

        localctx = SparqlParser.UsingClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_usingClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(SparqlParser.USING)
            self.state = 596
            _la = self._input.LA(1)
            if _la==SparqlParser.NAMED:
                self.state = 595
                self.match(SparqlParser.NAMED)


            self.state = 598
            self.iri()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphOrDefaultContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GraphOrDefaultContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(SparqlParser.DEFAULT, 0)

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def GRAPH(self):
            return self.getToken(SparqlParser.GRAPH, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_graphOrDefault

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGraphOrDefault(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGraphOrDefault(self)




    def graphOrDefault(self):

        localctx = SparqlParser.GraphOrDefaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_graphOrDefault)
        self._la = 0 # Token type
        try:
            self.state = 605
            token = self._input.LA(1)
            if token in [SparqlParser.DEFAULT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.match(SparqlParser.DEFAULT)

            elif token in [SparqlParser.GRAPH, SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 602
                _la = self._input.LA(1)
                if _la==SparqlParser.GRAPH:
                    self.state = 601
                    self.match(SparqlParser.GRAPH)


                self.state = 604
                self.iri()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphRefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GraphRefContext, self).__init__(parent, invokingState)
            self.parser = parser

        def GRAPH(self):
            return self.getToken(SparqlParser.GRAPH, 0)

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_graphRef

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGraphRef(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGraphRef(self)




    def graphRef(self):

        localctx = SparqlParser.GraphRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_graphRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(SparqlParser.GRAPH)
            self.state = 608
            self.iri()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphRefAllContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GraphRefAllContext, self).__init__(parent, invokingState)
            self.parser = parser

        def graphRef(self):
            return self.getTypedRuleContext(SparqlParser.GraphRefContext,0)


        def DEFAULT(self):
            return self.getToken(SparqlParser.DEFAULT, 0)

        def NAMED(self):
            return self.getToken(SparqlParser.NAMED, 0)

        def ALL(self):
            return self.getToken(SparqlParser.ALL, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_graphRefAll

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGraphRefAll(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGraphRefAll(self)




    def graphRefAll(self):

        localctx = SparqlParser.GraphRefAllContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_graphRefAll)
        try:
            self.state = 614
            token = self._input.LA(1)
            if token in [SparqlParser.GRAPH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 610
                self.graphRef()

            elif token in [SparqlParser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
                self.match(SparqlParser.DEFAULT)

            elif token in [SparqlParser.NAMED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 612
                self.match(SparqlParser.NAMED)

            elif token in [SparqlParser.ALL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 613
                self.match(SparqlParser.ALL)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuadPatternContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.QuadPatternContext, self).__init__(parent, invokingState)
            self.parser = parser

        def quads(self):
            return self.getTypedRuleContext(SparqlParser.QuadsContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_quadPattern

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterQuadPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitQuadPattern(self)




    def quadPattern(self):

        localctx = SparqlParser.QuadPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_quadPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.match(SparqlParser.OPEN_CURLY_BRACE)
            self.state = 617
            self.quads()
            self.state = 618
            self.match(SparqlParser.CLOSE_CURLY_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuadDataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.QuadDataContext, self).__init__(parent, invokingState)
            self.parser = parser

        def quads(self):
            return self.getTypedRuleContext(SparqlParser.QuadsContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_quadData

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterQuadData(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitQuadData(self)




    def quadData(self):

        localctx = SparqlParser.QuadDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_quadData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.match(SparqlParser.OPEN_CURLY_BRACE)
            self.state = 621
            self.quads()
            self.state = 622
            self.match(SparqlParser.CLOSE_CURLY_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuadsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.QuadsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def triplesTemplate(self):
            return self.getTypedRuleContext(SparqlParser.TriplesTemplateContext,0)


        def quadsDetails(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.QuadsDetailsContext)
            else:
                return self.getTypedRuleContext(SparqlParser.QuadsDetailsContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_quads

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterQuads(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitQuads(self)




    def quads(self):

        localctx = SparqlParser.QuadsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_quads)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 625
            _la = self._input.LA(1)
            if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                self.state = 624
                self.triplesTemplate()


            self.state = 630
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.GRAPH:
                self.state = 627
                self.quadsDetails()
                self.state = 632
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuadsDetailsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.QuadsDetailsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def quadsNotTriples(self):
            return self.getTypedRuleContext(SparqlParser.QuadsNotTriplesContext,0)


        def triplesTemplate(self):
            return self.getTypedRuleContext(SparqlParser.TriplesTemplateContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_quadsDetails

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterQuadsDetails(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitQuadsDetails(self)




    def quadsDetails(self):

        localctx = SparqlParser.QuadsDetailsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_quadsDetails)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.quadsNotTriples()
            self.state = 635
            _la = self._input.LA(1)
            if _la==SparqlParser.DOT:
                self.state = 634
                self.match(SparqlParser.DOT)


            self.state = 638
            _la = self._input.LA(1)
            if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                self.state = 637
                self.triplesTemplate()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuadsNotTriplesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.QuadsNotTriplesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def GRAPH(self):
            return self.getToken(SparqlParser.GRAPH, 0)

        def varOrIRI(self):
            return self.getTypedRuleContext(SparqlParser.VarOrIRIContext,0)


        def triplesTemplate(self):
            return self.getTypedRuleContext(SparqlParser.TriplesTemplateContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_quadsNotTriples

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterQuadsNotTriples(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitQuadsNotTriples(self)




    def quadsNotTriples(self):

        localctx = SparqlParser.QuadsNotTriplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_quadsNotTriples)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.match(SparqlParser.GRAPH)
            self.state = 641
            self.varOrIRI()
            self.state = 642
            self.match(SparqlParser.OPEN_CURLY_BRACE)
            self.state = 644
            _la = self._input.LA(1)
            if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                self.state = 643
                self.triplesTemplate()


            self.state = 646
            self.match(SparqlParser.CLOSE_CURLY_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TriplesTemplateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.TriplesTemplateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def triplesSameSubject(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.TriplesSameSubjectContext)
            else:
                return self.getTypedRuleContext(SparqlParser.TriplesSameSubjectContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_triplesTemplate

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterTriplesTemplate(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitTriplesTemplate(self)




    def triplesTemplate(self):

        localctx = SparqlParser.TriplesTemplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_triplesTemplate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            self.triplesSameSubject()
            self.state = 655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.DOT:
                self.state = 649
                self.match(SparqlParser.DOT)
                self.state = 651
                _la = self._input.LA(1)
                if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                    self.state = 650
                    self.triplesSameSubject()


                self.state = 657
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupGraphPatternContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GroupGraphPatternContext, self).__init__(parent, invokingState)
            self.parser = parser

        def subSelect(self):
            return self.getTypedRuleContext(SparqlParser.SubSelectContext,0)


        def groupGraphPatternSub(self):
            return self.getTypedRuleContext(SparqlParser.GroupGraphPatternSubContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_groupGraphPattern

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGroupGraphPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGroupGraphPattern(self)




    def groupGraphPattern(self):

        localctx = SparqlParser.GroupGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_groupGraphPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.match(SparqlParser.OPEN_CURLY_BRACE)
            self.state = 661
            token = self._input.LA(1)
            if token in [SparqlParser.SELECT]:
                self.state = 659
                self.subSelect()

            elif token in [SparqlParser.VALUES, SparqlParser.OPTIONAL, SparqlParser.GRAPH, SparqlParser.FILTER, SparqlParser.TRUE, SparqlParser.FALSE, SparqlParser.SERVICE, SparqlParser.BIND, SparqlParser.MINUS, SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.BLANK_NODE_LABEL, SparqlParser.VAR1, SparqlParser.VAR2, SparqlParser.INTEGER, SparqlParser.DECIMAL, SparqlParser.DOUBLE, SparqlParser.INTEGER_POSITIVE, SparqlParser.DECIMAL_POSITIVE, SparqlParser.DOUBLE_POSITIVE, SparqlParser.INTEGER_NEGATIVE, SparqlParser.DECIMAL_NEGATIVE, SparqlParser.DOUBLE_NEGATIVE, SparqlParser.STRING_LITERAL1, SparqlParser.STRING_LITERAL2, SparqlParser.STRING_LITERAL_LONG1, SparqlParser.STRING_LITERAL_LONG2, SparqlParser.OPEN_BRACE, SparqlParser.OPEN_CURLY_BRACE, SparqlParser.CLOSE_CURLY_BRACE, SparqlParser.OPEN_SQUARE_BRACKET]:
                self.state = 660
                self.groupGraphPatternSub()

            else:
                raise NoViableAltException(self)

            self.state = 663
            self.match(SparqlParser.CLOSE_CURLY_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupGraphPatternSubContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GroupGraphPatternSubContext, self).__init__(parent, invokingState)
            self.parser = parser

        def triplesBlock(self):
            return self.getTypedRuleContext(SparqlParser.TriplesBlockContext,0)


        def groupGraphPatternSubList(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.GroupGraphPatternSubListContext)
            else:
                return self.getTypedRuleContext(SparqlParser.GroupGraphPatternSubListContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_groupGraphPatternSub

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGroupGraphPatternSub(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGroupGraphPatternSub(self)




    def groupGraphPatternSub(self):

        localctx = SparqlParser.GroupGraphPatternSubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_groupGraphPatternSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            _la = self._input.LA(1)
            if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                self.state = 665
                self.triplesBlock()


            self.state = 671
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SparqlParser.VALUES) | (1 << SparqlParser.OPTIONAL) | (1 << SparqlParser.GRAPH) | (1 << SparqlParser.FILTER) | (1 << SparqlParser.SERVICE) | (1 << SparqlParser.BIND) | (1 << SparqlParser.MINUS))) != 0) or _la==SparqlParser.OPEN_CURLY_BRACE:
                self.state = 668
                self.groupGraphPatternSubList()
                self.state = 673
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupGraphPatternSubListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GroupGraphPatternSubListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def graphPatternNotTriples(self):
            return self.getTypedRuleContext(SparqlParser.GraphPatternNotTriplesContext,0)


        def triplesBlock(self):
            return self.getTypedRuleContext(SparqlParser.TriplesBlockContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_groupGraphPatternSubList

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGroupGraphPatternSubList(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGroupGraphPatternSubList(self)




    def groupGraphPatternSubList(self):

        localctx = SparqlParser.GroupGraphPatternSubListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_groupGraphPatternSubList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
            self.graphPatternNotTriples()
            self.state = 676
            _la = self._input.LA(1)
            if _la==SparqlParser.DOT:
                self.state = 675
                self.match(SparqlParser.DOT)


            self.state = 679
            _la = self._input.LA(1)
            if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                self.state = 678
                self.triplesBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TriplesBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.TriplesBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def triplesSameSubjectPath(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.TriplesSameSubjectPathContext)
            else:
                return self.getTypedRuleContext(SparqlParser.TriplesSameSubjectPathContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_triplesBlock

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterTriplesBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitTriplesBlock(self)




    def triplesBlock(self):

        localctx = SparqlParser.TriplesBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_triplesBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.triplesSameSubjectPath()
            self.state = 688
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.DOT:
                self.state = 682
                self.match(SparqlParser.DOT)
                self.state = 684
                _la = self._input.LA(1)
                if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                    self.state = 683
                    self.triplesSameSubjectPath()


                self.state = 690
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphPatternNotTriplesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GraphPatternNotTriplesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def groupOrUnionGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GroupOrUnionGraphPatternContext,0)


        def optionalGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.OptionalGraphPatternContext,0)


        def minusGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.MinusGraphPatternContext,0)


        def graphGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GraphGraphPatternContext,0)


        def serviceGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.ServiceGraphPatternContext,0)


        def xfilter(self):
            return self.getTypedRuleContext(SparqlParser.XfilterContext,0)


        def bind(self):
            return self.getTypedRuleContext(SparqlParser.BindContext,0)


        def inlineData(self):
            return self.getTypedRuleContext(SparqlParser.InlineDataContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_graphPatternNotTriples

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGraphPatternNotTriples(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGraphPatternNotTriples(self)




    def graphPatternNotTriples(self):

        localctx = SparqlParser.GraphPatternNotTriplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_graphPatternNotTriples)
        try:
            self.state = 699
            token = self._input.LA(1)
            if token in [SparqlParser.OPEN_CURLY_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 691
                self.groupOrUnionGraphPattern()

            elif token in [SparqlParser.OPTIONAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 692
                self.optionalGraphPattern()

            elif token in [SparqlParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 693
                self.minusGraphPattern()

            elif token in [SparqlParser.GRAPH]:
                self.enterOuterAlt(localctx, 4)
                self.state = 694
                self.graphGraphPattern()

            elif token in [SparqlParser.SERVICE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 695
                self.serviceGraphPattern()

            elif token in [SparqlParser.FILTER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 696
                self.xfilter()

            elif token in [SparqlParser.BIND]:
                self.enterOuterAlt(localctx, 7)
                self.state = 697
                self.bind()

            elif token in [SparqlParser.VALUES]:
                self.enterOuterAlt(localctx, 8)
                self.state = 698
                self.inlineData()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptionalGraphPatternContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.OptionalGraphPatternContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OPTIONAL(self):
            return self.getToken(SparqlParser.OPTIONAL, 0)

        def groupGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GroupGraphPatternContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_optionalGraphPattern

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterOptionalGraphPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitOptionalGraphPattern(self)




    def optionalGraphPattern(self):

        localctx = SparqlParser.OptionalGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_optionalGraphPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 701
            self.match(SparqlParser.OPTIONAL)
            self.state = 702
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphGraphPatternContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GraphGraphPatternContext, self).__init__(parent, invokingState)
            self.parser = parser

        def GRAPH(self):
            return self.getToken(SparqlParser.GRAPH, 0)

        def varOrIRI(self):
            return self.getTypedRuleContext(SparqlParser.VarOrIRIContext,0)


        def groupGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GroupGraphPatternContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_graphGraphPattern

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGraphGraphPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGraphGraphPattern(self)




    def graphGraphPattern(self):

        localctx = SparqlParser.GraphGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_graphGraphPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 704
            self.match(SparqlParser.GRAPH)
            self.state = 705
            self.varOrIRI()
            self.state = 706
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ServiceGraphPatternContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ServiceGraphPatternContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SERVICE(self):
            return self.getToken(SparqlParser.SERVICE, 0)

        def varOrIRI(self):
            return self.getTypedRuleContext(SparqlParser.VarOrIRIContext,0)


        def groupGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GroupGraphPatternContext,0)


        def SILENT(self):
            return self.getToken(SparqlParser.SILENT, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_serviceGraphPattern

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterServiceGraphPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitServiceGraphPattern(self)




    def serviceGraphPattern(self):

        localctx = SparqlParser.ServiceGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_serviceGraphPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 708
            self.match(SparqlParser.SERVICE)
            self.state = 710
            _la = self._input.LA(1)
            if _la==SparqlParser.SILENT:
                self.state = 709
                self.match(SparqlParser.SILENT)


            self.state = 712
            self.varOrIRI()
            self.state = 713
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BindContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.BindContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BIND(self):
            return self.getToken(SparqlParser.BIND, 0)

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def AS(self):
            return self.getToken(SparqlParser.AS, 0)

        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_bind

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterBind(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitBind(self)




    def bind(self):

        localctx = SparqlParser.BindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_bind)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 715
            self.match(SparqlParser.BIND)
            self.state = 716
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 717
            self.expression(0)
            self.state = 718
            self.match(SparqlParser.AS)
            self.state = 719
            self.var()
            self.state = 720
            self.match(SparqlParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InlineDataContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.InlineDataContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VALUES(self):
            return self.getToken(SparqlParser.VALUES, 0)

        def dataBlock(self):
            return self.getTypedRuleContext(SparqlParser.DataBlockContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_inlineData

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterInlineData(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitInlineData(self)




    def inlineData(self):

        localctx = SparqlParser.InlineDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_inlineData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
            self.match(SparqlParser.VALUES)
            self.state = 723
            self.dataBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataBlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.DataBlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def inlineDataOneVar(self):
            return self.getTypedRuleContext(SparqlParser.InlineDataOneVarContext,0)


        def inlineDataFull(self):
            return self.getTypedRuleContext(SparqlParser.InlineDataFullContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_dataBlock

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterDataBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitDataBlock(self)




    def dataBlock(self):

        localctx = SparqlParser.DataBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_dataBlock)
        try:
            self.state = 727
            token = self._input.LA(1)
            if token in [SparqlParser.VAR1, SparqlParser.VAR2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 725
                self.inlineDataOneVar()

            elif token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 726
                self.inlineDataFull()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InlineDataOneVarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.InlineDataOneVarContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def dataBlockValue(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.DataBlockValueContext)
            else:
                return self.getTypedRuleContext(SparqlParser.DataBlockValueContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_inlineDataOneVar

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterInlineDataOneVar(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitInlineDataOneVar(self)




    def inlineDataOneVar(self):

        localctx = SparqlParser.InlineDataOneVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_inlineDataOneVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self.var()
            self.state = 730
            self.match(SparqlParser.OPEN_CURLY_BRACE)
            self.state = 734
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SparqlParser.TRUE) | (1 << SparqlParser.FALSE) | (1 << SparqlParser.UNDEF))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)))) != 0):
                self.state = 731
                self.dataBlockValue()
                self.state = 736
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 737
            self.match(SparqlParser.CLOSE_CURLY_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InlineDataFullContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.InlineDataFullContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.VarContext)
            else:
                return self.getTypedRuleContext(SparqlParser.VarContext,i)


        def dataBlockValues(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.DataBlockValuesContext)
            else:
                return self.getTypedRuleContext(SparqlParser.DataBlockValuesContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_inlineDataFull

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterInlineDataFull(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitInlineDataFull(self)




    def inlineDataFull(self):

        localctx = SparqlParser.InlineDataFullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_inlineDataFull)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 743
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.VAR1 or _la==SparqlParser.VAR2:
                self.state = 740
                self.var()
                self.state = 745
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 746
            self.match(SparqlParser.CLOSE_BRACE)
            self.state = 747
            self.match(SparqlParser.OPEN_CURLY_BRACE)
            self.state = 751
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.OPEN_BRACE:
                self.state = 748
                self.dataBlockValues()
                self.state = 753
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 754
            self.match(SparqlParser.CLOSE_CURLY_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataBlockValuesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.DataBlockValuesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dataBlockValue(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.DataBlockValueContext)
            else:
                return self.getTypedRuleContext(SparqlParser.DataBlockValueContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_dataBlockValues

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterDataBlockValues(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitDataBlockValues(self)




    def dataBlockValues(self):

        localctx = SparqlParser.DataBlockValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_dataBlockValues)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 756
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 760
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SparqlParser.TRUE) | (1 << SparqlParser.FALSE) | (1 << SparqlParser.UNDEF))) != 0) or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)))) != 0):
                self.state = 757
                self.dataBlockValue()
                self.state = 762
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 763
            self.match(SparqlParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataBlockValueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.DataBlockValueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def rdfLiteral(self):
            return self.getTypedRuleContext(SparqlParser.RdfLiteralContext,0)


        def numericLiteral(self):
            return self.getTypedRuleContext(SparqlParser.NumericLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(SparqlParser.BooleanLiteralContext,0)


        def UNDEF(self):
            return self.getToken(SparqlParser.UNDEF, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_dataBlockValue

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterDataBlockValue(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitDataBlockValue(self)




    def dataBlockValue(self):

        localctx = SparqlParser.DataBlockValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_dataBlockValue)
        try:
            self.state = 770
            token = self._input.LA(1)
            if token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 765
                self.iri()

            elif token in [SparqlParser.STRING_LITERAL1, SparqlParser.STRING_LITERAL2, SparqlParser.STRING_LITERAL_LONG1, SparqlParser.STRING_LITERAL_LONG2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 766
                self.rdfLiteral()

            elif token in [SparqlParser.INTEGER, SparqlParser.DECIMAL, SparqlParser.DOUBLE, SparqlParser.INTEGER_POSITIVE, SparqlParser.DECIMAL_POSITIVE, SparqlParser.DOUBLE_POSITIVE, SparqlParser.INTEGER_NEGATIVE, SparqlParser.DECIMAL_NEGATIVE, SparqlParser.DOUBLE_NEGATIVE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 767
                self.numericLiteral()

            elif token in [SparqlParser.TRUE, SparqlParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 768
                self.booleanLiteral()

            elif token in [SparqlParser.UNDEF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 769
                self.match(SparqlParser.UNDEF)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MinusGraphPatternContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.MinusGraphPatternContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(SparqlParser.MINUS, 0)

        def groupGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GroupGraphPatternContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_minusGraphPattern

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterMinusGraphPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitMinusGraphPattern(self)




    def minusGraphPattern(self):

        localctx = SparqlParser.MinusGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_minusGraphPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 772
            self.match(SparqlParser.MINUS)
            self.state = 773
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupOrUnionGraphPatternContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GroupOrUnionGraphPatternContext, self).__init__(parent, invokingState)
            self.parser = parser

        def groupGraphPattern(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.GroupGraphPatternContext)
            else:
                return self.getTypedRuleContext(SparqlParser.GroupGraphPatternContext,i)


        def UNION(self, i=None):
            if i is None:
                return self.getTokens(SparqlParser.UNION)
            else:
                return self.getToken(SparqlParser.UNION, i)

        def getRuleIndex(self):
            return SparqlParser.RULE_groupOrUnionGraphPattern

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGroupOrUnionGraphPattern(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGroupOrUnionGraphPattern(self)




    def groupOrUnionGraphPattern(self):

        localctx = SparqlParser.GroupOrUnionGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_groupOrUnionGraphPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
            self.groupGraphPattern()
            self.state = 780
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.UNION:
                self.state = 776
                self.match(SparqlParser.UNION)
                self.state = 777
                self.groupGraphPattern()
                self.state = 782
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class XfilterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.XfilterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(SparqlParser.FILTER, 0)

        def constraint(self):
            return self.getTypedRuleContext(SparqlParser.ConstraintContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_xfilter

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterXfilter(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitXfilter(self)




    def xfilter(self):

        localctx = SparqlParser.XfilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_xfilter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 783
            self.match(SparqlParser.FILTER)
            self.state = 784
            self.constraint()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ConstraintContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def builtInCall(self):
            return self.getTypedRuleContext(SparqlParser.BuiltInCallContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SparqlParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_constraint

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterConstraint(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitConstraint(self)




    def constraint(self):

        localctx = SparqlParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_constraint)
        try:
            self.state = 792
            token = self._input.LA(1)
            if token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 786
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 787
                self.expression(0)
                self.state = 788
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STR, SparqlParser.LANG, SparqlParser.LANGMATCHES, SparqlParser.DATATYPE, SparqlParser.BOUND, SparqlParser.SAMETERM, SparqlParser.ISIRI, SparqlParser.ISURI, SparqlParser.ISBLANK, SparqlParser.ISLITERAL, SparqlParser.REGEX, SparqlParser.SUBSTR, SparqlParser.IRI, SparqlParser.URI, SparqlParser.BNODE, SparqlParser.RAND, SparqlParser.ABS, SparqlParser.CEIL, SparqlParser.FLOOR, SparqlParser.ROUND, SparqlParser.CONCAT, SparqlParser.STRLEN, SparqlParser.UCASE, SparqlParser.LCASE, SparqlParser.ENCODE_FOR_URI, SparqlParser.CONTAINS, SparqlParser.STRSTARTS, SparqlParser.STRENDS, SparqlParser.STRBEFORE, SparqlParser.STRAFTER, SparqlParser.REPLACE, SparqlParser.YEAR, SparqlParser.MONTH, SparqlParser.DAY, SparqlParser.HOURS, SparqlParser.MINUTES, SparqlParser.SECONDS, SparqlParser.TIMEZONE, SparqlParser.TZ, SparqlParser.NOW, SparqlParser.UUID, SparqlParser.STRUUID, SparqlParser.MD5, SparqlParser.SHA1, SparqlParser.SHA256, SparqlParser.SHA384, SparqlParser.SHA512, SparqlParser.COALESCE, SparqlParser.IF, SparqlParser.STRLANG, SparqlParser.STRDT, SparqlParser.ISNUMERIC, SparqlParser.COUNT, SparqlParser.SUM, SparqlParser.MIN, SparqlParser.MAX, SparqlParser.AVG, SparqlParser.SAMPLE, SparqlParser.GROUP_CONCAT, SparqlParser.NOT, SparqlParser.EXISTS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 790
                self.builtInCall()

            elif token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 791
                self.functionCall()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.FunctionCallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def argList(self):
            return self.getTypedRuleContext(SparqlParser.ArgListContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_functionCall

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = SparqlParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 794
            self.iri()
            self.state = 795
            self.argList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ArgListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionListContext,0)


        def DISTINCT(self):
            return self.getToken(SparqlParser.DISTINCT, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_argList

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterArgList(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitArgList(self)




    def argList(self):

        localctx = SparqlParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 797
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 803
            token = self._input.LA(1)
            if token in [SparqlParser.DISTINCT, SparqlParser.STR, SparqlParser.LANG, SparqlParser.LANGMATCHES, SparqlParser.DATATYPE, SparqlParser.BOUND, SparqlParser.SAMETERM, SparqlParser.ISIRI, SparqlParser.ISURI, SparqlParser.ISBLANK, SparqlParser.ISLITERAL, SparqlParser.REGEX, SparqlParser.SUBSTR, SparqlParser.TRUE, SparqlParser.FALSE, SparqlParser.IRI, SparqlParser.URI, SparqlParser.BNODE, SparqlParser.RAND, SparqlParser.ABS, SparqlParser.CEIL, SparqlParser.FLOOR, SparqlParser.ROUND, SparqlParser.CONCAT, SparqlParser.STRLEN, SparqlParser.UCASE, SparqlParser.LCASE, SparqlParser.ENCODE_FOR_URI, SparqlParser.CONTAINS, SparqlParser.STRSTARTS, SparqlParser.STRENDS, SparqlParser.STRBEFORE, SparqlParser.STRAFTER, SparqlParser.REPLACE, SparqlParser.YEAR, SparqlParser.MONTH, SparqlParser.DAY, SparqlParser.HOURS, SparqlParser.MINUTES, SparqlParser.SECONDS, SparqlParser.TIMEZONE, SparqlParser.TZ, SparqlParser.NOW, SparqlParser.UUID, SparqlParser.STRUUID, SparqlParser.MD5, SparqlParser.SHA1, SparqlParser.SHA256, SparqlParser.SHA384, SparqlParser.SHA512, SparqlParser.COALESCE, SparqlParser.IF, SparqlParser.STRLANG, SparqlParser.STRDT, SparqlParser.ISNUMERIC, SparqlParser.COUNT, SparqlParser.SUM, SparqlParser.MIN, SparqlParser.MAX, SparqlParser.AVG, SparqlParser.SAMPLE, SparqlParser.GROUP_CONCAT, SparqlParser.NOT, SparqlParser.EXISTS, SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.VAR1, SparqlParser.VAR2, SparqlParser.INTEGER, SparqlParser.DECIMAL, SparqlParser.DOUBLE, SparqlParser.INTEGER_POSITIVE, SparqlParser.DECIMAL_POSITIVE, SparqlParser.DOUBLE_POSITIVE, SparqlParser.INTEGER_NEGATIVE, SparqlParser.DECIMAL_NEGATIVE, SparqlParser.DOUBLE_NEGATIVE, SparqlParser.STRING_LITERAL1, SparqlParser.STRING_LITERAL2, SparqlParser.STRING_LITERAL_LONG1, SparqlParser.STRING_LITERAL_LONG2, SparqlParser.OPEN_BRACE, SparqlParser.PLUS_SIGN, SparqlParser.MINUS_SIGN, SparqlParser.ASTERISK, SparqlParser.NEGATION, SparqlParser.DIVIDE]:
                self.state = 799
                _la = self._input.LA(1)
                if _la==SparqlParser.DISTINCT:
                    self.state = 798
                    self.match(SparqlParser.DISTINCT)


                self.state = 801
                self.expressionList()

            elif token in [SparqlParser.CLOSE_BRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 805
            self.match(SparqlParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ExpressionListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_expressionList

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterExpressionList(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = SparqlParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 807
            self.expression(0)
            self.state = 812
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.COMMA:
                self.state = 808
                self.match(SparqlParser.COMMA)
                self.state = 809
                self.expression(0)
                self.state = 814
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstructTemplateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ConstructTemplateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def constructTriples(self):
            return self.getTypedRuleContext(SparqlParser.ConstructTriplesContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_constructTemplate

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterConstructTemplate(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitConstructTemplate(self)




    def constructTemplate(self):

        localctx = SparqlParser.ConstructTemplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_constructTemplate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 815
            self.match(SparqlParser.OPEN_CURLY_BRACE)
            self.state = 817
            _la = self._input.LA(1)
            if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                self.state = 816
                self.constructTriples()


            self.state = 819
            self.match(SparqlParser.CLOSE_CURLY_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstructTriplesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ConstructTriplesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def triplesSameSubject(self):
            return self.getTypedRuleContext(SparqlParser.TriplesSameSubjectContext,0)


        def constructTriples(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ConstructTriplesContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ConstructTriplesContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_constructTriples

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterConstructTriples(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitConstructTriples(self)




    def constructTriples(self):

        localctx = SparqlParser.ConstructTriplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_constructTriples)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 821
            self.triplesSameSubject()
            self.state = 828
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 822
                    self.match(SparqlParser.DOT)
                    self.state = 824
                    _la = self._input.LA(1)
                    if _la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0):
                        self.state = 823
                        self.constructTriples()

             
                self.state = 830
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TriplesSameSubjectContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.TriplesSameSubjectContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varOrTerm(self):
            return self.getTypedRuleContext(SparqlParser.VarOrTermContext,0)


        def propertyListNotEmpty(self):
            return self.getTypedRuleContext(SparqlParser.PropertyListNotEmptyContext,0)


        def triplesNode(self):
            return self.getTypedRuleContext(SparqlParser.TriplesNodeContext,0)


        def propertyList(self):
            return self.getTypedRuleContext(SparqlParser.PropertyListContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_triplesSameSubject

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterTriplesSameSubject(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitTriplesSameSubject(self)




    def triplesSameSubject(self):

        localctx = SparqlParser.TriplesSameSubjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_triplesSameSubject)
        try:
            self.state = 837
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 831
                self.varOrTerm()
                self.state = 832
                self.propertyListNotEmpty()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 834
                self.triplesNode()
                self.state = 835
                self.propertyList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PropertyListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyListNotEmpty(self):
            return self.getTypedRuleContext(SparqlParser.PropertyListNotEmptyContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_propertyList

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPropertyList(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPropertyList(self)




    def propertyList(self):

        localctx = SparqlParser.PropertyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_propertyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 840
            _la = self._input.LA(1)
            if _la==SparqlParser.A or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)))) != 0):
                self.state = 839
                self.propertyListNotEmpty()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyListNotEmptyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PropertyListNotEmptyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def verb(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.VerbContext)
            else:
                return self.getTypedRuleContext(SparqlParser.VerbContext,i)


        def objectList(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ObjectListContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ObjectListContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_propertyListNotEmpty

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPropertyListNotEmpty(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPropertyListNotEmpty(self)




    def propertyListNotEmpty(self):

        localctx = SparqlParser.PropertyListNotEmptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_propertyListNotEmpty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 842
            self.verb()
            self.state = 843
            self.objectList()
            self.state = 852
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.SEMICOLON:
                self.state = 844
                self.match(SparqlParser.SEMICOLON)
                self.state = 848
                _la = self._input.LA(1)
                if _la==SparqlParser.A or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)))) != 0):
                    self.state = 845
                    self.verb()
                    self.state = 846
                    self.objectList()


                self.state = 854
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VerbContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.VerbContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varOrIRI(self):
            return self.getTypedRuleContext(SparqlParser.VarOrIRIContext,0)


        def A(self):
            return self.getToken(SparqlParser.A, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_verb

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterVerb(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitVerb(self)




    def verb(self):

        localctx = SparqlParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_verb)
        try:
            self.state = 857
            token = self._input.LA(1)
            if token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.VAR1, SparqlParser.VAR2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 855
                self.varOrIRI()

            elif token in [SparqlParser.A]:
                self.enterOuterAlt(localctx, 2)
                self.state = 856
                self.match(SparqlParser.A)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ObjectListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def yobject(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.YobjectContext)
            else:
                return self.getTypedRuleContext(SparqlParser.YobjectContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_objectList

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterObjectList(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitObjectList(self)




    def objectList(self):

        localctx = SparqlParser.ObjectListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_objectList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 859
            self.yobject()
            self.state = 864
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.COMMA:
                self.state = 860
                self.match(SparqlParser.COMMA)
                self.state = 861
                self.yobject()
                self.state = 866
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class YobjectContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.YobjectContext, self).__init__(parent, invokingState)
            self.parser = parser

        def graphNode(self):
            return self.getTypedRuleContext(SparqlParser.GraphNodeContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_yobject

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterYobject(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitYobject(self)




    def yobject(self):

        localctx = SparqlParser.YobjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_yobject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 867
            self.graphNode()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TriplesSameSubjectPathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.TriplesSameSubjectPathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varOrTerm(self):
            return self.getTypedRuleContext(SparqlParser.VarOrTermContext,0)


        def propertyListPathNotEmpty(self):
            return self.getTypedRuleContext(SparqlParser.PropertyListPathNotEmptyContext,0)


        def triplesNodePath(self):
            return self.getTypedRuleContext(SparqlParser.TriplesNodePathContext,0)


        def propertyListPath(self):
            return self.getTypedRuleContext(SparqlParser.PropertyListPathContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_triplesSameSubjectPath

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterTriplesSameSubjectPath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitTriplesSameSubjectPath(self)




    def triplesSameSubjectPath(self):

        localctx = SparqlParser.TriplesSameSubjectPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_triplesSameSubjectPath)
        try:
            self.state = 875
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 869
                self.varOrTerm()
                self.state = 870
                self.propertyListPathNotEmpty()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 872
                self.triplesNodePath()
                self.state = 873
                self.propertyListPath()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyListPathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PropertyListPathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyListPathNotEmpty(self):
            return self.getTypedRuleContext(SparqlParser.PropertyListPathNotEmptyContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_propertyListPath

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPropertyListPath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPropertyListPath(self)




    def propertyListPath(self):

        localctx = SparqlParser.PropertyListPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_propertyListPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 878
            _la = self._input.LA(1)
            if _la==SparqlParser.A or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INVERSE - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.NEGATION - 115)))) != 0):
                self.state = 877
                self.propertyListPathNotEmpty()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyListPathNotEmptyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PropertyListPathNotEmptyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def objectListPath(self):
            return self.getTypedRuleContext(SparqlParser.ObjectListPathContext,0)


        def verbPath(self):
            return self.getTypedRuleContext(SparqlParser.VerbPathContext,0)


        def verbSimple(self):
            return self.getTypedRuleContext(SparqlParser.VerbSimpleContext,0)


        def propertyListPathNotEmptyList(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.PropertyListPathNotEmptyListContext)
            else:
                return self.getTypedRuleContext(SparqlParser.PropertyListPathNotEmptyListContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_propertyListPathNotEmpty

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPropertyListPathNotEmpty(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPropertyListPathNotEmpty(self)




    def propertyListPathNotEmpty(self):

        localctx = SparqlParser.PropertyListPathNotEmptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_propertyListPathNotEmpty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 882
            token = self._input.LA(1)
            if token in [SparqlParser.A, SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.INVERSE, SparqlParser.OPEN_BRACE, SparqlParser.NEGATION]:
                self.state = 880
                self.verbPath()

            elif token in [SparqlParser.VAR1, SparqlParser.VAR2]:
                self.state = 881
                self.verbSimple()

            else:
                raise NoViableAltException(self)

            self.state = 884
            self.objectListPath()
            self.state = 891
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.SEMICOLON:
                self.state = 885
                self.match(SparqlParser.SEMICOLON)
                self.state = 887
                _la = self._input.LA(1)
                if _la==SparqlParser.A or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INVERSE - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.NEGATION - 115)))) != 0):
                    self.state = 886
                    self.propertyListPathNotEmptyList()


                self.state = 893
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PropertyListPathNotEmptyListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PropertyListPathNotEmptyListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def objectList(self):
            return self.getTypedRuleContext(SparqlParser.ObjectListContext,0)


        def verbPath(self):
            return self.getTypedRuleContext(SparqlParser.VerbPathContext,0)


        def verbSimple(self):
            return self.getTypedRuleContext(SparqlParser.VerbSimpleContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_propertyListPathNotEmptyList

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPropertyListPathNotEmptyList(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPropertyListPathNotEmptyList(self)




    def propertyListPathNotEmptyList(self):

        localctx = SparqlParser.PropertyListPathNotEmptyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_propertyListPathNotEmptyList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 896
            token = self._input.LA(1)
            if token in [SparqlParser.A, SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.INVERSE, SparqlParser.OPEN_BRACE, SparqlParser.NEGATION]:
                self.state = 894
                self.verbPath()

            elif token in [SparqlParser.VAR1, SparqlParser.VAR2]:
                self.state = 895
                self.verbSimple()

            else:
                raise NoViableAltException(self)

            self.state = 898
            self.objectList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VerbPathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.VerbPathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def path(self):
            return self.getTypedRuleContext(SparqlParser.PathContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_verbPath

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterVerbPath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitVerbPath(self)




    def verbPath(self):

        localctx = SparqlParser.VerbPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_verbPath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 900
            self.path()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VerbSimpleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.VerbSimpleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_verbSimple

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterVerbSimple(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitVerbSimple(self)




    def verbSimple(self):

        localctx = SparqlParser.VerbSimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_verbSimple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 902
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectListPathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ObjectListPathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def objectPath(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ObjectPathContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ObjectPathContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_objectListPath

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterObjectListPath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitObjectListPath(self)




    def objectListPath(self):

        localctx = SparqlParser.ObjectListPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_objectListPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 904
            self.objectPath()
            self.state = 909
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.COMMA:
                self.state = 905
                self.match(SparqlParser.COMMA)
                self.state = 906
                self.objectPath()
                self.state = 911
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectPathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ObjectPathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def graphNodePath(self):
            return self.getTypedRuleContext(SparqlParser.GraphNodePathContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_objectPath

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterObjectPath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitObjectPath(self)




    def objectPath(self):

        localctx = SparqlParser.ObjectPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_objectPath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 912
            self.graphNodePath()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def pathAlternative(self):
            return self.getTypedRuleContext(SparqlParser.PathAlternativeContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_path

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPath(self)




    def path(self):

        localctx = SparqlParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 914
            self.pathAlternative()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathAlternativeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PathAlternativeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def pathSequence(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.PathSequenceContext)
            else:
                return self.getTypedRuleContext(SparqlParser.PathSequenceContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_pathAlternative

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPathAlternative(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPathAlternative(self)




    def pathAlternative(self):

        localctx = SparqlParser.PathAlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_pathAlternative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 916
            self.pathSequence()
            self.state = 921
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.PIPE:
                self.state = 917
                self.match(SparqlParser.PIPE)
                self.state = 918
                self.pathSequence()
                self.state = 923
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PathSequenceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def pathEltOrInverse(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.PathEltOrInverseContext)
            else:
                return self.getTypedRuleContext(SparqlParser.PathEltOrInverseContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_pathSequence

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPathSequence(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPathSequence(self)




    def pathSequence(self):

        localctx = SparqlParser.PathSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_pathSequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 924
            self.pathEltOrInverse()
            self.state = 929
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SparqlParser.DIVIDE:
                self.state = 925
                self.match(SparqlParser.DIVIDE)
                self.state = 926
                self.pathEltOrInverse()
                self.state = 931
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathEltContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PathEltContext, self).__init__(parent, invokingState)
            self.parser = parser

        def pathPrimary(self):
            return self.getTypedRuleContext(SparqlParser.PathPrimaryContext,0)


        def pathMod(self):
            return self.getTypedRuleContext(SparqlParser.PathModContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_pathElt

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPathElt(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPathElt(self)




    def pathElt(self):

        localctx = SparqlParser.PathEltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_pathElt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 932
            self.pathPrimary()
            self.state = 934
            _la = self._input.LA(1)
            if ((((_la - 151)) & ~0x3f) == 0 and ((1 << (_la - 151)) & ((1 << (SparqlParser.PLUS_SIGN - 151)) | (1 << (SparqlParser.ASTERISK - 151)) | (1 << (SparqlParser.QUESTION_MARK - 151)))) != 0):
                self.state = 933
                self.pathMod()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathEltOrInverseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PathEltOrInverseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def pathElt(self):
            return self.getTypedRuleContext(SparqlParser.PathEltContext,0)


        def INVERSE(self):
            return self.getToken(SparqlParser.INVERSE, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_pathEltOrInverse

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPathEltOrInverse(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPathEltOrInverse(self)




    def pathEltOrInverse(self):

        localctx = SparqlParser.PathEltOrInverseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_pathEltOrInverse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 937
            _la = self._input.LA(1)
            if _la==SparqlParser.INVERSE:
                self.state = 936
                self.match(SparqlParser.INVERSE)


            self.state = 939
            self.pathElt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathModContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PathModContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token


        def getRuleIndex(self):
            return SparqlParser.RULE_pathMod

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPathMod(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPathMod(self)




    def pathMod(self):

        localctx = SparqlParser.PathModContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_pathMod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 941
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(((((_la - 151)) & ~0x3f) == 0 and ((1 << (_la - 151)) & ((1 << (SparqlParser.PLUS_SIGN - 151)) | (1 << (SparqlParser.ASTERISK - 151)) | (1 << (SparqlParser.QUESTION_MARK - 151)))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathPrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PathPrimaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def A(self):
            return self.getToken(SparqlParser.A, 0)

        def pathNegatedPropertySet(self):
            return self.getTypedRuleContext(SparqlParser.PathNegatedPropertySetContext,0)


        def path(self):
            return self.getTypedRuleContext(SparqlParser.PathContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_pathPrimary

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPathPrimary(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPathPrimary(self)




    def pathPrimary(self):

        localctx = SparqlParser.PathPrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_pathPrimary)
        try:
            self.state = 951
            token = self._input.LA(1)
            if token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 943
                self.iri()

            elif token in [SparqlParser.A]:
                self.enterOuterAlt(localctx, 2)
                self.state = 944
                self.match(SparqlParser.A)

            elif token in [SparqlParser.NEGATION]:
                self.enterOuterAlt(localctx, 3)
                self.state = 945
                self.match(SparqlParser.NEGATION)
                self.state = 946
                self.pathNegatedPropertySet()

            elif token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 947
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 948
                self.path()
                self.state = 949
                self.match(SparqlParser.CLOSE_BRACE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathNegatedPropertySetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PathNegatedPropertySetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def pathOneInPropertySet(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.PathOneInPropertySetContext)
            else:
                return self.getTypedRuleContext(SparqlParser.PathOneInPropertySetContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_pathNegatedPropertySet

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPathNegatedPropertySet(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPathNegatedPropertySet(self)




    def pathNegatedPropertySet(self):

        localctx = SparqlParser.PathNegatedPropertySetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_pathNegatedPropertySet)
        self._la = 0 # Token type
        try:
            self.state = 966
            token = self._input.LA(1)
            if token in [SparqlParser.A, SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.INVERSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 953
                self.pathOneInPropertySet()

            elif token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 954
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 963
                _la = self._input.LA(1)
                if _la==SparqlParser.A or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.INVERSE - 115)))) != 0):
                    self.state = 955
                    self.pathOneInPropertySet()
                    self.state = 960
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==SparqlParser.PIPE:
                        self.state = 956
                        self.match(SparqlParser.PIPE)
                        self.state = 957
                        self.pathOneInPropertySet()
                        self.state = 962
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 965
                self.match(SparqlParser.CLOSE_BRACE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathOneInPropertySetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PathOneInPropertySetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def A(self):
            return self.getToken(SparqlParser.A, 0)

        def INVERSE(self):
            return self.getToken(SparqlParser.INVERSE, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_pathOneInPropertySet

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPathOneInPropertySet(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPathOneInPropertySet(self)




    def pathOneInPropertySet(self):

        localctx = SparqlParser.PathOneInPropertySetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_pathOneInPropertySet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 969
            _la = self._input.LA(1)
            if _la==SparqlParser.INVERSE:
                self.state = 968
                self.match(SparqlParser.INVERSE)


            self.state = 973
            token = self._input.LA(1)
            if token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.state = 971
                self.iri()

            elif token in [SparqlParser.A]:
                self.state = 972
                self.match(SparqlParser.A)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntegerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.IntegerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(SparqlParser.INTEGER, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_integer

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterInteger(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitInteger(self)




    def integer(self):

        localctx = SparqlParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 975
            self.match(SparqlParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TriplesNodeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.TriplesNodeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def collection(self):
            return self.getTypedRuleContext(SparqlParser.CollectionContext,0)


        def blankNodePropertyList(self):
            return self.getTypedRuleContext(SparqlParser.BlankNodePropertyListContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_triplesNode

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterTriplesNode(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitTriplesNode(self)




    def triplesNode(self):

        localctx = SparqlParser.TriplesNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_triplesNode)
        try:
            self.state = 979
            token = self._input.LA(1)
            if token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 977
                self.collection()

            elif token in [SparqlParser.OPEN_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 978
                self.blankNodePropertyList()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlankNodePropertyListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.BlankNodePropertyListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyListNotEmpty(self):
            return self.getTypedRuleContext(SparqlParser.PropertyListNotEmptyContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_blankNodePropertyList

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterBlankNodePropertyList(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitBlankNodePropertyList(self)




    def blankNodePropertyList(self):

        localctx = SparqlParser.BlankNodePropertyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_blankNodePropertyList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 981
            self.match(SparqlParser.OPEN_SQUARE_BRACKET)
            self.state = 982
            self.propertyListNotEmpty()
            self.state = 983
            self.match(SparqlParser.CLOSE_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TriplesNodePathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.TriplesNodePathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def collectionPath(self):
            return self.getTypedRuleContext(SparqlParser.CollectionPathContext,0)


        def blankNodePropertyListPath(self):
            return self.getTypedRuleContext(SparqlParser.BlankNodePropertyListPathContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_triplesNodePath

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterTriplesNodePath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitTriplesNodePath(self)




    def triplesNodePath(self):

        localctx = SparqlParser.TriplesNodePathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_triplesNodePath)
        try:
            self.state = 987
            token = self._input.LA(1)
            if token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 985
                self.collectionPath()

            elif token in [SparqlParser.OPEN_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 986
                self.blankNodePropertyListPath()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlankNodePropertyListPathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.BlankNodePropertyListPathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def propertyListPathNotEmpty(self):
            return self.getTypedRuleContext(SparqlParser.PropertyListPathNotEmptyContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_blankNodePropertyListPath

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterBlankNodePropertyListPath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitBlankNodePropertyListPath(self)




    def blankNodePropertyListPath(self):

        localctx = SparqlParser.BlankNodePropertyListPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_blankNodePropertyListPath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 989
            self.match(SparqlParser.OPEN_SQUARE_BRACKET)
            self.state = 990
            self.propertyListPathNotEmpty()
            self.state = 991
            self.match(SparqlParser.CLOSE_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CollectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.CollectionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def graphNode(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.GraphNodeContext)
            else:
                return self.getTypedRuleContext(SparqlParser.GraphNodeContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_collection

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterCollection(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitCollection(self)




    def collection(self):

        localctx = SparqlParser.CollectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_collection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 993
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 995 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 994
                self.graphNode()
                self.state = 997 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0)):
                    break

            self.state = 999
            self.match(SparqlParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CollectionPathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.CollectionPathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def graphNodePath(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.GraphNodePathContext)
            else:
                return self.getTypedRuleContext(SparqlParser.GraphNodePathContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_collectionPath

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterCollectionPath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitCollectionPath(self)




    def collectionPath(self):

        localctx = SparqlParser.CollectionPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_collectionPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1001
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 1003 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1002
                self.graphNodePath()
                self.state = 1005 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SparqlParser.TRUE or _la==SparqlParser.FALSE or ((((_la - 115)) & ~0x3f) == 0 and ((1 << (_la - 115)) & ((1 << (SparqlParser.IRIREF - 115)) | (1 << (SparqlParser.PNAME_NS - 115)) | (1 << (SparqlParser.PNAME_LN - 115)) | (1 << (SparqlParser.BLANK_NODE_LABEL - 115)) | (1 << (SparqlParser.VAR1 - 115)) | (1 << (SparqlParser.VAR2 - 115)) | (1 << (SparqlParser.INTEGER - 115)) | (1 << (SparqlParser.DECIMAL - 115)) | (1 << (SparqlParser.DOUBLE - 115)) | (1 << (SparqlParser.INTEGER_POSITIVE - 115)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 115)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 115)) | (1 << (SparqlParser.INTEGER_NEGATIVE - 115)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 115)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 115)) | (1 << (SparqlParser.STRING_LITERAL1 - 115)) | (1 << (SparqlParser.STRING_LITERAL2 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 115)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 115)) | (1 << (SparqlParser.OPEN_BRACE - 115)) | (1 << (SparqlParser.OPEN_SQUARE_BRACKET - 115)))) != 0)):
                    break

            self.state = 1007
            self.match(SparqlParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphNodeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GraphNodeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varOrTerm(self):
            return self.getTypedRuleContext(SparqlParser.VarOrTermContext,0)


        def triplesNode(self):
            return self.getTypedRuleContext(SparqlParser.TriplesNodeContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_graphNode

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGraphNode(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGraphNode(self)




    def graphNode(self):

        localctx = SparqlParser.GraphNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_graphNode)
        try:
            self.state = 1011
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1009
                self.varOrTerm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1010
                self.triplesNode()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphNodePathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GraphNodePathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varOrTerm(self):
            return self.getTypedRuleContext(SparqlParser.VarOrTermContext,0)


        def triplesNodePath(self):
            return self.getTypedRuleContext(SparqlParser.TriplesNodePathContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_graphNodePath

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGraphNodePath(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGraphNodePath(self)




    def graphNodePath(self):

        localctx = SparqlParser.GraphNodePathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_graphNodePath)
        try:
            self.state = 1015
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1013
                self.varOrTerm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1014
                self.triplesNodePath()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarOrTermContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.VarOrTermContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def graphTerm(self):
            return self.getTypedRuleContext(SparqlParser.GraphTermContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_varOrTerm

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterVarOrTerm(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitVarOrTerm(self)




    def varOrTerm(self):

        localctx = SparqlParser.VarOrTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_varOrTerm)
        try:
            self.state = 1019
            token = self._input.LA(1)
            if token in [SparqlParser.VAR1, SparqlParser.VAR2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1017
                self.var()

            elif token in [SparqlParser.TRUE, SparqlParser.FALSE, SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.BLANK_NODE_LABEL, SparqlParser.INTEGER, SparqlParser.DECIMAL, SparqlParser.DOUBLE, SparqlParser.INTEGER_POSITIVE, SparqlParser.DECIMAL_POSITIVE, SparqlParser.DOUBLE_POSITIVE, SparqlParser.INTEGER_NEGATIVE, SparqlParser.DECIMAL_NEGATIVE, SparqlParser.DOUBLE_NEGATIVE, SparqlParser.STRING_LITERAL1, SparqlParser.STRING_LITERAL2, SparqlParser.STRING_LITERAL_LONG1, SparqlParser.STRING_LITERAL_LONG2, SparqlParser.OPEN_BRACE, SparqlParser.OPEN_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1018
                self.graphTerm()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarOrIRIContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.VarOrIRIContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_varOrIRI

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterVarOrIRI(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitVarOrIRI(self)




    def varOrIRI(self):

        localctx = SparqlParser.VarOrIRIContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_varOrIRI)
        try:
            self.state = 1023
            token = self._input.LA(1)
            if token in [SparqlParser.VAR1, SparqlParser.VAR2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1021
                self.var()

            elif token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1022
                self.iri()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.VarContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR1(self):
            return self.getToken(SparqlParser.VAR1, 0)

        def VAR2(self):
            return self.getToken(SparqlParser.VAR2, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_var

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterVar(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitVar(self)




    def var(self):

        localctx = SparqlParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1025
            _la = self._input.LA(1)
            if not(_la==SparqlParser.VAR1 or _la==SparqlParser.VAR2):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GraphTermContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.GraphTermContext, self).__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def rdfLiteral(self):
            return self.getTypedRuleContext(SparqlParser.RdfLiteralContext,0)


        def numericLiteral(self):
            return self.getTypedRuleContext(SparqlParser.NumericLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(SparqlParser.BooleanLiteralContext,0)


        def blankNode(self):
            return self.getTypedRuleContext(SparqlParser.BlankNodeContext,0)


        def nil(self):
            return self.getTypedRuleContext(SparqlParser.NilContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_graphTerm

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterGraphTerm(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitGraphTerm(self)




    def graphTerm(self):

        localctx = SparqlParser.GraphTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_graphTerm)
        try:
            self.state = 1033
            token = self._input.LA(1)
            if token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1027
                self.iri()

            elif token in [SparqlParser.STRING_LITERAL1, SparqlParser.STRING_LITERAL2, SparqlParser.STRING_LITERAL_LONG1, SparqlParser.STRING_LITERAL_LONG2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1028
                self.rdfLiteral()

            elif token in [SparqlParser.INTEGER, SparqlParser.DECIMAL, SparqlParser.DOUBLE, SparqlParser.INTEGER_POSITIVE, SparqlParser.DECIMAL_POSITIVE, SparqlParser.DOUBLE_POSITIVE, SparqlParser.INTEGER_NEGATIVE, SparqlParser.DECIMAL_NEGATIVE, SparqlParser.DOUBLE_NEGATIVE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1029
                self.numericLiteral()

            elif token in [SparqlParser.TRUE, SparqlParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1030
                self.booleanLiteral()

            elif token in [SparqlParser.BLANK_NODE_LABEL, SparqlParser.OPEN_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1031
                self.blankNode()

            elif token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1032
                self.nil()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NilContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.NilContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SparqlParser.RULE_nil

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterNil(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitNil(self)




    def nil(self):

        localctx = SparqlParser.NilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_nil)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1035
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 1036
            self.match(SparqlParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SparqlParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(SparqlParser.ExpressionContext, self).copyFrom(ctx)


    class UnarySignedLiteralExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.UnarySignedLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)

        def unaryLiteralExpression(self):
            return self.getTypedRuleContext(SparqlParser.UnaryLiteralExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterUnarySignedLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitUnarySignedLiteralExpression(self)


    class ConditionalOrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.ConditionalOrExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterConditionalOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitConditionalOrExpression(self)


    class AdditiveExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.AdditiveExpressionContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitAdditiveExpression(self)


    class UnaryAdditiveExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.UnaryAdditiveExpressionContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterUnaryAdditiveExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitUnaryAdditiveExpression(self)


    class RelationalExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.RelationalExpressionContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitRelationalExpression(self)


    class RelationalSetExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.RelationalSetExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)

        def IN(self):
            return self.getToken(SparqlParser.IN, 0)
        def NOT(self):
            return self.getToken(SparqlParser.NOT, 0)
        def expressionList(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionListContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterRelationalSetExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitRelationalSetExpression(self)


    class UnaryMultiplicativeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.UnaryMultiplicativeExpressionContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterUnaryMultiplicativeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitUnaryMultiplicativeExpression(self)


    class BaseExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.BaseExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def primaryExpression(self):
            return self.getTypedRuleContext(SparqlParser.PrimaryExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterBaseExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitBaseExpression(self)


    class MultiplicativeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.MultiplicativeExpressionContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitMultiplicativeExpression(self)


    class ConditionalAndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.ConditionalAndExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterConditionalAndExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitConditionalAndExpression(self)


    class UnaryNegationExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a SparqlParser.ExpressionContext)
            super(SparqlParser.UnaryNegationExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterUnaryNegationExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitUnaryNegationExpression(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SparqlParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 220
        self.enterRecursionRule(localctx, 220, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1046
            token = self._input.LA(1)
            if token in [SparqlParser.ASTERISK, SparqlParser.DIVIDE]:
                localctx = SparqlParser.UnaryMultiplicativeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 1039
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==SparqlParser.ASTERISK or _la==SparqlParser.DIVIDE):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 1040
                self.expression(10)

            elif token in [SparqlParser.PLUS_SIGN, SparqlParser.MINUS_SIGN]:
                localctx = SparqlParser.UnaryAdditiveExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1041
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==SparqlParser.PLUS_SIGN or _la==SparqlParser.MINUS_SIGN):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 1042
                self.expression(9)

            elif token in [SparqlParser.NEGATION]:
                localctx = SparqlParser.UnaryNegationExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1043
                self.match(SparqlParser.NEGATION)
                self.state = 1044
                self.expression(8)

            elif token in [SparqlParser.STR, SparqlParser.LANG, SparqlParser.LANGMATCHES, SparqlParser.DATATYPE, SparqlParser.BOUND, SparqlParser.SAMETERM, SparqlParser.ISIRI, SparqlParser.ISURI, SparqlParser.ISBLANK, SparqlParser.ISLITERAL, SparqlParser.REGEX, SparqlParser.SUBSTR, SparqlParser.TRUE, SparqlParser.FALSE, SparqlParser.IRI, SparqlParser.URI, SparqlParser.BNODE, SparqlParser.RAND, SparqlParser.ABS, SparqlParser.CEIL, SparqlParser.FLOOR, SparqlParser.ROUND, SparqlParser.CONCAT, SparqlParser.STRLEN, SparqlParser.UCASE, SparqlParser.LCASE, SparqlParser.ENCODE_FOR_URI, SparqlParser.CONTAINS, SparqlParser.STRSTARTS, SparqlParser.STRENDS, SparqlParser.STRBEFORE, SparqlParser.STRAFTER, SparqlParser.REPLACE, SparqlParser.YEAR, SparqlParser.MONTH, SparqlParser.DAY, SparqlParser.HOURS, SparqlParser.MINUTES, SparqlParser.SECONDS, SparqlParser.TIMEZONE, SparqlParser.TZ, SparqlParser.NOW, SparqlParser.UUID, SparqlParser.STRUUID, SparqlParser.MD5, SparqlParser.SHA1, SparqlParser.SHA256, SparqlParser.SHA384, SparqlParser.SHA512, SparqlParser.COALESCE, SparqlParser.IF, SparqlParser.STRLANG, SparqlParser.STRDT, SparqlParser.ISNUMERIC, SparqlParser.COUNT, SparqlParser.SUM, SparqlParser.MIN, SparqlParser.MAX, SparqlParser.AVG, SparqlParser.SAMPLE, SparqlParser.GROUP_CONCAT, SparqlParser.NOT, SparqlParser.EXISTS, SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN, SparqlParser.VAR1, SparqlParser.VAR2, SparqlParser.INTEGER, SparqlParser.DECIMAL, SparqlParser.DOUBLE, SparqlParser.INTEGER_POSITIVE, SparqlParser.DECIMAL_POSITIVE, SparqlParser.DOUBLE_POSITIVE, SparqlParser.INTEGER_NEGATIVE, SparqlParser.DECIMAL_NEGATIVE, SparqlParser.DOUBLE_NEGATIVE, SparqlParser.STRING_LITERAL1, SparqlParser.STRING_LITERAL2, SparqlParser.STRING_LITERAL_LONG1, SparqlParser.STRING_LITERAL_LONG2, SparqlParser.OPEN_BRACE]:
                localctx = SparqlParser.BaseExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 1045
                self.primaryExpression()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1077
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,121,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1075
                    la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
                    if la_ == 1:
                        localctx = SparqlParser.MultiplicativeExpressionContext(self, SparqlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1048
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 1049
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SparqlParser.ASTERISK or _la==SparqlParser.DIVIDE):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 1050
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = SparqlParser.AdditiveExpressionContext(self, SparqlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1051
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 1052
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SparqlParser.PLUS_SIGN or _la==SparqlParser.MINUS_SIGN):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 1053
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = SparqlParser.RelationalExpressionContext(self, SparqlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1054
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1055
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (SparqlParser.LESS_EQUAL - 137)) | (1 << (SparqlParser.GREATER_EQUAL - 137)) | (1 << (SparqlParser.NOT_EQUAL - 137)) | (1 << (SparqlParser.EQUAL - 137)) | (1 << (SparqlParser.LESS - 137)) | (1 << (SparqlParser.GREATER - 137)))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 1056
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = SparqlParser.UnarySignedLiteralExpressionContext(self, SparqlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1057
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1058
                        self.unaryLiteralExpression()
                        pass

                    elif la_ == 5:
                        localctx = SparqlParser.RelationalSetExpressionContext(self, SparqlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1059
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 1061
                        _la = self._input.LA(1)
                        if _la==SparqlParser.NOT:
                            self.state = 1060
                            self.match(SparqlParser.NOT)


                        self.state = 1063
                        self.match(SparqlParser.IN)
                        self.state = 1064
                        self.match(SparqlParser.OPEN_BRACE)
                        self.state = 1066
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SparqlParser.STR) | (1 << SparqlParser.LANG) | (1 << SparqlParser.LANGMATCHES) | (1 << SparqlParser.DATATYPE) | (1 << SparqlParser.BOUND) | (1 << SparqlParser.SAMETERM) | (1 << SparqlParser.ISIRI) | (1 << SparqlParser.ISURI) | (1 << SparqlParser.ISBLANK) | (1 << SparqlParser.ISLITERAL) | (1 << SparqlParser.REGEX) | (1 << SparqlParser.SUBSTR) | (1 << SparqlParser.TRUE) | (1 << SparqlParser.FALSE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SparqlParser.IRI - 64)) | (1 << (SparqlParser.URI - 64)) | (1 << (SparqlParser.BNODE - 64)) | (1 << (SparqlParser.RAND - 64)) | (1 << (SparqlParser.ABS - 64)) | (1 << (SparqlParser.CEIL - 64)) | (1 << (SparqlParser.FLOOR - 64)) | (1 << (SparqlParser.ROUND - 64)) | (1 << (SparqlParser.CONCAT - 64)) | (1 << (SparqlParser.STRLEN - 64)) | (1 << (SparqlParser.UCASE - 64)) | (1 << (SparqlParser.LCASE - 64)) | (1 << (SparqlParser.ENCODE_FOR_URI - 64)) | (1 << (SparqlParser.CONTAINS - 64)) | (1 << (SparqlParser.STRSTARTS - 64)) | (1 << (SparqlParser.STRENDS - 64)) | (1 << (SparqlParser.STRBEFORE - 64)) | (1 << (SparqlParser.STRAFTER - 64)) | (1 << (SparqlParser.REPLACE - 64)) | (1 << (SparqlParser.YEAR - 64)) | (1 << (SparqlParser.MONTH - 64)) | (1 << (SparqlParser.DAY - 64)) | (1 << (SparqlParser.HOURS - 64)) | (1 << (SparqlParser.MINUTES - 64)) | (1 << (SparqlParser.SECONDS - 64)) | (1 << (SparqlParser.TIMEZONE - 64)) | (1 << (SparqlParser.TZ - 64)) | (1 << (SparqlParser.NOW - 64)) | (1 << (SparqlParser.UUID - 64)) | (1 << (SparqlParser.STRUUID - 64)) | (1 << (SparqlParser.MD5 - 64)) | (1 << (SparqlParser.SHA1 - 64)) | (1 << (SparqlParser.SHA256 - 64)) | (1 << (SparqlParser.SHA384 - 64)) | (1 << (SparqlParser.SHA512 - 64)) | (1 << (SparqlParser.COALESCE - 64)) | (1 << (SparqlParser.IF - 64)) | (1 << (SparqlParser.STRLANG - 64)) | (1 << (SparqlParser.STRDT - 64)) | (1 << (SparqlParser.ISNUMERIC - 64)) | (1 << (SparqlParser.COUNT - 64)) | (1 << (SparqlParser.SUM - 64)) | (1 << (SparqlParser.MIN - 64)) | (1 << (SparqlParser.MAX - 64)) | (1 << (SparqlParser.AVG - 64)) | (1 << (SparqlParser.SAMPLE - 64)) | (1 << (SparqlParser.GROUP_CONCAT - 64)) | (1 << (SparqlParser.NOT - 64)) | (1 << (SparqlParser.EXISTS - 64)) | (1 << (SparqlParser.IRIREF - 64)) | (1 << (SparqlParser.PNAME_NS - 64)) | (1 << (SparqlParser.PNAME_LN - 64)) | (1 << (SparqlParser.VAR1 - 64)) | (1 << (SparqlParser.VAR2 - 64)) | (1 << (SparqlParser.INTEGER - 64)) | (1 << (SparqlParser.DECIMAL - 64)) | (1 << (SparqlParser.DOUBLE - 64)) | (1 << (SparqlParser.INTEGER_POSITIVE - 64)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 64)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (SparqlParser.INTEGER_NEGATIVE - 128)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 128)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 128)) | (1 << (SparqlParser.STRING_LITERAL1 - 128)) | (1 << (SparqlParser.STRING_LITERAL2 - 128)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 128)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 128)) | (1 << (SparqlParser.OPEN_BRACE - 128)) | (1 << (SparqlParser.PLUS_SIGN - 128)) | (1 << (SparqlParser.MINUS_SIGN - 128)) | (1 << (SparqlParser.ASTERISK - 128)) | (1 << (SparqlParser.NEGATION - 128)) | (1 << (SparqlParser.DIVIDE - 128)))) != 0):
                            self.state = 1065
                            self.expressionList()


                        self.state = 1068
                        self.match(SparqlParser.CLOSE_BRACE)
                        pass

                    elif la_ == 6:
                        localctx = SparqlParser.ConditionalAndExpressionContext(self, SparqlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1069
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 1070
                        self.match(SparqlParser.AND)
                        self.state = 1071
                        self.expression(0)
                        pass

                    elif la_ == 7:
                        localctx = SparqlParser.ConditionalOrExpressionContext(self, SparqlParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 1072
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                        self.state = 1073
                        self.match(SparqlParser.OR)
                        self.state = 1074
                        self.expression(0)
                        pass

             
                self.state = 1079
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,121,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class UnaryLiteralExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.UnaryLiteralExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def numericLiteralPositive(self):
            return self.getTypedRuleContext(SparqlParser.NumericLiteralPositiveContext,0)


        def numericLiteralNegative(self):
            return self.getTypedRuleContext(SparqlParser.NumericLiteralNegativeContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(SparqlParser.UnaryExpressionContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_unaryLiteralExpression

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterUnaryLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitUnaryLiteralExpression(self)




    def unaryLiteralExpression(self):

        localctx = SparqlParser.UnaryLiteralExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_unaryLiteralExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1082
            token = self._input.LA(1)
            if token in [SparqlParser.INTEGER_POSITIVE, SparqlParser.DECIMAL_POSITIVE, SparqlParser.DOUBLE_POSITIVE]:
                self.state = 1080
                self.numericLiteralPositive()

            elif token in [SparqlParser.INTEGER_NEGATIVE, SparqlParser.DECIMAL_NEGATIVE, SparqlParser.DOUBLE_NEGATIVE]:
                self.state = 1081
                self.numericLiteralNegative()

            else:
                raise NoViableAltException(self)

            self.state = 1086
            la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
            if la_ == 1:
                self.state = 1084
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==SparqlParser.ASTERISK or _la==SparqlParser.DIVIDE):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 1085
                self.unaryExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.UnaryExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def primaryExpression(self):
            return self.getTypedRuleContext(SparqlParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_unaryExpression

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitUnaryExpression(self)




    def unaryExpression(self):

        localctx = SparqlParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_unaryExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1089
            _la = self._input.LA(1)
            if ((((_la - 151)) & ~0x3f) == 0 and ((1 << (_la - 151)) & ((1 << (SparqlParser.PLUS_SIGN - 151)) | (1 << (SparqlParser.MINUS_SIGN - 151)) | (1 << (SparqlParser.NEGATION - 151)))) != 0):
                self.state = 1088
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 151)) & ~0x3f) == 0 and ((1 << (_la - 151)) & ((1 << (SparqlParser.PLUS_SIGN - 151)) | (1 << (SparqlParser.MINUS_SIGN - 151)) | (1 << (SparqlParser.NEGATION - 151)))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()


            self.state = 1091
            self.primaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PrimaryExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def builtInCall(self):
            return self.getTypedRuleContext(SparqlParser.BuiltInCallContext,0)


        def iriRefOrFunction(self):
            return self.getTypedRuleContext(SparqlParser.IriRefOrFunctionContext,0)


        def rdfLiteral(self):
            return self.getTypedRuleContext(SparqlParser.RdfLiteralContext,0)


        def numericLiteral(self):
            return self.getTypedRuleContext(SparqlParser.NumericLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(SparqlParser.BooleanLiteralContext,0)


        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_primaryExpression

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPrimaryExpression(self)




    def primaryExpression(self):

        localctx = SparqlParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_primaryExpression)
        try:
            self.state = 1103
            token = self._input.LA(1)
            if token in [SparqlParser.OPEN_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1093
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1094
                self.expression(0)
                self.state = 1095
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STR, SparqlParser.LANG, SparqlParser.LANGMATCHES, SparqlParser.DATATYPE, SparqlParser.BOUND, SparqlParser.SAMETERM, SparqlParser.ISIRI, SparqlParser.ISURI, SparqlParser.ISBLANK, SparqlParser.ISLITERAL, SparqlParser.REGEX, SparqlParser.SUBSTR, SparqlParser.IRI, SparqlParser.URI, SparqlParser.BNODE, SparqlParser.RAND, SparqlParser.ABS, SparqlParser.CEIL, SparqlParser.FLOOR, SparqlParser.ROUND, SparqlParser.CONCAT, SparqlParser.STRLEN, SparqlParser.UCASE, SparqlParser.LCASE, SparqlParser.ENCODE_FOR_URI, SparqlParser.CONTAINS, SparqlParser.STRSTARTS, SparqlParser.STRENDS, SparqlParser.STRBEFORE, SparqlParser.STRAFTER, SparqlParser.REPLACE, SparqlParser.YEAR, SparqlParser.MONTH, SparqlParser.DAY, SparqlParser.HOURS, SparqlParser.MINUTES, SparqlParser.SECONDS, SparqlParser.TIMEZONE, SparqlParser.TZ, SparqlParser.NOW, SparqlParser.UUID, SparqlParser.STRUUID, SparqlParser.MD5, SparqlParser.SHA1, SparqlParser.SHA256, SparqlParser.SHA384, SparqlParser.SHA512, SparqlParser.COALESCE, SparqlParser.IF, SparqlParser.STRLANG, SparqlParser.STRDT, SparqlParser.ISNUMERIC, SparqlParser.COUNT, SparqlParser.SUM, SparqlParser.MIN, SparqlParser.MAX, SparqlParser.AVG, SparqlParser.SAMPLE, SparqlParser.GROUP_CONCAT, SparqlParser.NOT, SparqlParser.EXISTS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1097
                self.builtInCall()

            elif token in [SparqlParser.IRIREF, SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1098
                self.iriRefOrFunction()

            elif token in [SparqlParser.STRING_LITERAL1, SparqlParser.STRING_LITERAL2, SparqlParser.STRING_LITERAL_LONG1, SparqlParser.STRING_LITERAL_LONG2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1099
                self.rdfLiteral()

            elif token in [SparqlParser.INTEGER, SparqlParser.DECIMAL, SparqlParser.DOUBLE, SparqlParser.INTEGER_POSITIVE, SparqlParser.DECIMAL_POSITIVE, SparqlParser.DOUBLE_POSITIVE, SparqlParser.INTEGER_NEGATIVE, SparqlParser.DECIMAL_NEGATIVE, SparqlParser.DOUBLE_NEGATIVE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1100
                self.numericLiteral()

            elif token in [SparqlParser.TRUE, SparqlParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1101
                self.booleanLiteral()

            elif token in [SparqlParser.VAR1, SparqlParser.VAR2]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1102
                self.var()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BuiltInCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.BuiltInCallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def aggregate(self):
            return self.getTypedRuleContext(SparqlParser.AggregateContext,0)


        def STR(self):
            return self.getToken(SparqlParser.STR, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def LANG(self):
            return self.getToken(SparqlParser.LANG, 0)

        def LANGMATCHES(self):
            return self.getToken(SparqlParser.LANGMATCHES, 0)

        def DATATYPE(self):
            return self.getToken(SparqlParser.DATATYPE, 0)

        def BOUND(self):
            return self.getToken(SparqlParser.BOUND, 0)

        def var(self):
            return self.getTypedRuleContext(SparqlParser.VarContext,0)


        def IRI(self):
            return self.getToken(SparqlParser.IRI, 0)

        def URI(self):
            return self.getToken(SparqlParser.URI, 0)

        def BNODE(self):
            return self.getToken(SparqlParser.BNODE, 0)

        def RAND(self):
            return self.getToken(SparqlParser.RAND, 0)

        def ABS(self):
            return self.getToken(SparqlParser.ABS, 0)

        def CEIL(self):
            return self.getToken(SparqlParser.CEIL, 0)

        def FLOOR(self):
            return self.getToken(SparqlParser.FLOOR, 0)

        def ROUND(self):
            return self.getToken(SparqlParser.ROUND, 0)

        def CONCAT(self):
            return self.getToken(SparqlParser.CONCAT, 0)

        def expressionList(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionListContext,0)


        def subStringExpression(self):
            return self.getTypedRuleContext(SparqlParser.SubStringExpressionContext,0)


        def STRLEN(self):
            return self.getToken(SparqlParser.STRLEN, 0)

        def strReplaceExpression(self):
            return self.getTypedRuleContext(SparqlParser.StrReplaceExpressionContext,0)


        def UCASE(self):
            return self.getToken(SparqlParser.UCASE, 0)

        def LCASE(self):
            return self.getToken(SparqlParser.LCASE, 0)

        def ENCODE_FOR_URI(self):
            return self.getToken(SparqlParser.ENCODE_FOR_URI, 0)

        def CONTAINS(self):
            return self.getToken(SparqlParser.CONTAINS, 0)

        def STRSTARTS(self):
            return self.getToken(SparqlParser.STRSTARTS, 0)

        def STRENDS(self):
            return self.getToken(SparqlParser.STRENDS, 0)

        def STRBEFORE(self):
            return self.getToken(SparqlParser.STRBEFORE, 0)

        def STRAFTER(self):
            return self.getToken(SparqlParser.STRAFTER, 0)

        def YEAR(self):
            return self.getToken(SparqlParser.YEAR, 0)

        def MONTH(self):
            return self.getToken(SparqlParser.MONTH, 0)

        def DAY(self):
            return self.getToken(SparqlParser.DAY, 0)

        def HOURS(self):
            return self.getToken(SparqlParser.HOURS, 0)

        def MINUTES(self):
            return self.getToken(SparqlParser.MINUTES, 0)

        def SECONDS(self):
            return self.getToken(SparqlParser.SECONDS, 0)

        def TIMEZONE(self):
            return self.getToken(SparqlParser.TIMEZONE, 0)

        def TZ(self):
            return self.getToken(SparqlParser.TZ, 0)

        def NOW(self):
            return self.getToken(SparqlParser.NOW, 0)

        def UUID(self):
            return self.getToken(SparqlParser.UUID, 0)

        def STRUUID(self):
            return self.getToken(SparqlParser.STRUUID, 0)

        def MD5(self):
            return self.getToken(SparqlParser.MD5, 0)

        def SHA1(self):
            return self.getToken(SparqlParser.SHA1, 0)

        def SHA256(self):
            return self.getToken(SparqlParser.SHA256, 0)

        def SHA384(self):
            return self.getToken(SparqlParser.SHA384, 0)

        def SHA512(self):
            return self.getToken(SparqlParser.SHA512, 0)

        def COALESCE(self):
            return self.getToken(SparqlParser.COALESCE, 0)

        def IF(self):
            return self.getToken(SparqlParser.IF, 0)

        def STRLANG(self):
            return self.getToken(SparqlParser.STRLANG, 0)

        def STRDT(self):
            return self.getToken(SparqlParser.STRDT, 0)

        def SAMETERM(self):
            return self.getToken(SparqlParser.SAMETERM, 0)

        def ISIRI(self):
            return self.getToken(SparqlParser.ISIRI, 0)

        def ISURI(self):
            return self.getToken(SparqlParser.ISURI, 0)

        def ISBLANK(self):
            return self.getToken(SparqlParser.ISBLANK, 0)

        def ISLITERAL(self):
            return self.getToken(SparqlParser.ISLITERAL, 0)

        def ISNUMERIC(self):
            return self.getToken(SparqlParser.ISNUMERIC, 0)

        def regexExpression(self):
            return self.getTypedRuleContext(SparqlParser.RegexExpressionContext,0)


        def existsFunction(self):
            return self.getTypedRuleContext(SparqlParser.ExistsFunctionContext,0)


        def notExistsFunction(self):
            return self.getTypedRuleContext(SparqlParser.NotExistsFunctionContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_builtInCall

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterBuiltInCall(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitBuiltInCall(self)




    def builtInCall(self):

        localctx = SparqlParser.BuiltInCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_builtInCall)
        self._la = 0 # Token type
        try:
            self.state = 1373
            token = self._input.LA(1)
            if token in [SparqlParser.COUNT, SparqlParser.SUM, SparqlParser.MIN, SparqlParser.MAX, SparqlParser.AVG, SparqlParser.SAMPLE, SparqlParser.GROUP_CONCAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1105
                self.aggregate()

            elif token in [SparqlParser.STR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1106
                self.match(SparqlParser.STR)
                self.state = 1107
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1108
                self.expression(0)
                self.state = 1109
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.LANG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1111
                self.match(SparqlParser.LANG)
                self.state = 1112
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1113
                self.expression(0)
                self.state = 1114
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.LANGMATCHES]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1116
                self.match(SparqlParser.LANGMATCHES)
                self.state = 1117
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1118
                self.expression(0)
                self.state = 1119
                self.match(SparqlParser.COMMA)
                self.state = 1120
                self.expression(0)
                self.state = 1121
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.DATATYPE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1123
                self.match(SparqlParser.DATATYPE)
                self.state = 1124
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1125
                self.expression(0)
                self.state = 1126
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.BOUND]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1128
                self.match(SparqlParser.BOUND)
                self.state = 1129
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1130
                self.var()
                self.state = 1131
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.IRI]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1133
                self.match(SparqlParser.IRI)
                self.state = 1134
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1135
                self.expression(0)
                self.state = 1136
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.URI]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1138
                self.match(SparqlParser.URI)
                self.state = 1139
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1140
                self.expression(0)
                self.state = 1141
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.BNODE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1143
                self.match(SparqlParser.BNODE)
                self.state = 1144
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1146
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SparqlParser.STR) | (1 << SparqlParser.LANG) | (1 << SparqlParser.LANGMATCHES) | (1 << SparqlParser.DATATYPE) | (1 << SparqlParser.BOUND) | (1 << SparqlParser.SAMETERM) | (1 << SparqlParser.ISIRI) | (1 << SparqlParser.ISURI) | (1 << SparqlParser.ISBLANK) | (1 << SparqlParser.ISLITERAL) | (1 << SparqlParser.REGEX) | (1 << SparqlParser.SUBSTR) | (1 << SparqlParser.TRUE) | (1 << SparqlParser.FALSE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SparqlParser.IRI - 64)) | (1 << (SparqlParser.URI - 64)) | (1 << (SparqlParser.BNODE - 64)) | (1 << (SparqlParser.RAND - 64)) | (1 << (SparqlParser.ABS - 64)) | (1 << (SparqlParser.CEIL - 64)) | (1 << (SparqlParser.FLOOR - 64)) | (1 << (SparqlParser.ROUND - 64)) | (1 << (SparqlParser.CONCAT - 64)) | (1 << (SparqlParser.STRLEN - 64)) | (1 << (SparqlParser.UCASE - 64)) | (1 << (SparqlParser.LCASE - 64)) | (1 << (SparqlParser.ENCODE_FOR_URI - 64)) | (1 << (SparqlParser.CONTAINS - 64)) | (1 << (SparqlParser.STRSTARTS - 64)) | (1 << (SparqlParser.STRENDS - 64)) | (1 << (SparqlParser.STRBEFORE - 64)) | (1 << (SparqlParser.STRAFTER - 64)) | (1 << (SparqlParser.REPLACE - 64)) | (1 << (SparqlParser.YEAR - 64)) | (1 << (SparqlParser.MONTH - 64)) | (1 << (SparqlParser.DAY - 64)) | (1 << (SparqlParser.HOURS - 64)) | (1 << (SparqlParser.MINUTES - 64)) | (1 << (SparqlParser.SECONDS - 64)) | (1 << (SparqlParser.TIMEZONE - 64)) | (1 << (SparqlParser.TZ - 64)) | (1 << (SparqlParser.NOW - 64)) | (1 << (SparqlParser.UUID - 64)) | (1 << (SparqlParser.STRUUID - 64)) | (1 << (SparqlParser.MD5 - 64)) | (1 << (SparqlParser.SHA1 - 64)) | (1 << (SparqlParser.SHA256 - 64)) | (1 << (SparqlParser.SHA384 - 64)) | (1 << (SparqlParser.SHA512 - 64)) | (1 << (SparqlParser.COALESCE - 64)) | (1 << (SparqlParser.IF - 64)) | (1 << (SparqlParser.STRLANG - 64)) | (1 << (SparqlParser.STRDT - 64)) | (1 << (SparqlParser.ISNUMERIC - 64)) | (1 << (SparqlParser.COUNT - 64)) | (1 << (SparqlParser.SUM - 64)) | (1 << (SparqlParser.MIN - 64)) | (1 << (SparqlParser.MAX - 64)) | (1 << (SparqlParser.AVG - 64)) | (1 << (SparqlParser.SAMPLE - 64)) | (1 << (SparqlParser.GROUP_CONCAT - 64)) | (1 << (SparqlParser.NOT - 64)) | (1 << (SparqlParser.EXISTS - 64)) | (1 << (SparqlParser.IRIREF - 64)) | (1 << (SparqlParser.PNAME_NS - 64)) | (1 << (SparqlParser.PNAME_LN - 64)) | (1 << (SparqlParser.VAR1 - 64)) | (1 << (SparqlParser.VAR2 - 64)) | (1 << (SparqlParser.INTEGER - 64)) | (1 << (SparqlParser.DECIMAL - 64)) | (1 << (SparqlParser.DOUBLE - 64)) | (1 << (SparqlParser.INTEGER_POSITIVE - 64)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 64)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (SparqlParser.INTEGER_NEGATIVE - 128)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 128)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 128)) | (1 << (SparqlParser.STRING_LITERAL1 - 128)) | (1 << (SparqlParser.STRING_LITERAL2 - 128)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 128)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 128)) | (1 << (SparqlParser.OPEN_BRACE - 128)) | (1 << (SparqlParser.PLUS_SIGN - 128)) | (1 << (SparqlParser.MINUS_SIGN - 128)) | (1 << (SparqlParser.ASTERISK - 128)) | (1 << (SparqlParser.NEGATION - 128)) | (1 << (SparqlParser.DIVIDE - 128)))) != 0):
                    self.state = 1145
                    self.expression(0)


                self.state = 1148
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.RAND]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1149
                self.match(SparqlParser.RAND)
                self.state = 1150
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1151
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.ABS]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1152
                self.match(SparqlParser.ABS)
                self.state = 1153
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1154
                self.expression(0)
                self.state = 1155
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.CEIL]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1157
                self.match(SparqlParser.CEIL)
                self.state = 1158
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1159
                self.expression(0)
                self.state = 1160
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.FLOOR]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1162
                self.match(SparqlParser.FLOOR)
                self.state = 1163
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1164
                self.expression(0)
                self.state = 1165
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.ROUND]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1167
                self.match(SparqlParser.ROUND)
                self.state = 1168
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1169
                self.expression(0)
                self.state = 1170
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.CONCAT]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1172
                self.match(SparqlParser.CONCAT)
                self.state = 1173
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1175
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SparqlParser.STR) | (1 << SparqlParser.LANG) | (1 << SparqlParser.LANGMATCHES) | (1 << SparqlParser.DATATYPE) | (1 << SparqlParser.BOUND) | (1 << SparqlParser.SAMETERM) | (1 << SparqlParser.ISIRI) | (1 << SparqlParser.ISURI) | (1 << SparqlParser.ISBLANK) | (1 << SparqlParser.ISLITERAL) | (1 << SparqlParser.REGEX) | (1 << SparqlParser.SUBSTR) | (1 << SparqlParser.TRUE) | (1 << SparqlParser.FALSE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SparqlParser.IRI - 64)) | (1 << (SparqlParser.URI - 64)) | (1 << (SparqlParser.BNODE - 64)) | (1 << (SparqlParser.RAND - 64)) | (1 << (SparqlParser.ABS - 64)) | (1 << (SparqlParser.CEIL - 64)) | (1 << (SparqlParser.FLOOR - 64)) | (1 << (SparqlParser.ROUND - 64)) | (1 << (SparqlParser.CONCAT - 64)) | (1 << (SparqlParser.STRLEN - 64)) | (1 << (SparqlParser.UCASE - 64)) | (1 << (SparqlParser.LCASE - 64)) | (1 << (SparqlParser.ENCODE_FOR_URI - 64)) | (1 << (SparqlParser.CONTAINS - 64)) | (1 << (SparqlParser.STRSTARTS - 64)) | (1 << (SparqlParser.STRENDS - 64)) | (1 << (SparqlParser.STRBEFORE - 64)) | (1 << (SparqlParser.STRAFTER - 64)) | (1 << (SparqlParser.REPLACE - 64)) | (1 << (SparqlParser.YEAR - 64)) | (1 << (SparqlParser.MONTH - 64)) | (1 << (SparqlParser.DAY - 64)) | (1 << (SparqlParser.HOURS - 64)) | (1 << (SparqlParser.MINUTES - 64)) | (1 << (SparqlParser.SECONDS - 64)) | (1 << (SparqlParser.TIMEZONE - 64)) | (1 << (SparqlParser.TZ - 64)) | (1 << (SparqlParser.NOW - 64)) | (1 << (SparqlParser.UUID - 64)) | (1 << (SparqlParser.STRUUID - 64)) | (1 << (SparqlParser.MD5 - 64)) | (1 << (SparqlParser.SHA1 - 64)) | (1 << (SparqlParser.SHA256 - 64)) | (1 << (SparqlParser.SHA384 - 64)) | (1 << (SparqlParser.SHA512 - 64)) | (1 << (SparqlParser.COALESCE - 64)) | (1 << (SparqlParser.IF - 64)) | (1 << (SparqlParser.STRLANG - 64)) | (1 << (SparqlParser.STRDT - 64)) | (1 << (SparqlParser.ISNUMERIC - 64)) | (1 << (SparqlParser.COUNT - 64)) | (1 << (SparqlParser.SUM - 64)) | (1 << (SparqlParser.MIN - 64)) | (1 << (SparqlParser.MAX - 64)) | (1 << (SparqlParser.AVG - 64)) | (1 << (SparqlParser.SAMPLE - 64)) | (1 << (SparqlParser.GROUP_CONCAT - 64)) | (1 << (SparqlParser.NOT - 64)) | (1 << (SparqlParser.EXISTS - 64)) | (1 << (SparqlParser.IRIREF - 64)) | (1 << (SparqlParser.PNAME_NS - 64)) | (1 << (SparqlParser.PNAME_LN - 64)) | (1 << (SparqlParser.VAR1 - 64)) | (1 << (SparqlParser.VAR2 - 64)) | (1 << (SparqlParser.INTEGER - 64)) | (1 << (SparqlParser.DECIMAL - 64)) | (1 << (SparqlParser.DOUBLE - 64)) | (1 << (SparqlParser.INTEGER_POSITIVE - 64)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 64)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (SparqlParser.INTEGER_NEGATIVE - 128)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 128)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 128)) | (1 << (SparqlParser.STRING_LITERAL1 - 128)) | (1 << (SparqlParser.STRING_LITERAL2 - 128)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 128)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 128)) | (1 << (SparqlParser.OPEN_BRACE - 128)) | (1 << (SparqlParser.PLUS_SIGN - 128)) | (1 << (SparqlParser.MINUS_SIGN - 128)) | (1 << (SparqlParser.ASTERISK - 128)) | (1 << (SparqlParser.NEGATION - 128)) | (1 << (SparqlParser.DIVIDE - 128)))) != 0):
                    self.state = 1174
                    self.expressionList()


                self.state = 1177
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.SUBSTR]:
                self.enterOuterAlt(localctx, 16)
                self.state = 1178
                self.subStringExpression()

            elif token in [SparqlParser.STRLEN]:
                self.enterOuterAlt(localctx, 17)
                self.state = 1179
                self.match(SparqlParser.STRLEN)
                self.state = 1180
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1181
                self.expression(0)
                self.state = 1182
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.REPLACE]:
                self.enterOuterAlt(localctx, 18)
                self.state = 1184
                self.strReplaceExpression()

            elif token in [SparqlParser.UCASE]:
                self.enterOuterAlt(localctx, 19)
                self.state = 1185
                self.match(SparqlParser.UCASE)
                self.state = 1186
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1187
                self.expression(0)
                self.state = 1188
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.LCASE]:
                self.enterOuterAlt(localctx, 20)
                self.state = 1190
                self.match(SparqlParser.LCASE)
                self.state = 1191
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1192
                self.expression(0)
                self.state = 1193
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.ENCODE_FOR_URI]:
                self.enterOuterAlt(localctx, 21)
                self.state = 1195
                self.match(SparqlParser.ENCODE_FOR_URI)
                self.state = 1196
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1197
                self.expression(0)
                self.state = 1198
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.CONTAINS]:
                self.enterOuterAlt(localctx, 22)
                self.state = 1200
                self.match(SparqlParser.CONTAINS)
                self.state = 1201
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1202
                self.expression(0)
                self.state = 1203
                self.match(SparqlParser.COMMA)
                self.state = 1204
                self.expression(0)
                self.state = 1205
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STRSTARTS]:
                self.enterOuterAlt(localctx, 23)
                self.state = 1207
                self.match(SparqlParser.STRSTARTS)
                self.state = 1208
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1209
                self.expression(0)
                self.state = 1210
                self.match(SparqlParser.COMMA)
                self.state = 1211
                self.expression(0)
                self.state = 1212
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STRENDS]:
                self.enterOuterAlt(localctx, 24)
                self.state = 1214
                self.match(SparqlParser.STRENDS)
                self.state = 1215
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1216
                self.expression(0)
                self.state = 1217
                self.match(SparqlParser.COMMA)
                self.state = 1218
                self.expression(0)
                self.state = 1219
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STRBEFORE]:
                self.enterOuterAlt(localctx, 25)
                self.state = 1221
                self.match(SparqlParser.STRBEFORE)
                self.state = 1222
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1223
                self.expression(0)
                self.state = 1224
                self.match(SparqlParser.COMMA)
                self.state = 1225
                self.expression(0)
                self.state = 1226
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STRAFTER]:
                self.enterOuterAlt(localctx, 26)
                self.state = 1228
                self.match(SparqlParser.STRAFTER)
                self.state = 1229
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1230
                self.expression(0)
                self.state = 1231
                self.match(SparqlParser.COMMA)
                self.state = 1232
                self.expression(0)
                self.state = 1233
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.YEAR]:
                self.enterOuterAlt(localctx, 27)
                self.state = 1235
                self.match(SparqlParser.YEAR)
                self.state = 1236
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1237
                self.expression(0)
                self.state = 1238
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.MONTH]:
                self.enterOuterAlt(localctx, 28)
                self.state = 1240
                self.match(SparqlParser.MONTH)
                self.state = 1241
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1242
                self.expression(0)
                self.state = 1243
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.DAY]:
                self.enterOuterAlt(localctx, 29)
                self.state = 1245
                self.match(SparqlParser.DAY)
                self.state = 1246
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1247
                self.expression(0)
                self.state = 1248
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.HOURS]:
                self.enterOuterAlt(localctx, 30)
                self.state = 1250
                self.match(SparqlParser.HOURS)
                self.state = 1251
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1252
                self.expression(0)
                self.state = 1253
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.MINUTES]:
                self.enterOuterAlt(localctx, 31)
                self.state = 1255
                self.match(SparqlParser.MINUTES)
                self.state = 1256
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1257
                self.expression(0)
                self.state = 1258
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.SECONDS]:
                self.enterOuterAlt(localctx, 32)
                self.state = 1260
                self.match(SparqlParser.SECONDS)
                self.state = 1261
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1262
                self.expression(0)
                self.state = 1263
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.TIMEZONE]:
                self.enterOuterAlt(localctx, 33)
                self.state = 1265
                self.match(SparqlParser.TIMEZONE)
                self.state = 1266
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1267
                self.expression(0)
                self.state = 1268
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.TZ]:
                self.enterOuterAlt(localctx, 34)
                self.state = 1270
                self.match(SparqlParser.TZ)
                self.state = 1271
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1272
                self.expression(0)
                self.state = 1273
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.NOW]:
                self.enterOuterAlt(localctx, 35)
                self.state = 1275
                self.match(SparqlParser.NOW)
                self.state = 1276
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1277
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.UUID]:
                self.enterOuterAlt(localctx, 36)
                self.state = 1278
                self.match(SparqlParser.UUID)
                self.state = 1279
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1280
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STRUUID]:
                self.enterOuterAlt(localctx, 37)
                self.state = 1281
                self.match(SparqlParser.STRUUID)
                self.state = 1282
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1283
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.MD5]:
                self.enterOuterAlt(localctx, 38)
                self.state = 1284
                self.match(SparqlParser.MD5)
                self.state = 1285
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1286
                self.expression(0)
                self.state = 1287
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.SHA1]:
                self.enterOuterAlt(localctx, 39)
                self.state = 1289
                self.match(SparqlParser.SHA1)
                self.state = 1290
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1291
                self.expression(0)
                self.state = 1292
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.SHA256]:
                self.enterOuterAlt(localctx, 40)
                self.state = 1294
                self.match(SparqlParser.SHA256)
                self.state = 1295
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1296
                self.expression(0)
                self.state = 1297
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.SHA384]:
                self.enterOuterAlt(localctx, 41)
                self.state = 1299
                self.match(SparqlParser.SHA384)
                self.state = 1300
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1301
                self.expression(0)
                self.state = 1302
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.SHA512]:
                self.enterOuterAlt(localctx, 42)
                self.state = 1304
                self.match(SparqlParser.SHA512)
                self.state = 1305
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1306
                self.expression(0)
                self.state = 1307
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.COALESCE]:
                self.enterOuterAlt(localctx, 43)
                self.state = 1309
                self.match(SparqlParser.COALESCE)
                self.state = 1310
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1312
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SparqlParser.STR) | (1 << SparqlParser.LANG) | (1 << SparqlParser.LANGMATCHES) | (1 << SparqlParser.DATATYPE) | (1 << SparqlParser.BOUND) | (1 << SparqlParser.SAMETERM) | (1 << SparqlParser.ISIRI) | (1 << SparqlParser.ISURI) | (1 << SparqlParser.ISBLANK) | (1 << SparqlParser.ISLITERAL) | (1 << SparqlParser.REGEX) | (1 << SparqlParser.SUBSTR) | (1 << SparqlParser.TRUE) | (1 << SparqlParser.FALSE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SparqlParser.IRI - 64)) | (1 << (SparqlParser.URI - 64)) | (1 << (SparqlParser.BNODE - 64)) | (1 << (SparqlParser.RAND - 64)) | (1 << (SparqlParser.ABS - 64)) | (1 << (SparqlParser.CEIL - 64)) | (1 << (SparqlParser.FLOOR - 64)) | (1 << (SparqlParser.ROUND - 64)) | (1 << (SparqlParser.CONCAT - 64)) | (1 << (SparqlParser.STRLEN - 64)) | (1 << (SparqlParser.UCASE - 64)) | (1 << (SparqlParser.LCASE - 64)) | (1 << (SparqlParser.ENCODE_FOR_URI - 64)) | (1 << (SparqlParser.CONTAINS - 64)) | (1 << (SparqlParser.STRSTARTS - 64)) | (1 << (SparqlParser.STRENDS - 64)) | (1 << (SparqlParser.STRBEFORE - 64)) | (1 << (SparqlParser.STRAFTER - 64)) | (1 << (SparqlParser.REPLACE - 64)) | (1 << (SparqlParser.YEAR - 64)) | (1 << (SparqlParser.MONTH - 64)) | (1 << (SparqlParser.DAY - 64)) | (1 << (SparqlParser.HOURS - 64)) | (1 << (SparqlParser.MINUTES - 64)) | (1 << (SparqlParser.SECONDS - 64)) | (1 << (SparqlParser.TIMEZONE - 64)) | (1 << (SparqlParser.TZ - 64)) | (1 << (SparqlParser.NOW - 64)) | (1 << (SparqlParser.UUID - 64)) | (1 << (SparqlParser.STRUUID - 64)) | (1 << (SparqlParser.MD5 - 64)) | (1 << (SparqlParser.SHA1 - 64)) | (1 << (SparqlParser.SHA256 - 64)) | (1 << (SparqlParser.SHA384 - 64)) | (1 << (SparqlParser.SHA512 - 64)) | (1 << (SparqlParser.COALESCE - 64)) | (1 << (SparqlParser.IF - 64)) | (1 << (SparqlParser.STRLANG - 64)) | (1 << (SparqlParser.STRDT - 64)) | (1 << (SparqlParser.ISNUMERIC - 64)) | (1 << (SparqlParser.COUNT - 64)) | (1 << (SparqlParser.SUM - 64)) | (1 << (SparqlParser.MIN - 64)) | (1 << (SparqlParser.MAX - 64)) | (1 << (SparqlParser.AVG - 64)) | (1 << (SparqlParser.SAMPLE - 64)) | (1 << (SparqlParser.GROUP_CONCAT - 64)) | (1 << (SparqlParser.NOT - 64)) | (1 << (SparqlParser.EXISTS - 64)) | (1 << (SparqlParser.IRIREF - 64)) | (1 << (SparqlParser.PNAME_NS - 64)) | (1 << (SparqlParser.PNAME_LN - 64)) | (1 << (SparqlParser.VAR1 - 64)) | (1 << (SparqlParser.VAR2 - 64)) | (1 << (SparqlParser.INTEGER - 64)) | (1 << (SparqlParser.DECIMAL - 64)) | (1 << (SparqlParser.DOUBLE - 64)) | (1 << (SparqlParser.INTEGER_POSITIVE - 64)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 64)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (SparqlParser.INTEGER_NEGATIVE - 128)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 128)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 128)) | (1 << (SparqlParser.STRING_LITERAL1 - 128)) | (1 << (SparqlParser.STRING_LITERAL2 - 128)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 128)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 128)) | (1 << (SparqlParser.OPEN_BRACE - 128)) | (1 << (SparqlParser.PLUS_SIGN - 128)) | (1 << (SparqlParser.MINUS_SIGN - 128)) | (1 << (SparqlParser.ASTERISK - 128)) | (1 << (SparqlParser.NEGATION - 128)) | (1 << (SparqlParser.DIVIDE - 128)))) != 0):
                    self.state = 1311
                    self.expressionList()


                self.state = 1314
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.IF]:
                self.enterOuterAlt(localctx, 44)
                self.state = 1315
                self.match(SparqlParser.IF)
                self.state = 1316
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1317
                self.expression(0)
                self.state = 1318
                self.match(SparqlParser.COMMA)
                self.state = 1319
                self.expression(0)
                self.state = 1320
                self.match(SparqlParser.COMMA)
                self.state = 1321
                self.expression(0)
                self.state = 1322
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STRLANG]:
                self.enterOuterAlt(localctx, 45)
                self.state = 1324
                self.match(SparqlParser.STRLANG)
                self.state = 1325
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1326
                self.expression(0)
                self.state = 1327
                self.match(SparqlParser.COMMA)
                self.state = 1328
                self.expression(0)
                self.state = 1329
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.STRDT]:
                self.enterOuterAlt(localctx, 46)
                self.state = 1331
                self.match(SparqlParser.STRDT)
                self.state = 1332
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1333
                self.expression(0)
                self.state = 1334
                self.match(SparqlParser.COMMA)
                self.state = 1335
                self.expression(0)
                self.state = 1336
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.SAMETERM]:
                self.enterOuterAlt(localctx, 47)
                self.state = 1338
                self.match(SparqlParser.SAMETERM)
                self.state = 1339
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1340
                self.expression(0)
                self.state = 1341
                self.match(SparqlParser.COMMA)
                self.state = 1342
                self.expression(0)
                self.state = 1343
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.ISIRI]:
                self.enterOuterAlt(localctx, 48)
                self.state = 1345
                self.match(SparqlParser.ISIRI)
                self.state = 1346
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1347
                self.expression(0)
                self.state = 1348
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.ISURI]:
                self.enterOuterAlt(localctx, 49)
                self.state = 1350
                self.match(SparqlParser.ISURI)
                self.state = 1351
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1352
                self.expression(0)
                self.state = 1353
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.ISBLANK]:
                self.enterOuterAlt(localctx, 50)
                self.state = 1355
                self.match(SparqlParser.ISBLANK)
                self.state = 1356
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1357
                self.expression(0)
                self.state = 1358
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.ISLITERAL]:
                self.enterOuterAlt(localctx, 51)
                self.state = 1360
                self.match(SparqlParser.ISLITERAL)
                self.state = 1361
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1362
                self.expression(0)
                self.state = 1363
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.ISNUMERIC]:
                self.enterOuterAlt(localctx, 52)
                self.state = 1365
                self.match(SparqlParser.ISNUMERIC)
                self.state = 1366
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1367
                self.expression(0)
                self.state = 1368
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.REGEX]:
                self.enterOuterAlt(localctx, 53)
                self.state = 1370
                self.regexExpression()

            elif token in [SparqlParser.EXISTS]:
                self.enterOuterAlt(localctx, 54)
                self.state = 1371
                self.existsFunction()

            elif token in [SparqlParser.NOT]:
                self.enterOuterAlt(localctx, 55)
                self.state = 1372
                self.notExistsFunction()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegexExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.RegexExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def REGEX(self):
            return self.getToken(SparqlParser.REGEX, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_regexExpression

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterRegexExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitRegexExpression(self)




    def regexExpression(self):

        localctx = SparqlParser.RegexExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_regexExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1375
            self.match(SparqlParser.REGEX)
            self.state = 1376
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 1377
            self.expression(0)
            self.state = 1378
            self.match(SparqlParser.COMMA)
            self.state = 1379
            self.expression(0)
            self.state = 1382
            _la = self._input.LA(1)
            if _la==SparqlParser.COMMA:
                self.state = 1380
                self.match(SparqlParser.COMMA)
                self.state = 1381
                self.expression(0)


            self.state = 1384
            self.match(SparqlParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubStringExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.SubStringExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SUBSTR(self):
            return self.getToken(SparqlParser.SUBSTR, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_subStringExpression

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterSubStringExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitSubStringExpression(self)




    def subStringExpression(self):

        localctx = SparqlParser.SubStringExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_subStringExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1386
            self.match(SparqlParser.SUBSTR)
            self.state = 1387
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 1388
            self.expression(0)
            self.state = 1389
            self.match(SparqlParser.COMMA)
            self.state = 1390
            self.expression(0)
            self.state = 1393
            _la = self._input.LA(1)
            if _la==SparqlParser.COMMA:
                self.state = 1391
                self.match(SparqlParser.COMMA)
                self.state = 1392
                self.expression(0)


            self.state = 1395
            self.match(SparqlParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StrReplaceExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.StrReplaceExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def REPLACE(self):
            return self.getToken(SparqlParser.REPLACE, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SparqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SparqlParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SparqlParser.RULE_strReplaceExpression

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterStrReplaceExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitStrReplaceExpression(self)




    def strReplaceExpression(self):

        localctx = SparqlParser.StrReplaceExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_strReplaceExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1397
            self.match(SparqlParser.REPLACE)
            self.state = 1398
            self.match(SparqlParser.OPEN_BRACE)
            self.state = 1399
            self.expression(0)
            self.state = 1400
            self.match(SparqlParser.COMMA)
            self.state = 1401
            self.expression(0)
            self.state = 1402
            self.match(SparqlParser.COMMA)
            self.state = 1403
            self.expression(0)
            self.state = 1406
            _la = self._input.LA(1)
            if _la==SparqlParser.COMMA:
                self.state = 1404
                self.match(SparqlParser.COMMA)
                self.state = 1405
                self.expression(0)


            self.state = 1408
            self.match(SparqlParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExistsFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.ExistsFunctionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EXISTS(self):
            return self.getToken(SparqlParser.EXISTS, 0)

        def groupGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GroupGraphPatternContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_existsFunction

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterExistsFunction(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitExistsFunction(self)




    def existsFunction(self):

        localctx = SparqlParser.ExistsFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_existsFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1410
            self.match(SparqlParser.EXISTS)
            self.state = 1411
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NotExistsFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.NotExistsFunctionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(SparqlParser.NOT, 0)

        def EXISTS(self):
            return self.getToken(SparqlParser.EXISTS, 0)

        def groupGraphPattern(self):
            return self.getTypedRuleContext(SparqlParser.GroupGraphPatternContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_notExistsFunction

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterNotExistsFunction(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitNotExistsFunction(self)




    def notExistsFunction(self):

        localctx = SparqlParser.NotExistsFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_notExistsFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1413
            self.match(SparqlParser.NOT)
            self.state = 1414
            self.match(SparqlParser.EXISTS)
            self.state = 1415
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AggregateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.AggregateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COUNT(self):
            return self.getToken(SparqlParser.COUNT, 0)

        def ASTERISK(self):
            return self.getToken(SparqlParser.ASTERISK, 0)

        def expression(self):
            return self.getTypedRuleContext(SparqlParser.ExpressionContext,0)


        def DISTINCT(self):
            return self.getToken(SparqlParser.DISTINCT, 0)

        def SUM(self):
            return self.getToken(SparqlParser.SUM, 0)

        def MIN(self):
            return self.getToken(SparqlParser.MIN, 0)

        def MAX(self):
            return self.getToken(SparqlParser.MAX, 0)

        def AVG(self):
            return self.getToken(SparqlParser.AVG, 0)

        def SAMPLE(self):
            return self.getToken(SparqlParser.SAMPLE, 0)

        def GROUP_CONCAT(self):
            return self.getToken(SparqlParser.GROUP_CONCAT, 0)

        def SEPARATOR(self):
            return self.getToken(SparqlParser.SEPARATOR, 0)

        def string(self):
            return self.getTypedRuleContext(SparqlParser.StringContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_aggregate

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterAggregate(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitAggregate(self)




    def aggregate(self):

        localctx = SparqlParser.AggregateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_aggregate)
        self._la = 0 # Token type
        try:
            self.state = 1481
            token = self._input.LA(1)
            if token in [SparqlParser.COUNT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1417
                self.match(SparqlParser.COUNT)
                self.state = 1418
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1420
                _la = self._input.LA(1)
                if _la==SparqlParser.DISTINCT:
                    self.state = 1419
                    self.match(SparqlParser.DISTINCT)


                self.state = 1424
                la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
                if la_ == 1:
                    self.state = 1422
                    self.match(SparqlParser.ASTERISK)
                    pass

                elif la_ == 2:
                    self.state = 1423
                    self.expression(0)
                    pass


                self.state = 1426
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.SUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1427
                self.match(SparqlParser.SUM)
                self.state = 1428
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1430
                _la = self._input.LA(1)
                if _la==SparqlParser.DISTINCT:
                    self.state = 1429
                    self.match(SparqlParser.DISTINCT)


                self.state = 1432
                self.expression(0)
                self.state = 1433
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.MIN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1435
                self.match(SparqlParser.MIN)
                self.state = 1436
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1438
                _la = self._input.LA(1)
                if _la==SparqlParser.DISTINCT:
                    self.state = 1437
                    self.match(SparqlParser.DISTINCT)


                self.state = 1440
                self.expression(0)
                self.state = 1441
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.MAX]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1443
                self.match(SparqlParser.MAX)
                self.state = 1444
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1446
                _la = self._input.LA(1)
                if _la==SparqlParser.DISTINCT:
                    self.state = 1445
                    self.match(SparqlParser.DISTINCT)


                self.state = 1448
                self.expression(0)
                self.state = 1449
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.AVG]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1451
                self.match(SparqlParser.AVG)
                self.state = 1452
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1454
                _la = self._input.LA(1)
                if _la==SparqlParser.DISTINCT:
                    self.state = 1453
                    self.match(SparqlParser.DISTINCT)


                self.state = 1456
                self.expression(0)
                self.state = 1457
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.SAMPLE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1459
                self.match(SparqlParser.SAMPLE)
                self.state = 1460
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1462
                _la = self._input.LA(1)
                if _la==SparqlParser.DISTINCT:
                    self.state = 1461
                    self.match(SparqlParser.DISTINCT)


                self.state = 1464
                self.expression(0)
                self.state = 1465
                self.match(SparqlParser.CLOSE_BRACE)

            elif token in [SparqlParser.GROUP_CONCAT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1467
                self.match(SparqlParser.GROUP_CONCAT)
                self.state = 1468
                self.match(SparqlParser.OPEN_BRACE)
                self.state = 1470
                _la = self._input.LA(1)
                if _la==SparqlParser.DISTINCT:
                    self.state = 1469
                    self.match(SparqlParser.DISTINCT)


                self.state = 1472
                self.expression(0)
                self.state = 1477
                _la = self._input.LA(1)
                if _la==SparqlParser.SEMICOLON:
                    self.state = 1473
                    self.match(SparqlParser.SEMICOLON)
                    self.state = 1474
                    self.match(SparqlParser.SEPARATOR)
                    self.state = 1475
                    self.match(SparqlParser.EQUAL)
                    self.state = 1476
                    self.string()


                self.state = 1479
                self.match(SparqlParser.CLOSE_BRACE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IriRefOrFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.IriRefOrFunctionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def argList(self):
            return self.getTypedRuleContext(SparqlParser.ArgListContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_iriRefOrFunction

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterIriRefOrFunction(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitIriRefOrFunction(self)




    def iriRefOrFunction(self):

        localctx = SparqlParser.IriRefOrFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_iriRefOrFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1483
            self.iri()
            self.state = 1485
            la_ = self._interp.adaptivePredict(self._input,143,self._ctx)
            if la_ == 1:
                self.state = 1484
                self.argList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RdfLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.RdfLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(SparqlParser.StringContext,0)


        def LANGTAG(self):
            return self.getToken(SparqlParser.LANGTAG, 0)

        def iri(self):
            return self.getTypedRuleContext(SparqlParser.IriContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_rdfLiteral

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterRdfLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitRdfLiteral(self)




    def rdfLiteral(self):

        localctx = SparqlParser.RdfLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_rdfLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1487
            self.string()
            self.state = 1491
            la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
            if la_ == 1:
                self.state = 1488
                self.match(SparqlParser.LANGTAG)

            elif la_ == 2:
                self.state = 1489
                self.match(SparqlParser.REFERENCE)
                self.state = 1490
                self.iri()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.NumericLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def numericLiteralUnsigned(self):
            return self.getTypedRuleContext(SparqlParser.NumericLiteralUnsignedContext,0)


        def numericLiteralPositive(self):
            return self.getTypedRuleContext(SparqlParser.NumericLiteralPositiveContext,0)


        def numericLiteralNegative(self):
            return self.getTypedRuleContext(SparqlParser.NumericLiteralNegativeContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_numericLiteral

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitNumericLiteral(self)




    def numericLiteral(self):

        localctx = SparqlParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_numericLiteral)
        try:
            self.state = 1496
            token = self._input.LA(1)
            if token in [SparqlParser.INTEGER, SparqlParser.DECIMAL, SparqlParser.DOUBLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1493
                self.numericLiteralUnsigned()

            elif token in [SparqlParser.INTEGER_POSITIVE, SparqlParser.DECIMAL_POSITIVE, SparqlParser.DOUBLE_POSITIVE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1494
                self.numericLiteralPositive()

            elif token in [SparqlParser.INTEGER_NEGATIVE, SparqlParser.DECIMAL_NEGATIVE, SparqlParser.DOUBLE_NEGATIVE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1495
                self.numericLiteralNegative()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralUnsignedContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.NumericLiteralUnsignedContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(SparqlParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(SparqlParser.DECIMAL, 0)

        def DOUBLE(self):
            return self.getToken(SparqlParser.DOUBLE, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_numericLiteralUnsigned

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterNumericLiteralUnsigned(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitNumericLiteralUnsigned(self)




    def numericLiteralUnsigned(self):

        localctx = SparqlParser.NumericLiteralUnsignedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_numericLiteralUnsigned)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1498
            _la = self._input.LA(1)
            if not(((((_la - 122)) & ~0x3f) == 0 and ((1 << (_la - 122)) & ((1 << (SparqlParser.INTEGER - 122)) | (1 << (SparqlParser.DECIMAL - 122)) | (1 << (SparqlParser.DOUBLE - 122)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralPositiveContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.NumericLiteralPositiveContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_POSITIVE(self):
            return self.getToken(SparqlParser.INTEGER_POSITIVE, 0)

        def DECIMAL_POSITIVE(self):
            return self.getToken(SparqlParser.DECIMAL_POSITIVE, 0)

        def DOUBLE_POSITIVE(self):
            return self.getToken(SparqlParser.DOUBLE_POSITIVE, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_numericLiteralPositive

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterNumericLiteralPositive(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitNumericLiteralPositive(self)




    def numericLiteralPositive(self):

        localctx = SparqlParser.NumericLiteralPositiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_numericLiteralPositive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1500
            _la = self._input.LA(1)
            if not(((((_la - 125)) & ~0x3f) == 0 and ((1 << (_la - 125)) & ((1 << (SparqlParser.INTEGER_POSITIVE - 125)) | (1 << (SparqlParser.DECIMAL_POSITIVE - 125)) | (1 << (SparqlParser.DOUBLE_POSITIVE - 125)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericLiteralNegativeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.NumericLiteralNegativeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_NEGATIVE(self):
            return self.getToken(SparqlParser.INTEGER_NEGATIVE, 0)

        def DECIMAL_NEGATIVE(self):
            return self.getToken(SparqlParser.DECIMAL_NEGATIVE, 0)

        def DOUBLE_NEGATIVE(self):
            return self.getToken(SparqlParser.DOUBLE_NEGATIVE, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_numericLiteralNegative

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterNumericLiteralNegative(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitNumericLiteralNegative(self)




    def numericLiteralNegative(self):

        localctx = SparqlParser.NumericLiteralNegativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_numericLiteralNegative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1502
            _la = self._input.LA(1)
            if not(((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (SparqlParser.INTEGER_NEGATIVE - 128)) | (1 << (SparqlParser.DECIMAL_NEGATIVE - 128)) | (1 << (SparqlParser.DOUBLE_NEGATIVE - 128)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleanLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.BooleanLiteralContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(SparqlParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SparqlParser.FALSE, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_booleanLiteral

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitBooleanLiteral(self)




    def booleanLiteral(self):

        localctx = SparqlParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1504
            _la = self._input.LA(1)
            if not(_la==SparqlParser.TRUE or _la==SparqlParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.StringContext, self).__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL1(self):
            return self.getToken(SparqlParser.STRING_LITERAL1, 0)

        def STRING_LITERAL2(self):
            return self.getToken(SparqlParser.STRING_LITERAL2, 0)

        def STRING_LITERAL_LONG1(self):
            return self.getToken(SparqlParser.STRING_LITERAL_LONG1, 0)

        def STRING_LITERAL_LONG2(self):
            return self.getToken(SparqlParser.STRING_LITERAL_LONG2, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_string

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterString(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitString(self)




    def string(self):

        localctx = SparqlParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1506
            _la = self._input.LA(1)
            if not(((((_la - 131)) & ~0x3f) == 0 and ((1 << (_la - 131)) & ((1 << (SparqlParser.STRING_LITERAL1 - 131)) | (1 << (SparqlParser.STRING_LITERAL2 - 131)) | (1 << (SparqlParser.STRING_LITERAL_LONG1 - 131)) | (1 << (SparqlParser.STRING_LITERAL_LONG2 - 131)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IriContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.IriContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IRIREF(self):
            return self.getToken(SparqlParser.IRIREF, 0)

        def prefixedName(self):
            return self.getTypedRuleContext(SparqlParser.PrefixedNameContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_iri

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterIri(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitIri(self)




    def iri(self):

        localctx = SparqlParser.IriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_iri)
        try:
            self.state = 1510
            token = self._input.LA(1)
            if token in [SparqlParser.IRIREF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1508
                self.match(SparqlParser.IRIREF)

            elif token in [SparqlParser.PNAME_NS, SparqlParser.PNAME_LN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1509
                self.prefixedName()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrefixedNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.PrefixedNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PNAME_LN(self):
            return self.getToken(SparqlParser.PNAME_LN, 0)

        def PNAME_NS(self):
            return self.getToken(SparqlParser.PNAME_NS, 0)

        def getRuleIndex(self):
            return SparqlParser.RULE_prefixedName

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterPrefixedName(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitPrefixedName(self)




    def prefixedName(self):

        localctx = SparqlParser.PrefixedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_prefixedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1512
            _la = self._input.LA(1)
            if not(_la==SparqlParser.PNAME_NS or _la==SparqlParser.PNAME_LN):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlankNodeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.BlankNodeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLANK_NODE_LABEL(self):
            return self.getToken(SparqlParser.BLANK_NODE_LABEL, 0)

        def anon(self):
            return self.getTypedRuleContext(SparqlParser.AnonContext,0)


        def getRuleIndex(self):
            return SparqlParser.RULE_blankNode

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterBlankNode(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitBlankNode(self)




    def blankNode(self):

        localctx = SparqlParser.BlankNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_blankNode)
        try:
            self.state = 1516
            token = self._input.LA(1)
            if token in [SparqlParser.BLANK_NODE_LABEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1514
                self.match(SparqlParser.BLANK_NODE_LABEL)

            elif token in [SparqlParser.OPEN_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1515
                self.anon()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AnonContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SparqlParser.AnonContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SparqlParser.RULE_anon

        def enterRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.enterAnon(self)

        def exitRule(self, listener):
            if isinstance( listener, SparqlParserListener ):
                listener.exitAnon(self)




    def anon(self):

        localctx = SparqlParser.AnonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_anon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1518
            self.match(SparqlParser.OPEN_SQUARE_BRACKET)
            self.state = 1519
            self.match(SparqlParser.CLOSE_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[110] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




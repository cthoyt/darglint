# Generated on 2020-04-04 11:23:48.103239

from darglint.parse.grammar import (
    BaseGrammar,
    P,
)

from darglint.token import (
    TokenType,
)

from darglint.parse.identifiers import (
    NoqaIdentifier,
)

from darglint.errors import (
    EmptyDescriptionError,
)

class YieldsGrammar(BaseGrammar):
    productions = [
        P("yields-section", ([], "yhead", "yields-section1", 0), ([], "yhead-no-follow", "newlines", 0), ([EmptyDescriptionError], "colon", "yhead-no-follow1", 0), ([EmptyDescriptionError], "colon", "yhead-no-follow3", 0)),
        P("yield-type-section", (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.SEE, 0), (TokenType.ALSO, 0), (TokenType.NOTES, 0), (TokenType.EXAMPLES, 0), (TokenType.REFERENCES, 0), (TokenType.HEADER, 0)),
        P("yhead", ([], "colon", "yhead0", 0), ([], "colon", "yhead1", 0)),
        P("yhead-no-follow", ([EmptyDescriptionError], "colon", "yhead-no-follow1", 0), ([EmptyDescriptionError], "colon", "yhead-no-follow3", 0)),
        P("item-body", ([], "line", "item-body0", 0), ([], "line", "item-body1", 0), ([], "line", "item-body2", 0), ([], "word", "line", 0), ([], "word", "noqa-maybe", 0), ([NoqaIdentifier], "hash", "noqa", 0), ([NoqaIdentifier], "noqa-head", "noqa-statement1", 0), (TokenType.INDENT, 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.SEE, 0), (TokenType.ALSO, 0), (TokenType.NOTES, 0), (TokenType.EXAMPLES, 0), (TokenType.REFERENCES, 0), (TokenType.HEADER, 0)),
        P("block-indented", ([], "paragraph-indented", "block-indented0", 0), ([], "paragraph-indented", "block-indented1", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0)),
        P("split-indented", ([], "newline", "split-indented0", 0), (TokenType.NEWLINE, 0)),
        P("paragraph-indented", ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0)),
        P("indented", ([], "indent", "indents", 0), (TokenType.INDENT, 0)),
        P("line", ([], "word", "line", 0), ([], "word", "noqa-maybe", 0), ([NoqaIdentifier], "hash", "noqa", 0), ([NoqaIdentifier], "noqa-head", "noqa-statement1", 0), (TokenType.INDENT, 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.SEE, 0), (TokenType.ALSO, 0), (TokenType.NOTES, 0), (TokenType.EXAMPLES, 0), (TokenType.REFERENCES, 0), (TokenType.HEADER, 0)),
        P("indents", ([], "indent", "indents", 0), (TokenType.INDENT, 0)),
        P("split", ([], "newline", "split0", 0)),
        P("newlines", ([], "newline", "newlines", 0), (TokenType.NEWLINE, 0)),
        P("word", (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.SEE, 0), (TokenType.ALSO, 0), (TokenType.NOTES, 0), (TokenType.EXAMPLES, 0), (TokenType.REFERENCES, 0), (TokenType.HEADER, 0)),
        P("colon", (TokenType.COLON, 0)),
        P("hash", (TokenType.HASH, 0)),
        P("indent", (TokenType.INDENT, 0)),
        P("newline", (TokenType.NEWLINE, 0)),
        P("yields", (TokenType.YIELDS, 0)),
        P("noqa", (TokenType.NOQA, 0)),
        P("noqa-maybe", ([NoqaIdentifier], "hash", "noqa", 0), ([NoqaIdentifier], "noqa-head", "noqa-statement1", 0)),
        P("noqa-head", ([], "hash", "noqa", 0)),
        P("words", ([], "word", "words", 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.SEE, 0), (TokenType.ALSO, 0), (TokenType.NOTES, 0), (TokenType.EXAMPLES, 0), (TokenType.REFERENCES, 0), (TokenType.HEADER, 0)),
        P("yields-section1", ([], "item-body", "newlines", 0), ([], "line", "item-body0", 0), ([], "line", "item-body1", 0), ([], "line", "item-body2", 0), ([], "word", "line", 0), ([], "word", "noqa-maybe", 0), ([NoqaIdentifier], "hash", "noqa", 0), ([NoqaIdentifier], "noqa-head", "noqa-statement1", 0), (TokenType.INDENT, 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.SEE, 0), (TokenType.ALSO, 0), (TokenType.NOTES, 0), (TokenType.EXAMPLES, 0), (TokenType.REFERENCES, 0), (TokenType.HEADER, 0)),
        P("yhead0", ([], "yields", "colon", 0)),
        P("yhead1", ([], "yields", "yhead2", 0)),
        P("yhead2", ([], "yield-type-section", "colon", 0)),
        P("yhead-no-follow1", ([], "yields", "colon", 0)),
        P("yhead-no-follow3", ([], "yields", "yhead-no-follow4", 0)),
        P("yhead-no-follow4", ([], "yield-type-section", "colon", 0)),
        P("item-body0", ([], "newline", "block-indented", 0)),
        P("item-body1", ([], "newlines", "block-indented", 0), ([], "paragraph-indented", "block-indented0", 0), ([], "paragraph-indented", "block-indented1", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0)),
        P("item-body2", ([], "newline", "item-body3", 0)),
        P("item-body3", ([], "indent", "item-body4", 0)),
        P("item-body4", ([], "newline", "item-body5", 0)),
        P("item-body5", ([], "newlines", "block-indented", 0), ([], "paragraph-indented", "block-indented0", 0), ([], "paragraph-indented", "block-indented1", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0)),
        P("block-indented0", ([], "split", "block-indented", 0)),
        P("block-indented1", ([], "split-indented", "block-indented", 0)),
        P("split-indented0", ([], "indents", "newlines", 0), ([], "indent", "indents", 0), (TokenType.INDENT, 0), ([], "newline", "newlines", 0), (TokenType.NEWLINE, 0)),
        P("paragraph-indented0", ([], "line", "paragraph-indented1", 0)),
        P("paragraph-indented1", ([], "newline", "paragraph-indented", 0)),
        P("split0", ([], "newline", "newlines", 0), (TokenType.NEWLINE, 0)),
        P("noqa-statement1", ([], "colon", "words", 0)),
    ]
    start = "yields-section"
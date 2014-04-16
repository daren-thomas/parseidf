# This file is licensed under the terms of the MIT license. See the file
# "LICENSE" in the project root for more information.
#
# This module was developed by Daren Thomas at the assistant chair for
# Sustainable Architecture and Building Technologies (Suat) at the Institute of
# Technology in Architecture, ETH Zürich. See http://suat.arch.ethz.ch for
# more information.
'''
parseidf.py


parses an idf file into a dictionary of lists in the following manner:

    each idf object is represented by a list of its fields, with the first
    field being the objects type.

    each such list is appended to a list of objects with the same type in the
    dictionary, indexed by type:

    { [A] => [ [A, x, y, z], [A, a, b, c],
      [B] => [ [B, 1, 2], [B, 1, 2, 3] }

    also, all field values are strings, i.e. no interpretation of the values is
    made.
'''
import ply.lex as lex
import ply.yacc as yacc

# list of token names
tokens = ('VALUE',
          'COMMA',
          'SEMICOLON')

# regular expression rules for simple tokens
t_COMMA = r'[ \t]*,[ \t]*'
t_SEMICOLON = r'[ \t]*;[ \t]*'


# ignore comments, tracking line numbers at the same time
def t_COMMENT(t):
    r'[ \t\r\n]*!.*'
    newlines = [n for n in t.value if n == '\n']
    t.lineno += len(newlines)
    pass
    # No return value. Token discarded


# Define a rule so we can track line numbers
def t_newline(t):
    r'[ \t]*(\r?\n)+'
    t.lexer.lineno += len(t.value)


def t_VALUE(t):
    r'[ \t]*([^!,;\n]|[*])+[ \t]*'
    return t


# Error handling rule
def t_error(t):
    raise SyntaxError("Illegal character '%s' at line %d of input"
                      % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)


# define grammar of idf objects
def p_idffile(p):
    'idffile : idfobjectlist'
    result = {}
    for idfobject in p[1]:
        name = idfobject[0]
        result.setdefault(name.upper(), []).append(idfobject)
    p[0] = result


def p_idfobjectlist(p):
    'idfobjectlist : idfobject'
    p[0] = [p[1]]


def p_idfobjectlist_multiple(p):
    'idfobjectlist : idfobject idfobjectlist'
    p[0] = [p[1]] + p[2]


def p_idfobject(p):
    'idfobject : objectname SEMICOLON'
    p[0] = [p[1]]


def p_idfobject_with_values(p):
    'idfobject : objectname COMMA valuelist SEMICOLON'
    p[0] = [p[1]] + p[3]


def p_objectname(p):
    'objectname : VALUE'
    p[0] = p[1].strip()


def p_valuelist(p):
    'valuelist : VALUE'
    p[0] = [p[1].strip()]


def p_valuelist_multiple(p):
    'valuelist : VALUE COMMA valuelist'
    p[0] = [p[1].strip()] + p[3]


# oh, and handle errors
def p_error(p):
    raise SyntaxError("Syntax error in input on line %d" % lex.lexer.lineno)


def parse(input):
    '''
    parses a string with the contents of the idf file and returns the
    dictionary representation.
    '''
    lexer = lex.lex(debug=False)
    lexer.input(input)
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    return result

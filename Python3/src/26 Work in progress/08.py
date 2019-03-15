import pandas as pd
import os, sys
import ply.lex as lex
import ply.yacc as yacc



########################### LEXER ###########################
# Tokens

reserved = {
   'TITLE' : 'title'
}

tokens = ['LEFT_SQUARE_BRACKET', 'RIGHT_SQUARE_BRACKET', 'QUOTE', 'HEADINGS', 'NUMBER', 
          'SPACE', 'TYPE', 'LINE', 'END_ROW', 'BAR', 'BLANK_COL', 'NL']  + list(reserved.values())

t_SPACE = r"[ \t]+"

def t_LEFT_SQUARE_BRACKET(t):
    r"\["
    return t

def t_RIGHT_SQUARE_BRACKET(t):
    r"\]"
    return t

def t_QUOTE(t):
    r"'"
    return t

def t_HEADINGS(t):
    r"Number\|Section\|Question\|Type\|Option1\|Option2\|Option3\|Option4\|Option5\|Option6\|Option7\|Option8\|Option9"
    return t

def t_LINE(t):
    r"[^|~]+"
    return t

def t_BAR(t):
    r"[|]"
    return t
    
def t_TYPE(t):
    r'title'
    return t
    
def t_NL(t):
    r"~\n"
    return t
    
def t_error(t):
    print(f"{data[:t.lexpos]}")
    raise Exception(f"Illegal character {t.value[0]} at position {t.lexpos}")
#    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex(debug=False)


########################### PARSER ###########################

# each parsing function is of the form "p_*"
# p[0] = value to place in the LHS of BNF
# this will then be copied p[1], p[2], .. representing the RHS of BNF in higher rule

"""
spreadsheet: [ ' headings question* ' ]
question : part1 part2 part3 nl 
part1:    number section questionTitle type option1 blank*
part2:    blank* options nl
part3:    (blank{t} mark{t} nl | nl | (blank{t}* option{t}* nl)+)

"""

def p_spreadsheet(p):
    """    spreadsheet : headings blank_lines
    """
    print(sys._getframe().f_code.co_name)

def p_blanks(p):
    """ blanks : BAR blanks
               | BAR
    """
    print(sys._getframe().f_code.co_name, end=" ")

def p_blank_line(p):
    """ blank_line : blanks NL """
    print(sys._getframe().f_code.co_name)

def p_blank_lines(p):
    """ blank_lines : blank_line blank_lines
                    | blank_line
    """
    print(sys._getframe().f_code.co_name)
    
def p_headings(p):
    """ headings : HEADINGS NL
    """
    print(sys._getframe().f_code.co_name)
    p[0] = p[1]
    
def p_line(p):
    """ line : LINE """
    print(sys._getframe().f_code.co_name, end=" ")
    p[0] = p[1]
    
def p_number(p):
    """ number : LINE BAR """
    print(sys._getframe().f_code.co_name, end=" ")
    
def p_option1(p):
    """ option1 : blanks line blanks
                | blanks
    """
    print(sys._getframe().f_code.co_name, end=" ")

def p_options(p):
    """ options : line blanks NL
    """
    print(sys._getframe().f_code.co_name, end=" ")

def p_part1(p):
    """ part1 : question type option1 NL
    """
    print(sys._getframe().f_code.co_name)

def p_part2(p):
    """ part2 : blanks options NL
    """    
    print(sys._getframe().f_code.co_name, end=" ")

def p_part3(p):
    """
    part3 : blanks options NL
          | NL
    """
    print(sys._getframe().f_code.co_name, end=" ")

def p_question(p):
    """ question : BAR BAR questionTitle
                 | number section questionTitle
    """
    print(sys._getframe().f_code.co_name, end=" ")
    print(f".{p[3]}.")
    p[0] = p[3]
    
def p_questionBlocks(p):
    """ questionBlocks : questionBlock questionBlocks
                       | questionBlock
    """
    print(sys._getframe().f_code.co_name)

def p_questionBlock(p):
    """ questionBlock : blank_line 
    """
    print(sys._getframe().f_code.co_name)

def p_questionTitle(p):
    "questionTitle : line BAR" 
    print(sys._getframe().f_code.co_name, end=" ")
    p[0] = p[1] + p[2]

def p_section(p):
    """ section : LINE BAR """
    print(sys._getframe().f_code.co_name, end=" ")
    
def p_type(p):
    "type : line BAR"
    print(sys._getframe().f_code.co_name, end=" ")
    p[0] = p[1]
    
def p_error(p):
    print()
    print()
    print("Syntax error at '%s'" % p.value)
    print(f"{data[:p.lexpos]}")

parser = yacc.yacc()


########################### APPLICATION ###########################

os.chdir("datax")
excelFile = "highlands.xlsx"
pd.set_option('display.width', 1000)
table = pd.read_excel(excelFile, 'questions', converters={'Number':str})
table = table.drop(['Comments'], axis=1)
try:
    table = table.drop(['Important'], axis=1)
except:
    pass        # may have left this (unused) column in old spreadsheet
table[['Number']] = table[['Number']].fillna(value="")
table[['Section']] = table[['Section']].fillna(value="")

data = table.to_csv(None, sep="|", line_terminator="\n", header=True, index=False).split('\n')

s = "~\n".join(data[:3])
s += "~\n"
print(s)
parser.parse(s)

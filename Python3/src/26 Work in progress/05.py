import pandas as pd
import os
import ply.lex as lex
import ply.yacc as yacc



########################### LEXER ###########################
# Tokens

tokens = ('LEFT_SQUARE_BRACKET', 'HEADINGS', 'RIGHT_SQUARE_BRACKET', 'END_ROW', 'COL', 'BLANK_COL')

def t_LEFT_SQUARE_BRACKET(t):
    r"\[[']"
    return t

def t_RIGHT_SQUARE_BRACKET(t):
    r"[']\]"
    return t

def t_HEADINGS(t):
    r"Number\|Section\|Question\|Type\|Option1\|Option2\|Option3\|Option4\|Option5\|Option6\|Option7\|Option8\|Option9"
    return t

t_END_ROW = r"~"

def t_COL(t):
    r"[^|~]*[|]"
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

def p_full(p):
    """ spreadsheet : LEFT_SQUARE_BRACKET headings rows RIGHT_SQUARE_BRACKET"""
    p[0] = p[2] + p[3]
    print("Headings OK")

def p_headings(p):
    "headings : HEADINGS END_ROW"
    p[0] = p[1]

    
def p_rows(p):
    """ rows : row end_row
             | rows row end_row
    """
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_end_row(p):
    """ end_row : END_ROW """
    if Global.question != "|":
        if Global.isBlankLine:
            print(f"{Global.isBlankLine}:{Global.row}:{Global.question}:OK")
        else:
            print(f"{Global.isBlankLine}:{Global.row}:{Global.question}:FAIL")
    p[0] = p[1]
    
def p_row(p):
    """ row : row COL
            | COL
    """
    if len(p) == 3:
        p[0] = p[1] + p[2]
        Global.row = p[0]
        Global.isBlankLine = (Global.row == Global.blankLine)
    if len(p) == 2:
        p[0] = p[1]
        Global.previousQuestion = Global.question
        Global.question = p[1]

def p_error(p):
    print(f"{data[:p.lexpos]}")
    print("Syntax error at '%s'" % p.value)

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

s = """['Number,Section,Question,Type,Option1,Option2,Option3,Option4,Option5,Option6,Option7,Option8,Option9', ',,,,,,,,,,,,', ',,,,,,,,,,,,', ',,'"""
data = table.to_csv(None, sep="|", line_terminator="~", header=True, index=False).split('\n')
data = str(data)

class Global():
    blankLine = r"||||||||||||~"
    question = None
    isBlankLine = None
    row = None


    
print(data)
try:
    parser.parse(data, debug=False)
except Exception as e:
    print(e)
    

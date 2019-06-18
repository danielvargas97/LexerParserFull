tokens = ['NUMBER','PLUS','TIMES','MINUS','DIVI']

t_PLUS = r"\+"
t_TIMES = r"\*"
t_MINUS = r"\-"
t_DIVI = r"\/"

def t_NUMBER(token):
    r"\d+"
    token.value = int(token.value)
    return token

t_ignore_WHITESPACES = r"[ \t]+"

def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

def t_error(token):
    message = "Token desconocido:"
    message = "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

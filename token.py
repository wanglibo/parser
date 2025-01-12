from enum import Enum
from typing import List, Self

# Accept table at token level
#ACCEPT_NEXT = {
#    TokenType.SELECT: [TokenType.WORD, TokenType.NUMBER, TokenType.STAR],
#    TokenType.NUMBER: []
#}

class TokenType(Enum):
    # Basic elements
    WORD = 0
    NUMBER = 1
    # Symbols   
    DOT = 30
    COMMA = 31
    SEMICOLON = 32
    EQUALS = 33
    GREATER_THAN = 34
    LESS_THAN = 35
    GREATER_THAN_OR_EQUAL = 36
    LESS_THAN_OR_EQUAL = 37
    NOT_EQUAL = 38
    OPEN_PAREN = 39
    CLOSE_PAREN = 40
    # OPEN_BRACKET = 41   
    # CLOSE_BRACKET = 42
    # OPEN_BRACE = 43
    # CLOSE_BRACE = 44
    PLUS = 45
    MINUS = 46
    STAR = 47  # Map to both select * and a * b
    DIVIDE = 48
    MODULO = 49
    # Keywords
    SELECT = 101
    FROM = 102
    WHERE = 103
    AND = 104
    OR = 105
    NOT = 106
    JOIN = 107
    LEFT = 108
    RIGHT = 109
    INNER = 110
    OUTER = 111
    ON = 112
    USING = 113
    GROUP = 114
    BY = 115
    ORDER = 116
    ASC = 117
    DESC = 118
    LIMIT = 119
    OFFSET = 120
    AS = 121
    IN = 122
    IS = 123
    NULL = 124
    TRUE = 125
    FALSE = 126
    DEFINE = 127
    TABLE = 128
    CREATE = 129
    CASE = 130
    WHEN = 131
    END = 132
    ALL = 133
    EXISTS = 134
    ANY = 135
    LIKE = 136
    SOME = 137
    # Functions
    AVG = 201
    SUM = 202
    COUNT = 203
    MAX = 204
    MIN = 205


# This is incomplete yet
TOKEN_STRING_TO_TYPE = {
    'select': TokenType.SELECT,
    'from': TokenType.FROM,
    'where': TokenType.WHERE,
    '.': TokenType.DOT,
    ';': TokenType.SEMICOLON,
    '=': TokenType.EQUALS,
    '<': TokenType.LESS_THAN,
    '<=': TokenType.LESS_THAN_OR_EQUAL,
    'and': TokenType.AND,
}

def infer_token_type(s : str) -> TokenType:       
    s = s.lower()
    if s in TOKEN_STRING_TO_TYPE:
        return TOKEN_STRING_TO_TYPE[s]
    elif s.isdigit():
        return TokenType.NUMBER
    return TokenType.WORD

# Represents a token in the query
class Token:

    type: TokenType
    value: str

    def __init__(self, segment: str) -> None:
        self.type = infer_token_type(segment)
        self.value = None
        if self.type == TokenType.WORD or self.type == TokenType.NUMBER:
            self.value = segment

    def __repr__(self):
        return f'Token({self.type}' + (f', {self.value}' if self.value else '') + ')'


    #def accept(self, next_token: Self) -> bool:
    #    return self.type in ACCEPT_NEXT and next_token in ACCEPT_NEXT[self.type]
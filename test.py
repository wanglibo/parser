from token import Token
from typing import List

SINGLE_CHAR_OPERATORS='.,;=()+-*/%'

def isSymbol(char: str) -> bool:
    return char in SINGLE_CHAR_OPERATORS or char in '><!'


def matchOperator(s: str, position: int) -> str:
    if s[position] in SINGLE_CHAR_OPERATORS:
        return s[position]
    elif s[position] in '><!':
        if position+1 >= len(s) or s[position+1] != '=':
            return s[position]
        # >=, <=, !=
        return s[position:position+2]
    return None

def tokenize(query: str) -> List[str]:
    """ Tokenizes a query string into a list of words. """
    # First let's segment the query into words. 
    ptr = 0
    tokens = []
    while ptr < len(query):
        # Skip whitespaces
        if query[ptr].isspace():
            ptr += 1
        # Check if the current character is a letter
        elif query[ptr].isalpha():
            start = ptr
            while ptr < len(query) and query[ptr].isalnum():  # Notice here alnum is needed
                ptr += 1
            segment = query[start:ptr]
            tokens.append(Token(segment))
        # Check if the current character is a number
        # This does not handle special cases like hex (0x62af), negative numbers and floats yet.
        elif query[ptr].isdigit():
            start = ptr
            while ptr < len(query) and (query[ptr].isdigit() or query[ptr] in '.abcdefABCDEFx'):
                ptr += 1
            segment = query[start:ptr]
            valid = False
            try:
                int(segment)
                valid = True
            except ValueError:
                pass
            try: 
                int(segment, 16)
                valid = True
            except ValueError:
                pass
            try:
                float(segment)
                valid = True
            except ValueError:
                pass
            if not valid:
                raise ValueError('Invalid number in query: ', segment)
            tokens.append(Token(segment))
        # Check if the current character is a symbol
        # This could be problematic, if we have a multi-character symbol like '!=', '<=', '>=', etc.
        elif isSymbol(query[ptr]):
            segment = matchOperator(query, ptr)
            if not segment:  # This should not happen
                raise ValueError(f'failed to parse query: {query}')
            ptr += len(segment)
            tokens.append(Token(segment))
        else:
            ptr += 1
    return tokens

def test():
    query = "SELECT a.b FROM table WHERE column <= 3.1 and column2 < 0x1a;"
    print(query)
    tokens = tokenize(query)
    print(tokens)
    

if __name__ == '__main__':
    test()
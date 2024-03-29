possible_signs = ('^', '*', '/', '%', '+', '-', "<<", ">>", '&', '|', '(', ')')


def get_polish(expression: list, first: int = 1) -> list:
    if first:
        expression = expression[::-1]

    polish = []
    signs = []

    while expression:
        symbol = expression.pop()
        if symbol.isdecimal():
            polish.append(symbol)
        elif symbol == '(':
            signs.append('(')
        elif symbol == ')':
            c = signs.pop()
            while c != '(':
                polish.append(c)
                c = signs.pop()
        else:
            if not signs:
                signs.append(symbol)
            else:
                previous = signs.pop()
                if possible_signs.index(symbol) > possible_signs.index(previous):
                    polish.append(previous)
                    signs.append(symbol)
                else:
                    signs.append(previous)
                    signs.append(symbol)

    while signs:
        polish.append(signs.pop())

    return polish


if __name__ == '__main__':
    with open("/Users/rustamsalimov/Documents/GitHub/ALGs/to_polish/input.txt", "r") as input:
        string = input.readline()

    expression = string.split()

    print(get_polish(expression))

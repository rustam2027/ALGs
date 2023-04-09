possible_signs = ('^', '*', '/', '%', '+', '-', "<<", ">>", '&', '|')


def find_next_valid_index(array: list) -> int:
    counter = 1
    for i in range(len(array) - 1, -1, -1):
        if array[i] == '(':
            counter += 1
        elif array[i] == ')':
            counter -= 1
        if not counter:
            return i
    return -1


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
            polish += get_polish(expression[find_next_valid_index(expression) + 1:], 0)
            expression = expression[:find_next_valid_index(expression) + 1]
        elif symbol != ')':
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

from utils import read, write


def removing_brackets(s):
    remove = set()
    stack = []
    for i, char in enumerate(s):
        if char in '([{':
            stack.append((char, i))
        elif char in ')]}':
            if stack and ((char == ')' and stack[-1][0] == '(') or (char == ']' and stack[-1][0] == '[') or (char == '}' and stack[-1][0] == '{')):
                stack.pop()
            else:
                remove.add(i)
    for _, i in stack:
        remove.add(i)
    return ''.join(char for i, char in enumerate(s) if i not in remove)


def main():
    input_data, = read(type_convert=str)
    brackets = input_data[0]
    write(end='')
    write(removing_brackets(brackets), to_end=True)


if __name__ == '__main__':
    main()

from utils import read, write


def tree_height(data):
    n = data[0][0]

    if n == 0:
        return 0

    left = [-1] * n
    right = [-1] * n
    is_child = [False] * n

    for i in range(n):
        _, l, r = data[i+1]
        if l != 0:
            left_child = l - 1
            left[i] = left_child
            is_child[left_child] = True
        if r != 0:
            right_child = r - 1
            right[i] = right_child
            is_child[right_child] = True

    root = -1
    for i in range(n):
        if not is_child[i]:
            root = i
            break

    max_height = 0
    stack = [(root, 1)]

    while stack:
        node, height = stack.pop()
        if height > max_height:
            max_height = height

        if left[node] != -1:
            stack.append((left[node], height + 1))
        if right[node] != -1:
            stack.append((right[node], height + 1))

    return max_height


def main():
    data = [list(line) for line in read(type_convert=int)]
    write(end='')
    write(tree_height(data), to_end=True)


if __name__ == "__main__":
    main()

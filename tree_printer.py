tree_value = int(input('Enter the length of the Tree: '))


def xtree(lines):
    n = lines

    for outer in range(1, n+1):
        for space in range(1, (n+1)-outer):
            print(" ", end="")
        for inner in range(1, outer+1):
            print(inner, end=" ")
        print(" ")


xtree(tree_value)
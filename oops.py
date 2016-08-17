def printTree(node):
    currentLevel = []
    toPrint = []
    nextLevel = []
    currentLevel.append(node)
    while len(currentLevel) > 0:
        node = currentLevel.pop(0)
        toPrint.append(node.value)

        if node.left is not None:
            nextLevel.append(node.left)
            # toPrint.append(node.left.value)
        if node.right is not None:
            nextLevel.append(node.right)
            # toPrint.append(node.right.value)
        if len(currentLevel) == 0:
            currentLevel = nextLevel
            for item in toPrint:
                print(item, end="")
            toPrint = []
            print()

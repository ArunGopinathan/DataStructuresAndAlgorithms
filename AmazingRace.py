numTests = int(input())

for t in range(numTests):
    numCars = int(input())
    heights = [int(heightIn) for heightIn in input().split()]
    winner = 0
    maxScore = 0
    for pos in range(numCars):
        sees = 0
        # maxHeight = 0
        for viewPos in range(pos - 1, -1, -1):
            if heights[viewPos] >= heights[pos]:
                sees += 1
                break
            else:
                sees += 1
                # maxHeight = heights[viewPos]
        # maxHeight = 0
        for viewPos in range(pos + 1, numCars):
            if heights[viewPos] >= heights[pos]:
                sees += 1
                break
            else:
                sees += 1
                # maxHeight = heights[viewPos]

        if sees * (pos + 1) > maxScore:
            maxScore = sees * (pos + 1)
            winner = pos
    print(winner + 1)
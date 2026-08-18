for y in range(5):
    for x in range(5):
        if x >= 4:
            color = "brown"
        elif y == 0 and x >= 3:
            color = "brown"
        elif (y == 1 and x == 0) or (y == 4 and x == 0):
            color = "white"
        elif (x >= 2 and y >= 1) or (x >= 1 and y >= 3):
            color = "red"
        else:
            color = "purple"

        pydle(x, y, "", color)

grid = ['wbbbw', 'oryro', 'wrrrw', 'wwzww', 'wwzww']
# Added 'y': 'yellow' to the dictionary
colors = {'w': 'white', 'b': 'blue', 'z': 'black', 'r': 'red', 'o': 'orange', 'y': 'yellow'}








for x in range(5):
    for y in range(5):
        pydle(x,y,'',colors[grid[y][x]])

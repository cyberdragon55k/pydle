grid = [
    "wbwgw",
    "rrbrr",
    "rrrrr",
    "rrrrr",
    "wrrrw"]
colors = {'w': 'white', 'b': 'brown', 'g': 'green', 'r': 'red'}
for y in range(5):
    for x in range(5):
        pydle(x, y, "", colors[grid[y][x]])

colors = {'w': 'white', 'k': 'black', 'r': 'brown'}
grid = [
    "wwwwk",
    "wwwkw",
    "wrrww",
    "rrrww",
    "rrwww"]
for y in range(5):
    for x in range(5):
        bg_color = colors[grid[y][x]]
        if x + y == 4:
            text = "╳" if x == 1 else "╱"
            pydle(x, y, text, bg_color)
        else:
            pydle(x, y, "", bg_color)

grid=['rrrrr','rrwrr','wrrrw','wrrrw','rrrrr']
colors={'r':'red','w':'white'}
for x in range(5):
    for y in range(5):
        text = str(y * 3 + x - 6) if 0 < x < 4 and y > 1 else 'II' if (x, y) == (2, 1) else '_' if y == 1 else ''
        pydle(x,y,text,colors[grid[y][x]])

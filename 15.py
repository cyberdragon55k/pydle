grid=[
    'bbbww',
    'wbbbw',
    'bbrbw',
    'wboor',
    'bboww']
colors={'b':'blue','w':'white','r':'black','o':'orange'}
for x in range(5):
    for y in range(5):
        pydle(x,y,"",colors[grid[y][x]])

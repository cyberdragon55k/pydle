grid=[
    "bbbww",
    "wbwwr",
    "yrrrr",
    "oyrwr",
    "woyww"]
colors={'b':'black','w':'white','y':'yellow','o':'red','r':'brown'}
for y in range(5):
    for x in range(5):
        pydle(x,y,"",colors[grid[y][x]])

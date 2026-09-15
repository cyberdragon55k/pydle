grid=[
    "yywww",
    "yyygg",
    "wyggw",
    "wgggg",
    "wgwgg"]
colors={'w':"white",'y':"yellow",'g':'green'}
for y in range(5):
    for x in range(5):
        pydle(x,y,"",colors[grid[y][x]])

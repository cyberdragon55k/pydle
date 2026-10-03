grid=['wwrrw','wrrrr','wrrrr','wbrrw','bwwww']
colors={'w':'white','r':'red','b':'brown'}
for x in range(5):
    for y in range(5):
        text ='⚪' if (x==3 and y==3) else ''
        pydle(x,y,text,colors[grid[y][x]])
grid=['wwrrw','wrrrr','wrrrr','wbrrw','bwwww']
colors={'w':'white','r':'red','b':'brown'}
for x in range(5):
    for y in range(5):
        text ='⚪' if (x==3 and y==3) else ''
        pydle(x,y,text,colors[grid[y][x]])

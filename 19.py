grid=['wwwwg','wwrrw','wrrrw','wrrww','rrwww']
colors={'w':'white','r':'red','g':'green'}
for x in range(5):
    for y in range(5):
        text='🔥'if (x==3 and y==1) or (x==1 and y==3) else ''
        pydle(x,y,text,colors[grid[y][x]])

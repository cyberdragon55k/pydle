grid=['bywyb','wbybw','wbwbw','wbwbw','bwywb']
colors={'b':'blue','w':'white','y':'yellow'}
for x in range(5):
    for y in range(5):
        text = '⧖' if x==2 and y==2 else ''
        pydle(x,y,text,colors[grid[y][x]])

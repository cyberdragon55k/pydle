grid=['bwwww','wwwww','wwwwb','bvbvb','vbvbb']
colors={'b':'black','v':'blue','w':'white'}
for x in range(5):
    for y in range(5):
        text = '⚡' if y==2 and x in (1,3) else ''
        pydle(x,y,text,colors[grid[y][x]])

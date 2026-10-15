grid =['bbbrb','bbrbb','bwwwb','xxxxx','bwwwb']
colors={'b':'blue','x':'black','w':'white','r':'red'}
for x in range(5):
    for y in range(5):
        text = '🧊' if y==4 and x in (0,4) else ''
        pydle(x,y,text,colors[grid[y][x]])
grid =['bbbrb','bbrbb','bwwwb','xxxxx','bwwwb']
colors={'b':'blue','x':'black','w':'white','r':'red'}
for x in range(5):
    for y in range(5):
        text = '🧊' if y==4 and x in (0,4) else ''
        pydle(x,y,text,colors[grid[y][x]])

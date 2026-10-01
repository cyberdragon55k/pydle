grid=['bbbbb','bwwwb','bwbwb','bwwwb','bwbbb']
colors={'b':'blue','w':'white'}
for x in range(5):
    for y in range(5):
        text = '➔' if(x==2 and y==0) else''
        pydle(x,y,text,colors[grid[y][x]])
grid=['bbbbb','bwwwb','bwbwb','bwwwb','bwbbb']
colors={'b':'blue','w':'white'}
for x in range(5):
    for y in range(5):
        text = '➔' if(x==2 and y==0) else''
        pydle(x,y,text,colors[grid[y][x]])

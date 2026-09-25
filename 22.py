grid=['yyyyy','oyyyo','ooooo','ooooo','bwwwb']
colors={'y':'yellow','o':'orange','w':'white','b':'black'}
for x in range(5):
    for y in range(5):
        text = '🍷' if (x==0 and y==0) else""
        pydle(x,y,text,colors[grid[y][x]])

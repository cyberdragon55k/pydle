grid=['yyyyw','yyyyb','wwwwb','wwbbb','wwxww']
colors={'y':'yellow','x':'black','b':'brown','w':'white'}
for x in range(5):
    for y in range(5):
        pydle(x,y,'',colors[grid[y][x]])

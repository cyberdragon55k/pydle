grid=['orwwb','wrbbb','wrbbb','wwrwr','wwrwr']
colors={'o':'orange','r':'red','b':'black','w':'white'}
for x in range(5):
    for y in range(5):
        text='o' if (x==1 and y==0) else''
        pydle(x,y,text,colors[grid[y][x]])

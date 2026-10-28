g=['wwbww','wwbww','wwbww','wrrrw','rrrrr']
c={'w':'white','r':'red','b':'brown'}
for x in range(5):
    for y in range(5):
        t='🧤' if x==3 and y ==0 else ''
        pydle(x,y,t,c[g[y][x]])
        

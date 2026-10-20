g=['wwwww','wrwrw','wrrrw','wwrww','bbbbb']
c={'w':'white','r':'red','b':'black'}
d={(0,0):'╲',(4,0):'╱',(0,3):'╱',(4,3):'╲'}
for x in range(5):
    for y in range(5):
        pydle(x,y,d.get((x,y),''),c[g[y][x]])

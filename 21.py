g=['bwrwb','wrrrw','wrrrw','bbrbb','bbwbb']
c={'b':'black','r':'brown','w':'white'}
s={(0,0):'w',(1,0):'==',(2,0):'O',(3,0):'==',(4,0):'w',(1,2):'▪️',(3,2):'▪️'}
for x in range(5):
    for y in range(5):
        pydle(x,y,s.get((x,y),""),c[g[y][x]])

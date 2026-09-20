g=['ggggg','grrrg','rbbbr','rbbbr','rbbbr']
c={'g':'green','b':'black','r':'brown'}
s={(2,1):"🚥",(1,2):"🦇",(1,4):"🔺🔺",(3,4):"🔸🔸"}
for x in range(5):
 for y in range(5):
  pydle(x,y,s.get((x,y),""),c[g[y][x]])

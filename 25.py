grid=['byzwr','wwwwr','zwrwr','zwywr','zwbwr']
colors={'b':'blue','w':'white','z':'black','r':'red','y':'yellow'}
for x in range(5):
    for y in range(5):
        text = "7,7,7,,9,,,,,10,1,,5,,🙂,2,,5,,12,3,,5,,13".split(',')[y*5+x]
        pydle(x,y,text,colors[grid[y][x]])
grid=['byzwr','wwwwr','zwrwr','zwywr','zwbwr']
colors={'b':'blue','w':'white','z':'black','r':'red','y':'yellow'}
for x in range(5):
    for y in range(5):
        text = "7,7,7,,9,,,,,10,1,,5,,🙂,2,,5,,12,3,,5,,13".split(',')[y*5+x]
        pydle(x,y,text,colors[grid[y][x]])

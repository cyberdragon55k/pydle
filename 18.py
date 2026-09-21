grid=[
    'brwrb',
    'wbrbw',
    'wyyyw',
    'yyyyy',
    'wyyyw'
]
colors={'b':'blue','r':'red','w':'white','y':'yellow'}

for x in range(5):
    for y in range(5):
        text = "1" if x==2 and y==3 else ""
        pydle(x,y,text,colors[grid[y][x]])

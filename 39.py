g=['wbbbw','wzebw','wwbww','wbezw','wbbbw']
for x in range(5):
  for y in range(5):
    v=g[y][x]
    pydle(x,y,'💤'if v=='z'else'🛌'if v=='e'else'','blue'if v=='b'else'white')

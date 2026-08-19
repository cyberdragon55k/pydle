c={"w":"white","g":"green","b":"blue","y":"yellow","o":"orange","r":"red"}
for x in range(5):
 for y in range(5):
  n = y * 5 + x + 1
  if n in [1,7,10,13,19,23]: pydle(x, y, "😊", "white")
  else: pydle(x, y, str(n), c["wgbyorwgbwgbwgbyorwgbywgb"[n-1]])

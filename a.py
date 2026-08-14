for x in range(5):
    for y in range(5):
        pydle(x, y, "", "orange")
for x in [0, 4]:
    for y in [0, 4]:
        pydle(x, y, "", "blue")
for x in [1, 3]:
    for y in [1, 3]:
        pydle(x, y, "", "yellow")
for x,y in [(1,2),(2,1),(2,2),(2,3),(3,2)]: pydle(x,y,"","black")

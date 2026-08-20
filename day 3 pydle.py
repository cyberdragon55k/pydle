c = {"b":"blue","w":"white","k":"black","y":"yellow"}
grid = ["bbwbb","bwbwb","wbwbw","kykyk","kykyk"]
for y in range(5):
    for x in range(5):
        bg_color = c[grid[y][x]]
        if x == 4 and y == 3:
            pydle(x,y, "o",bg_color)
        else:
            pydle(x,y,"",bg_color)

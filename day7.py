c = {"k": "black", "g": "green", "w": "white", "o": "yellow"}
bg = [
    "kgkww", 
    "ggggg", 
    "gwwwo", 
    "gwoww", 
    "ggggg"
]

for y in range(5):
    for x in range(5):
        pydle(x, y, "", c[bg[y][x]])

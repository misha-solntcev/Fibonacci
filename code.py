x = 1
y = 2
SUM = 0
for i in range(0,10):
    SUM = x + y
    x = y
    y = SUM
    print(SUM)
    
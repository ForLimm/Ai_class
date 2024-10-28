x = [5,5,10,3,2,6,7]
y1=4
y2=2
def search(y):
    for i in range(len(x)):
        if x[i]==y:
            return i
    return 0
print(search(y1))
print(search(y2))
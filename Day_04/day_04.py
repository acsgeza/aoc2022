with open('inputT.txt') as f:
    lines = [line.rstrip() for line in f]

def part_1():
    i=0
    for line in lines:
        a, b = line.split(',')
        f = list(map(int, a.split("-")))
        first = set(list(range(f[0], f[1]+1)))
        g = list(map(int, b.split("-")))
        second =set(list(range(g[0], g[1]+1)))
        if len(first.intersection(second))==len(second) or len(second.intersection(first))==len(first):
            i+=1
    return i

def part_2():
    i=0
    for line in lines:
        a, b = line.split(',')
        f = list(map(int, a.split("-")))
        g = list(map(int, b.split("-")))
        if f[0]>g[0]:
            if g[1]>=f[0]:
                i+=1
        elif f[1]>=g[0]:
            i+=1

    return i
print(part_1())
print(part_2())
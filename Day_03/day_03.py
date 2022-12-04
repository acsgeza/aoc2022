
with open('inputT.txt') as f:
    lines = [line.rstrip() for line in f]

UPPER=ord('a')-ord('A')+26
def part_1():
    sum=0
    for line in lines:
        size=len(line)
        first=set(line[:size//2])
        second=set(line[size//2:])
        inter = first.intersection(second)
        shared=list(inter)
        diff=ord(shared[0])-ord('a')+1
        diff += UPPER if diff < 1 else 0
        sum+=diff
    return sum

def part_2():
    sum=0
    size=len(lines)
    for ind in range(0,size,3):
        first=set(lines[ind])
        second=set(lines[ind+1])
        third=set(lines[ind+2])
        inter = first.intersection(second)
        shared=list(inter.intersection(third))
        diff=ord(shared[0])-ord('a')+1
        diff += UPPER if diff < 1 else 0
        sum+=diff
    return sum

print(part_2())
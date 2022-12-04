

with open('inputT.txt') as f:
    lines = [line.rstrip() for line in f]
def part_01():
    summas = []
    i = 0
    summa = 0
    for line in lines:
        if len(line) == 0:
            summas.append(summa)
            i+=1
            summa = 0
            continue
        summa += int(line)
    summas.sort(reverse=True)
    calories=max(summas)
    return calories

def part_02():
    summas = []
    size=len(lines)
    for i in range(0,size,3):
        summa = 0
        for j in range(i,i+3):
            if j<size and len(lines[j])>0:
                summa += int(lines[j])
        summas.append(summa)
    summas.sort(reverse=True)
    return sum(summas[:3])

print(part_01())
print(part_02())
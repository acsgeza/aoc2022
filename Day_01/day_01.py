
lines = []
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

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
print(calories)

print(sum(summas[:3]))
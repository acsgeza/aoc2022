shape={
    'A':1,
    'B':2,
    'C':3,
    'X':1,
    'Y':2,
    'Z':3,
}
with open('inputT.txt') as f:
    lines = [line.rstrip() for line in f]


def processA(op, my):
    score = scorecalc(op, my)
    return score


def scorecalc(op, my):
    diff = shape[my] - shape[op]
    score = 0
    if diff == 0:
        score = 3 + shape[my]
    elif diff == 1 or diff == -2:
        score = shape[my] + 6
    else:
        score = shape[my]
    return score

LOOSE={'A':'C','B':'A','C':'B'}
WIN={'A':'B','B':'C','C':'A'}

def processB(op, my):
    if my == 'X':
        score =scorecalc(op,LOOSE[op])
    elif my == 'Y':
        score = scorecalc(op,op)
    else:
        score = scorecalc(op,WIN[op])
    return score

scores=0
for line in lines:
    scores+=processB(line[0], line[2])

print(scores)
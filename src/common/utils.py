def GetDifferenceScore(term, choice):
    if len(term) > len(choice) or len(term) == 0:
        return -1
    scores = []
    for i in range(len(term)):
        l = term[i]
        positions = [i for i, letter in enumerate(choice) if letter == l]
        diffScore = 0
        for pos in positions:
            if pos - i < 0 or pos + len(term) - i > len(choice):
                continue
            for j, k in zip(range(pos-i, pos-i+len(term)), range(len(term))):
                if choice[j] != term[k]:
                    diffScore += 1
            scores.append(diffScore)
    return min(scores)
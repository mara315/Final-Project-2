def get_grades(score, best):

    if score >= best - 10:
        return 'A'
    elif score >= best - 20:
        return 'B'
    elif score >= best - 30:
        return 'C'
    elif score >= best - 40:
        return 'D'
    else:
        return 'F'

def calc_avg(scores):
    return sum(scores) / len(scores)

def calc_best(scores):
    return max(scores)

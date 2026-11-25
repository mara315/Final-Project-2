'''
Grade calculations
'''

def get_grades(score, best):

    '''
    Returns a letter grade based on best score.
    '''

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
    '''
    Returns highest score.
    '''

    return sum(scores) / len(scores)

def calc_best(scores):
    '''
    Returns average score.
    '''
    return max(scores)

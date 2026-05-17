# check score range is between 0 and 100
def is_valid_score(score):
    return score >= 0 and score <= 100

def classify_score(score):
    if score >= 85 :
        return "Excellent"
    elif score >= 50 :
        return "Pass"
    else:
        return "failed"

def score_average(math, physics, chemistry):
    average = (math + physics + chemistry) / 3
    return average
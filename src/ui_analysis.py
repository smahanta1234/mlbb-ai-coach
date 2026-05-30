def calculate_draft_score(ally_team, enemy_team):
    score=50

    if len(ally_team)>=3:
        score += 10
    
    if len(enemy_team)>=3:
        score+=5

    return min(score, 100)

def get_draft_verdict(score):
    if score>=80:
        return "Excellend Draft"
    
    if score>=65:
        return "Strong Draft"
    
    if score>=50:
        return "Balanced Draft"
    
    return "Weak Draft"

def detect_win_condition(playstyles):

    if "Split Push" in playstyles:
        return "Apply side lane pressure and force map rotations."

    if "Teamfight" in playstyles:
        return "Force grouped objective fights around Turtle and Lord."

    if "Scaling" in playstyles:
        return "Delay game pace and scale toward late game."

    if "Pickoff" in playstyles:
        return "Control vision and isolate enemy carries."

    return "Play around macro fundamentals and objective control."

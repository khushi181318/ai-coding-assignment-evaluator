def generate_feedback(scores):

    feedback = ""

    if scores["Code Quality"] < 10:
        feedback += "Needs better naming and comments.\n"
    else:
        feedback += "Code readability is good.\n"

    if scores["Logic Depth"] < 10:
        feedback += "Logic is basic. Improve edge case handling.\n"
    else:
        feedback += "Good logical structure.\n"

    if scores["Engineering Signals"] < 10:
        feedback += "Add modular functions and error handling.\n"
    else:
        feedback += "Shows engineering maturity.\n"

    if scores["Total Score"] > 70:
        verdict = "Recommended"
    elif scores["Total Score"] > 50:
        verdict = "Borderline"
    else:
        verdict = "Not Recommended"

    feedback += "\nHiring Verdict: " + verdict

    return feedback

import ast

def analyze_code(code):

    lines = code.split("\n")

    comments = sum(1 for l in lines if "#" in l)
    functions = code.count("def ")
    loops = code.count("for") + code.count("while")
    conditions = code.count("if")
    try_blocks = code.count("try")

    ast.parse(code)

    score_correctness = 40
    score_quality = min(20, comments*2 + functions*4)
    score_logic = min(20, loops*4 + conditions*2)
    score_engineering = min(20, try_blocks*5 + functions*3)

    total = score_correctness + score_quality + score_logic + score_engineering

    return {
        "Correctness": score_correctness,
        "Code Quality": score_quality,
        "Logic Depth": score_logic,
        "Engineering Signals": score_engineering,
        "Total Score": total
    }

from analyzer import analyze_code
from feedback import generate_feedback

print("=== AI Coding Assignment Evaluator ===")
print("Paste candidate code. Type END on new line when done:\n")

lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)

code = "\n".join(lines)

result = analyze_code(code)
feedback = generate_feedback(result)

print("\n--- Evaluation Report ---")
for k,v in result.items():
    print(f"{k}: {v}")

print("\n--- Recruiter Feedback ---")
print(feedback)

# AI Coding Assignment Evaluator

This project is a simple coding assignment evaluator that checks submitted code like a real hiring team.  
Instead of only checking whether the output is correct, it also looks at code quality, logic, and basic engineering practices.

The goal of this project is to simulate how recruiters review code during technical interviews.

---

## What this project does

- Analyzes Python code submitted by a candidate
- Checks code quality (comments, structure, readability)
- Measures logic depth (loops and conditions)
- Looks for basic engineering signals (functions, error handling)
- Gives recruiter-style feedback
- Provides a final hiring verdict

---

## Evaluation Criteria

The code is evaluated on:

- Correctness – 40%
- Code Quality – 20%
- Logic Depth – 20%
- Engineering Signals – 20%

Based on these scores, the system gives a final result:
Recommended / Borderline / Not Recommended.

---

## Technologies Used

- Python
- AST (for basic static code analysis)

---

## Project Files

ai-coding-assignment-evaluator/

app.py -> main file to run the evaluator
analyzer.py -> contains code analysis logic
feedback.py -> generates recruiter feedback
README.md -> project description

---

## How to Run

1. Make sure Python is installed.

2. Open terminal in project folder and run:


3. Paste candidate Python code.

4. Type `END` on a new line and press Enter.

You will see evaluation scores and recruiter-style feedback.

---

## Example Output

Correctness: 40  
Code Quality: 6  
Logic Depth: 4  
Engineering Signals: 8  
Total Score: 58  

Recruiter Feedback:
- Needs better naming and comments  
- Logic is basic. Improve edge case handling  
- Add modular functions and error handling  

Hiring Verdict: Borderline

---

## About the Project

This project focuses on explaining evaluation logic clearly instead of using heavy machine learning.  
It follows a rule-based approach to extract engineering signals and generate meaningful feedback.

Currently it supports Python code, but it can be extended to other languages in future.

---

## Author

Khushi Kumari


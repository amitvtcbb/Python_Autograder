# autograder_prog2.py

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Read input from input2.txt
with open('.autograder/input_output/input2.txt', 'r') as input_file:
    number = int(input_file.readline())

# Check if the student's number is prime
student_output = is_prime(number)

# Read expected output from output2.txt
with open('.autograder/input_output/output2.txt', 'r') as output_file:
    expected_output = bool(int(output_file.readline()))

# Compare student's output with expected output
if student_output == expected_output:
    feedback = "Program 2: Outputs match"
    score = 10
else:
    feedback = "Program 2: Outputs differ"
    score = 0

# Write feedback to feedback2.txt
with open('.autograder/input_output/feedback2.txt', 'w') as feedback_file:
    feedback_file.write(feedback)

# Write score to score2.txt
with open('.autograder/input_output/score2.txt', 'w') as score_file:
    score_file.write(str(score))

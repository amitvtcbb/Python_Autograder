# autograder_prog1.py

def calculate_digit_sum(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum

# Read input from input1.txt
with open('.autograder/input_output/input1.txt', 'r') as input_file:
    number = int(input_file.readline())

# Calculate the student's output
student_output = calculate_digit_sum(number)

# Read expected output from output1.txt
with open('.autograder/input_output/output1.txt', 'r') as output_file:
    expected_output = int(output_file.readline())

# Compare student's output with expected output
if student_output == expected_output:
    feedback = "Program 1: Outputs match"
    score = 10
else:
    feedback = "Program 1: Outputs differ"
    score = 0

# Write feedback and score to feedback1.txt
with open('.autograder/input_output/feedback1.txt', 'w') as feedback_file:
    feedback_file.write(feedback)

# Write score to score1.txt
with open('.autograder/input_output/score1.txt', 'w') as score_file:
    score_file.write(str(score))

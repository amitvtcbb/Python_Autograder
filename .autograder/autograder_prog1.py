def calculate_sum_of_digits(num):
    # Calculate the sum of digits in the number
    sum_of_digits = sum(int(digit) for digit in str(num))
    return sum_of_digits

# Function to generate feedback for program 1
def generate_program1_feedback(expected_output, student_output):
    if expected_output == student_output:
        grade = 100
        feedback = "Congratulations! Your solution for program 1 is correct."
    else:
        grade = 0
        feedback = "Oops! Your solution for program 1 is incorrect. Please check your code."

    feedback += f"\nGrade: {grade}%"
    return feedback

# Read the input number from the input.txt file
with open('Input_Ouput/input1.txt', 'r') as file:
    input_number = int(file.readline().strip())

# Calculate the expected sum of digits for the input number
expected_output = calculate_sum_of_digits(input_number)

# Read the student's output from the output.txt file
with open('Input_Ouput/output1.txt', 'r') as file:
    student_output = int(file.readline().strip())

# Generate feedback for program 1 based on the expected and student's output
feedback = generate_program1_feedback(expected_output, student_output)

# Print the feedback
print(feedback)

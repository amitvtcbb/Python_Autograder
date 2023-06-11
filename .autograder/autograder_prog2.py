def is_prime(num):
    # Check if the number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate feedback for program 2
def generate_program2_feedback(expected_output, student_output):
    if expected_output == student_output:
        grade = 100
        feedback = "Congratulations! Your solution for program 2 is correct."
    else:
        grade = 0
        feedback = "Oops! Your solution for program 2 is incorrect. Please check your code."

    feedback += f"\nGrade: {grade}%"
    return feedback

# Read the input number from the input.txt file
with open('Input_Ouput/input2.txt', 'r') as file:
    input_number = int(file.readline().strip())

# Calculate the expected output for the input number
expected_output = is_prime(input_number)

# Read the student's output from the output.txt file
with open('Input_Ouput/output2.txt', 'r') as file:
    student_output = bool(file.readline().strip())

# Generate feedback for program 2 based on the expected and student's output
feedback = generate_program2_feedback(expected_output, student_output)

# Print the feedback
print(feedback)

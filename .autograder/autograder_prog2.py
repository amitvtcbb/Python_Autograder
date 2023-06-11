import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def autograder():
    # Read input from input.txt file
    with open('input_output/input.txt', 'r') as file:
        number = int(file.read().strip())

    # Execute the student's solution script
    # Assuming the student's solution script is named "student_solution.py"
    exec(open("student_solution.py").read())

    # Check if the number is prime using the student's solution
    student_output = is_prime(number)

    # Compare the student's output with the expected output from output.txt file
    with open('input_output/output.txt', 'r') as file:
        expected_output = bool(file.read().strip())

    # Compare the student's output with the expected output
    if student_output == expected_output:
        score = 100
    else
        score = 0

    # Return the score
    return score

# Call the autograder function
score = autograder()

# Print the score
print("Score:", score)

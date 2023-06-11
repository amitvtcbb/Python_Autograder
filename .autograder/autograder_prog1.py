def autograder():
    # Read input from input.txt file
    with open('Input_Output/input1.txt', 'r') as file:
        number = int(file.read().strip())

    # Execute the student's solution script
    # Assuming the student's solution script is named "student_solution.py"
    exec(open("student_solution.py").read())

    # Calculate the sum of digits using the student's solution
    student_output = calculate_digit_sum(number)

    # Compare the student's output with the expected output from output.txt file
    with open('Input_Output/output1.txt', 'r') as file:
        expected_output = int(file.read().strip())

    # Compare the student's output with the expected output
    if student_output == expected_output:
        score = 100
    else:
        score = 0

    # Return the score
    return score

# Call the autograder function
score = autograder()

# Print the score
print("Score:", score)

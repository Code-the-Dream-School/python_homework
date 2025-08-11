import traceback

#Task 1: Diary

# Wrap the entire logic in a try block to catch any potential exceptions.
try:
    # Open the file 'diary.txt' in append mode ('a').
    # Using 'with' ensures the file is automatically closed, even if an error occurs.
    with open('diary.txt', 'a') as file:
        # Initialize the first prompt text.
        prompt = "What happened today? "
        
        # Start an infinite loop to repeatedly get user input.
        while True:
            # Get a line of input from the user using the current prompt.
            line = input(prompt)
            
            # Check for the special termination line.
            if line == "done for now":
                # Write the termination line to the file.
                diary_file.write(line + '\n')
                # Exit the loop.
                break
            
            # If the user did not enter the termination line, write their input
            # to the file, followed by a newline character.
            diary_file.write(line + '\n')
            
            # Change the prompt for all subsequent inputs.
            prompt = "What else? "

    # The file is automatically closed by the 'with' statement once the block is exited.
    print("Diary entry saved successfully.")

# The except block will catch any non-fatal exception that occurs in the try block.
except Exception as e:
    # Print the specific error message you requested.
    print(f"An exception occurred. The exception name is: {type(e).__name__}")
    
    # Use the traceback module to print the full traceback for debugging.
    # This shows exactly where in the code the error occurred.
    traceback.print_exc()

    

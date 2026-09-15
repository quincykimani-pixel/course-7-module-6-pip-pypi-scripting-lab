from datetime import datetime
import os

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list
 def generate_log(data):
    
    if not isinstance(data, list):
        raise ValueError("data must be a list of strings")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")
    
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
     
    print(f"Log written to {os.path.abspath(filename)}")

    pass
    return filename
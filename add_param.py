import os
import re

# Set the directory where you want to start the search
directory = "/home/nord/git/JPplusShinkansen-speed-cost-fork"

# Define the old and new strings
old_string = r'\* NumberCarsInConsist\(\) \) \* RunningCostFactor\(\);'
new_string = r'* NumberCarsInConsist() * param_A / param_B ) * RunningCostFactor() * param_running_cost;'

# Function to replace text in files
def replace_text_in_file(file_path):
    with open(file_path, 'r') as file:
        file_data = file.read()

    # Use regular expression to replace the target string
    new_data = re.sub(old_string, new_string, file_data)

    # Write the new data back to the file if changes were made
    if new_data != file_data:
        with open(file_path, 'w') as file:
            file.write(new_data)
        print(f"Updated: {file_path}")

# Walk through the directory and subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".pnml"):
            file_path = os.path.join(root, file)
            replace_text_in_file(file_path)


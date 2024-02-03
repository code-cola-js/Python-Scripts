# Import os module
import os

# Define the folder path
folder_path = r"C:\Users\Administrator\Desktop\TD-5th tester图文反馈（设计版）"

# Create an empty list to store the file names
file_names = []

# Loop through the folder and its subfolders
for root, dirs, files in os.walk(folder_path):
    # Loop through the files in each folder
    for file in files:
        # Append the file name to the list
        file_names.append(file)

# Define the output file name
output_file = "file_names.txt"

# Open the output file in write mode
with open(os.path.join(folder_path, output_file), "w") as f:
    # Loop through the file names list
    for name in file_names:
        # Write each file name on a new line
        f.write(name + "\n")

# Print a message to indicate the script is done
print("The script is done. Check the output file in the folder.")

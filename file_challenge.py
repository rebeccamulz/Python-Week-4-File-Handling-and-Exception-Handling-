"""
File Read & Write Challenge 🖋️
Error Handling Lab 🧪
"""

# Ask user for a filename
filename = input("Enter the name of the file to read: ")

try:
    # Try opening the file for reading
    with open(filename, "r") as file:
        content = file.read()
    
    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Success 🎉! Modified content written to {new_filename}")

# Handle errors
except FileNotFoundError:
    print("Error 🚨: File not found. Please check the filename and try again.")
except PermissionError:
    print("Error 🚨: You don’t have permission to read this file.")
except Exception as e:
    print(f"Unexpected error 😢: {e}")

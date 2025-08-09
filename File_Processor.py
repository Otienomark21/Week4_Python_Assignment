import os

def process_file(input_file):
    """
    Reads a file, converts its content to uppercase, and writes it to a new file.
    Includes error handling for file-related issues.

    Args:
        filename (str): The name of the file to be processed.
    """
    try:
        # Check if the file exists before trying to open it
        if not os.path.exists("input.txt"):
            raise FileNotFoundError(f"The file 'input.txt' was not found.")

        # Read the content of the original file
        with open("input.txt", 'r') as file:
            content = file.read()
        
        # Modify the content (convert to uppercase in this case)
        modified_content = content.upper()

        # Create the new filename
        base_name, extension = os.path.splitext("input.txt")
        new_filename = f"{base_name}_modified{extension}"
        
        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"✅ Successfully processed 'input.txt'.")
        print(f"📄 The modified content has been written to '{new_filename}'.")

    except FileNotFoundError as e:
        # Handle the specific case where the file doesn't exist
        print(f"❌ Error: {e}")
    except IOError as e:
        # Handle other file-related I/O errors (e.g., permission issues)
        print(f"❌ An I/O error occurred: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"❌ An unexpected error occurred: {e}")

# --- Main program flow ---
if __name__ == "__main__":
    # Prompt the user for the filename
    user_filename = input("Please enter the name of the file to process: ")
    
    # Call the function to process the file
    process_file(user_filename)


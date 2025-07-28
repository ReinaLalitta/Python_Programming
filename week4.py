def process_file():
    try:
        # Get input filename from user
        input_filename = input("Enter the name of the file to read: ")
        
        # Read the input file
        with open(input_filename, 'r') as file:
            content = file.read()
            
        # Process the content (convert to uppercase as an example)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = input_filename.split('.')[0] + '_modified.txt'
        
        # Write to the output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
            
        print(f"File processed successfully! Modified content written to {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file. It might be a binary file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    process_file()
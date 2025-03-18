import os

def file_to_binary(input_file, output_file):
    """Convert any file to a binary file."""
    try:
        with open(input_file, 'rb') as f:
            binary_data = f.read()
        
        with open(output_file, 'wb') as f:
            f.write(binary_data)
        
        print(f"File '{input_file}' has been converted to binary: '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")

def binary_to_file(input_file, output_file):
    """Convert a binary file back to its original format."""
    try:
        with open(input_file, 'rb') as f:
            original_data = f.read()
        
        with open(output_file, 'wb') as f:
            f.write(original_data)
        
        print(f"Binary file '{input_file}' has been converted back to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("1. Convert file to binary")
    print("2. Convert binary file back to original file")
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        input_file = input("Enter the file to convert to binary: ")
        output_file = input_file + ".bin"
        file_to_binary(input_file, output_file)
    elif choice == '2':
        input_file = input("Enter the binary file to convert back: ")
        output_file = input("Enter the output file name with extension: ")
        binary_to_file(input_file, output_file)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()

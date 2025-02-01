'''
Problem statement:

https://prepare.sh/interview/devops/674e96fc473242bc582e99cc

Linkedin

Safe File Reading in Python

- Implement a Python function that safely reads a file, handling various exceptions, and returns the file's content or an error message.'''

import os, argparse

def safe_file_reading(file_path: str, encoding: str = 'utf-8') -> str:
    
    try:
        
        with open(file_path, 'r', encoding=encoding) as file:
            content= file.read()
        return content
    
    except FileNotFoundError:
        return f"Error: The file '{file_path}' does not exist."
    
    except IsADirectoryError:
        return f"Error: '{file_path}' is a directory, not a file."
    
    except PermissionError:
        return f"Error: Permission denied to read the file {file_path}"
    
    except UnicodeDecodeError:
        return f"Error: the {file_path} contains invalid characters and cannot be 
    decoded using {encoding} encoding."

    except IOError as e:
        return f"Error: Input output error occured while reading '{file_path}': {str(e)}"
        
    except Exception as e:
        return f"Error: An unexpected error occurred while reading '{file_path}': {str(e)}"
    
def main():
    parser = argparse.ArgumentParser(description='Safe File Reading')
    
    parser.add_argument("-f", "--file", type=str, required=True, help="File path in string")
    parser.add_argument("-e", "--encoding", type=str, default='utf-8', help="Encoding type in string")
    
    args = parser.parse_args()
    
    result = safe_file_reading(args.file, args.encoding)
    
    print(result)
    
if __name__=="__main__":
    main()
    
    
# # Example 1: File exists and is readable
# print(safe_file_reading("example.txt"))

# # Example 2: File does not exist
# print(safe_file_reading("nonexistent.txt"))

# # Example 3: Path is a directory
# print(safe_file_reading("/home/user"))

# # Example 4: Permission denied
# print(safe_file_reading("/root/protected.txt"))

# # Example 5: Unicode decode error (binary file)
# print(safe_file_reading("binary_file.bin"))

# # Example 6: Custom encoding
# print(safe_file_reading("example.txt", encoding="latin-1"))
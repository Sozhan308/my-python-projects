# Safe File Reading in Python

## Objective
Implement a Python function that safely reads the content of a file while handling various exceptions that may occur during the file reading process. The function should return the file's content if the operation is successful, or a meaningful error message if an exception occurs.

## Requirements

### Function Signature
```python
def safe_read_file(file_path: str) -> str:
    pass
```
### Function Description

# Input

### Parameters:
- `file_path` (str): The path to the file that needs to be read.

# Output

- If the file is read successfully, return the content of the file as a string.
- If any exception occurs, return a descriptive error message indicating the type of error.

# Error Handling

The function should handle the following exceptions:

- **FileNotFoundError**: The file does not exist at the specified path.
- **PermissionError**: The program does not have the necessary permissions to read the file.
- **IsADirectoryError**: The specified path points to a directory, not a file.
- **UnicodeDecodeError**: The file contains characters that cannot be decoded using the default encoding (e.g., UTF-8).
- **IOError**: Any other I/O-related errors (e.g., disk full, device not ready).
- **Exception**: A catch-all for any other unexpected exceptions.

# Additional Considerations

- Use context managers (`with` statement) to ensure the file is properly closed after reading.
- Assume the file is a text file, and read it using the default encoding (UTF-8).
- Provide clear and user-friendly error messages for each type of exception.


# Example Usage:


### Example 1: File exists and is readable
```python
content = safe_read_file("example.txt")
print(content)  # Output: Content of the file
```

### Example 2: File does not exist
```python
content = safe_read_file("nonexistent.txt")
print(content)  # Output: "Error: The file 'nonexistent.txt' does not exist."
```

### Example 3: Permission denied
```python
content = safe_read_file("/root/protected.txt")
print(content)  # Output: "Error: Permission denied. Cannot read '/root/protected.txt'."
```

### Example 4: Path is a directory
```python
content = safe_read_file("/home/user")
print(content)  # Output: "Error: The path '/home/user' is a directory, not a file."
```

### Example 5: Unicode decode error
```python
content = safe_read_file("binary_file.bin")
print(content)  # Output: "Error: The file 'binary_file.bin' contains invalid characters and cannot be decoded."
```

# Evaluation Criteria

### Correctness
- The function should handle all specified exceptions and return the correct output.

### Readability
- The code should be clean, well-structured, and easy to understand.

### Efficiency
- The function should efficiently read the file and handle errors without unnecessary overhead.

### Robustness
- The function should gracefully handle edge cases and unexpected inputs.

## Bonus (Optional)
- Extend the function to accept an optional encoding parameter, allowing the caller to specify the file's encoding (e.g., utf-8, latin-1).
- Add support for reading binary files by introducing a mode parameter (e.g., 'r' for text, 'rb' for binary).

'''Write a script to list all files and directories in a given directory and their sizes'''

import os, sys, platform
# import psutil

def list_directory_files(directory):
    
    try:
        # Check if the path exists or not
        if not os.path.exists(directory):
            print(f"Error: {directory} is not existing")
            return
           
        # Check if it's a directory  
        if not os.path.isdir(directory):
            print(f"Error: {directory} is not a directory")
            return
            
        # Traversing each item 
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            
            try: 
                # check if it's a file or directory and get size
                if os.path.isfile(file_path):
                    size=os.path.getsize(file_path)
                    print(f"File: {file} \tSize: {size}")
                elif os.path.isdir(file_path):
                    # if it's a directory, we traverse through the whole list of sub-directories and take size of all the files inside it
                    size = sum(os.path.getsize(os.path.join(file_path,f)) for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f)))
                    print(f"Directory: {file} \tSize: {size}")
            except OSError as e:
                print(f"Error: Unable to get the size of '{file}': {e}")
    except Exception as e:
        print(f"An Exception occured {e}")
        
def remove_shell_script_files(directory):
    try:
        # Check if the path exists or not
        if not os.path.exists(directory):
            print(f"Error: {directory} is not existing")
            return
           
        # Check if it's a directory
        if not os.path.isdir(directory):
            print(f"Error: {directory} is not a directory")
            return
        try:
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path) and file_path.endswith('.sh'):
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
        except Exception as e:
            print(f"Error: Unable to remove {file_path}: {e}")               
    except Exception as e:
        print(f"An Exception occured {e}")


def main():
    
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd() # get current working directory as input
    
    list_directory_files(directory)
    remove_shell_script_files(directory)
    
if __name__ == '__main__':
    main()
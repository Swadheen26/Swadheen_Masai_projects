import os

def list_files_and_directories(directory_path):
    try:
        # List files and directories in the specified path
        contents = os.listdir(directory_path)

        print(f"Contents of {directory_path}:")
        for item in contents:
            print(item)

    except FileNotFoundError:
        print("Directory not found.")

def create_directory(directory_path):
    try:
        new_dir_name = input("Enter the name of the new directory: ")
        new_dir_path = os.path.join(directory_path, new_dir_name)
        os.makedirs(new_dir_path)
        print(f"Directory '{new_dir_name}' created successfully.")

    except PermissionError:
        print("Permission denied to create a directory.")
    except FileExistsError:
        print("Directory already exists.")


def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to delete the file.")
    except IOError:
        print("Error: could not delete file " + filename)
    

def rename_file(filename, new_filename):
   
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except PermissionError:
        print("Permission denied to rename the file.")
    except IOError:
        print("Error: could not rename file " + filename)
    
while True:
    print("\nOptions:")
    print("1. List files and directories")
    print("2. Create a directory")
    print("3. Delete a file")
    print("4. Rename a file")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        directory_path = input("Enter a directory path: ")
        list_files_and_directories(directory_path)
    elif choice == '2':
        directory_path = input("Enter a directory path: ")
        create_directory(directory_path)
    elif choice == '3':
        file_path = input("Enter the path of the file to delete: ")
        delete_file(file_path)
    elif choice == '4':
        file_path = input("Enter the path of the file to rename: ")
        new_filename = input("Enter the path of the file to rename: ")
        rename_file(file_path, new_filename)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please select a valid option.")







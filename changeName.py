import os
import sys

def change_names(folder_path, prefix, suffix=None):
    counter = 1

    for filename in sorted(os.listdir(folder_path)):
        if os.path.isfile(os.path.join(folder_path, filename)):
            _, extension = os.path.splitext(filename)
            
            if suffix is not None:
                new_name = f"{prefix}{str(counter).zfill(2)}_{suffix}{extension}"
            else:
                new_name = f"{prefix}{str(counter).zfill(2)}{extension}"
            
            file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_file_path)
            counter += 1

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python3 changeName.py <folder_path> <prefix> [suffix]")
        sys.exit(1)

    folder_path = sys.argv[1]
    prefix = sys.argv[2]
    
    suffix = None
    if len(sys.argv) == 4:
        suffix = sys.argv[3]

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        sys.exit(1)

    change_names(folder_path, prefix, suffix)
    print("File names changed successfully.")

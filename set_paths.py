import os
import sys

def update_path(path_var, path):
    with open(".env", "r") as f:
        lines = f.readlines()
    for line in lines:
        if path_var in line:
            lines[lines.index(line)] = f"{path_var}='{path}'\n"
    with open(".env", "w") as f:
        f.writelines(lines)

def add_path(path_var, path):
    with open(".env", "a") as f:
        f.write(f"{path_var}='{path}'\n")

def set_paths(path_var, temppath):
    if not os.path.isfile('.env'):
        try:
            with open('.env', "w") as f:
                f.write("")  # Create an empty .env file
        except Exception as e:
            print(f"An error occurred while creating the .env file: {e}")
            sys.exit(1)
    try:
        with open(".env", "r") as f:
            lines = f.read()
        if path_var in lines:
            update_path(path_var, temppath)
        else:
            add_path(path_var, temppath)
    except:
        print("An error occurred while updating the path.")
        sys.exit(1)

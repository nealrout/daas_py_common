import os

def generate_tree(path, ignore_folders=None, indent=''):
    if ignore_folders is None:
        ignore_folders = {'.git', '.venv', '__pycache__','build','dist','egg-info'}
    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if item not in ignore_folders:
                print(indent + '├───' + item)
                generate_tree(item_path, ignore_folders, indent + '│   ')
        else:
            print(indent + '│   ' + item)

if __name__ == "__main__":
    generate_tree(r'D:\src\github\daas_py')
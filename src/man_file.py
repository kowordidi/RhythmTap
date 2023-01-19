import os

def dir_path_root() -> str:
    """ root dir (abs) path of project - contains 'src', 'test', 'prj' ... """
    dir_path_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return dir_path_parent



def read_file(file_name):
    file_path = os.path.join(dir_path_root(), "dat", file_name)
    print(f"....trying to read file: {file_path}")
    with open(file_path, encoding="utf-8") as f:
        cts = f.read()
        print(f"file contemts....{cts}")

# ---------------------------------------
if __name__ == "__main__":
    read_file("hey.txt")

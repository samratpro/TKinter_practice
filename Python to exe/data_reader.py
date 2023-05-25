import sys, os
def read_path(relative):
    return os.path.join(os.environ.get("_MEIPASS2",os.path.abspath(".")),relative)

def read_file(path):
    file_path = read_path(path)
    with open(file_path, "r+") as f:
        print(f.read())

if __name__ == "__main__":
    file_name = input('Enter your txt file name that have here : ')
    read_file(file_name+'.txt')
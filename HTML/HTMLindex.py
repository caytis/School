import os

def search_dir(dir):
    """Search curr dir, make list with subdirs and images"""
    lyst = os.scandir(dir)
    names = list(entry.name for entry in lyst if entry.is_dir() or entry.is_file())
    for name in names:
        print(name)

if __name__ == '__main__':
    search_dir("HTML/Pictures")
    pass
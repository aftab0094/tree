import os
import pyperclip

def is_dir(path):
    try:
        with open(path) as f:
            f.close()
        return False
    except:
        return True

def is_child(dirc):
    os.chdir(dirc)
    if os.listdir() != []:
        os.chdir("..")
        return True
    os.chdir("..")
    return False

def get_child(dirc):
    os.chdir(dirc)
    a = os.listdir()
    os.chdir("..")
    return a

def str_length(string):
    a = 0
    for char in string:
        a += 1
    return a

def format_child(dirc):
    # ["child", ...] -> ["   child",...]
    # " " * dirc.length + " --- ".length
    child = get_child(dirc)
    temp_string = (str_length(dirc) + 5) * " "
    print(temp_string)
    for index, path in enumerate(child):
        if index == 0:
            continue
        child[index] = "\n" + temp_string + path
    return child

def print_child(dirc):
    fmt_list = format_child(dirc)
    fmt_string = f"{dirc} --- "
    for index, path in enumerate(fmt_list):
        fmt_string += path
    print(fmt_string)
    return fmt_string

ls_cur = os.listdir()

def main():
    global tree
    tree = ""
    for path in ls_cur:
        if is_dir(path):
            if not is_child(path):
                print(path)
                continue
            tree += "\n" + print_child(path)
        else:
            print(path)
            tree += "\n" + path

if __name__ == "__main__":
    main()
    perm = input("Do you want to copy this to clipboard?(y/n) ")
    if perm == "y":
        pyperclip.copy(tree)

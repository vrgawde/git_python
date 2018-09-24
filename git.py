import sys
import os
import hashlib
fname = input("Enter file name: ")
def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
            return hash_md5.hexdigest()




def init():
    initial_hash = md5(fname)
    print(initial_hash)
    f = open("log.txt", "a+")
    f.write(initial_hash + " - Initial Hash")
    f.write("\n")
    f.close()


def status():
    file_hash = md5(fname)
    with open('log.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        
    if last_line[:32] == file_hash :
        print("All Files are up-to-date. No Changes made")
    else:
        print("Following file have been modified: ")
        print(fname)



def log():
    os.system('cat log.txt')


"""
    if last_hash != hash_of_file:
        f = open("hash.txt", "a+")
        f.write(hash_of_file)
        f.write("\n")
        f.close()
        f = open("hash.txt", "r")
        print(fname)
        print('-' * 40)
        data = f.read()
        print(data)
        f.close()

    else:
        print("No Changes")
"""

def commit():
    file_hash = md5(fname)
    with open('log.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        print(last_line[:32])

    if last_line[:32] == file_hash :
        print("No Changes made to the File")
    else:
        comment = input("Enter new Commit Message: ")
        f = open("log.txt", "a+")
        f.write(file_hash + ' - ' + comment)
        f.write("\n")
        f.close()

if sys.argv[1] == "init":
    init()


if sys.argv[1] == "status":
    status()

if sys.argv[1] == "log":
    log()

if sys.argv[1] == "commit":
    commit()

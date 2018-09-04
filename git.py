import sys
import os
import hashlib

def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
            return hash_md5.hexdigest()




def init():
    global fname 
    fname = input("Enter file Name: ")
    initial_hash = md5(fname)
    print(initial_hash) 
    f = open("log.txt", "a+")
    f.write(initial_hash + " - Initial Hash")
    f.write("\n")
    f.close()


def status():
    pass


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
    pass


def push():
    pass


def pull():
    pass

if sys.argv[1] == "init":
    init()


if sys.argv[1] == "status":
    status()

if sys.argv[1] == "log":
    log()

if sys.argv[1] == "commit":
    commit()

if sys.argv[1] == "push":
    push()

if sys.argv[1] == "pull":
    pull()

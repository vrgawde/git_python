import sys
import os
import hashlib


def status():
    pass


def log():
    fname = "/home/falcon/Desktop/College/CASS/python_git/sample_file.txt"

    def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
            return hash_md5.hexdigest()

    hash_of_file = md5(fname)
    f = open("hash.txt", "r")
    line = f.readlines()
    last_hash = line[-1]
    print(last_hash)
    f.close()
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


def commit():
    pass


def push():
    pass


def pull():
    pass


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

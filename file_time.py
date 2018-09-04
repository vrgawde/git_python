import os


filename = "/home/falcon/Desktop/College/CASS/python_git/sample_file.txt"
statbuf = os.stat(filename)
print("Modification time: {}".format(statbuf.st_mtime))

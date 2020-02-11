# @filename: [m2p2]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources https://www.w3resource.com/python-exercises/os/python-os-exercise-15.php


import os
import sys
import time

def get_info(file_path):
    fd = os.open(file_path, os.O_RDWR)
    info = os.fstat(fd)
    
    last_mod_time = time.ctime(info.st_mtime)

    print("-"*30)

    print (f"file name: {file_path}")
    print (f"file size: {info.st_size} bytes")
    print (f"Inode number: {info.st_ino}")
    print (f"last mod: {last_mod_time}")
    os.close( fd)

if __name__ == '__main__':
    if len(sys.argv) > 1: 
        get_info(sys.argv[1])
    else:
        print("Provide a file or a file path as argument!")
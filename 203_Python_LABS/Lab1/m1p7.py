# @filename: [m1p7]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources https://stackoverflow.com/questions/19103052/python-string-formatting-columns-in-line
# https://stackoverflow.com/questions/421618/python-script-to-list-users-and-groups

import os
import pwd

#print(os.environ())

print("+-----------+---------------------------+")
for p in pwd.getpwall():
    if "/home/" in p[5]:
        print("| {0:<9} | {1:<25} |".format(p[0], p[5]))
print("+-----------+---------------------------+")
# @filename: [m2p5]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources https://linuxhandbook.com/execute-shell-command-python/
# http://man7.org/linux/man-pages/man5/utmp.5.html
# https://docs.python.org/2/library/struct.html
# https://www.geeksforgeeks.org/namedtuple-in-python/
# https://sattia.blogspot.com/2015/05/how-to-monitor-user-login-history-on.html
# https://github.com/dimkr/python2-utmp/blob/master/utmp/reader.py

import collections
import datetime
import struct
from enum import Enum

STRUCT = struct.Struct('hi32s4s32s256shhiii4i20s') #Struct format: defines the size of the struct to be read

#struck unpacks a string according to a given format
#the format is provided as a parameter on the class instance: struct.Struct()
#To represent the Struct utmp we use the format: hi32s4s32s256shhiii4i20s
"""
    The struct is represented in the man (5) utmp like this:
    struct utmp {
        short   ut_type;              /* Type of record */
        pid_t   ut_pid;               /* PID of login process */
        char    ut_line[UT_LINESIZE=32]; /* Device name of tty - "/dev/" */
        .
        .
        .

    And the format chars in the Struct module represents the datatype with character:
        h: short integer
        i: int
        s: char[]
        .
        .
        .

    Therefore: the "utmp struct" format is represented like hi32s... -> (32s means -> char[32])
    (source: https://docs.python.org/2/library/struct.html)
"""


class UtmEnum(Enum):
    empty = 0
    run_lvl = 1
    boot_time = 2
    new_time = 3
    old_time = 4
    init_process = 5
    login_process = 6
    user_process = 7
    dead_process = 8
    accounting = 9

#namedtuple is a dictionary like that can be called by key name
#also after definition lists can be added in the defined format, following the order of Key Name
Utmp = collections.namedtuple('Utmp', ['type', 'pid', 'line', 'id', 'user', 'host', 'exit0', 'exit1', 
                            'session', 'sec', 'usec', 'addr0', 'addr1', 'addr2', 'addr3', 'unused'])


#convert byte string when find it
def convert_string(val):
    if isinstance(val, bytes): #might be just an integer
        return val.rstrip(b'\0').decode() #rstrip is trimming the null characters \0 before decoding byte string 
    return val


utmp_lst = []
def read(buf):
    offset = 0
    while offset < len(buf):
        #STRUCT.unpack: the buffer until reaches the STRUCT size defined it it's constructor
        #map: for each iterable make it call convert_string to validate the string
        #Utmp._make: transform the iterable into the namedtuple
        #.append: Add the namedtuple to a list for be printed later
        utmp_lst.append(Utmp._make(map(convert_string, STRUCT.unpack_from(buf, offset))))
        offset += STRUCT.size


if __name__ == '__main__':
    
    with open("/var/log/wtmp", 'rb') as fd:
        buf = fd.read()
        read(buf)

    headers = "Type of record", "PID", "Terminal Name", "Username", "Device Name", "Hostname", "IP addr", "Time Entry"    
    print("{0:<19} | {1:<4} | {2} | {3} | {4} | {5:<17} | {6} | {7:<4}".format(*headers), end="\n")

    for utmpT in utmp_lst:
        time_entry = datetime.datetime.fromtimestamp(utmpT.sec) + datetime.timedelta(microseconds=utmpT.usec)
        
        print("[{0}] {1:<15}".format(utmpT.type, UtmEnum(utmpT.type).name), end=" | ")
        print("{0:<4}".format(utmpT.pid), end=" | ")
        print("{0:<13}".format(utmpT.id), end=" | ")
        print("{0:<8}".format(utmpT.user), end=" | ")
        print("{0:<11}".format(utmpT.line), end=" | ")
        print("{0:<17}".format(utmpT.host), end=" | ")
        print("{0}.{1}.{2}.{3}".format(utmpT.addr0,utmpT.addr1,utmpT.addr2,utmpT.addr3), end=" | ")
        print("{0}".format(time_entry), end="\n")

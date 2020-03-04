# @filename: [m034p1]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [Linux Process]
# @resources

import os

import pprint
import subprocess
#from file_manager import FileManager
from collections import namedtuple

# class ProcessStat(namedtuple('processStat', ''))

class LinuxProcess(namedtuple('linuxProcess', 'user pid cpu mem vsz rss tty stat start time command')):
    
    def __init__(self):
        pass


def get_processes():
    """
    Parse the output of `ps aux` into a list of dictionaries representing the parsed 
    process information from each row of the output. Keys are mapped to column names,
    parsed from the first line of the process' output.
    :rtype: list[dict]
    :returns: List of dictionaries, each representing a parsed row from the command output
    """
    output = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).stdout.readlines()        
    headers = [h for h in ' '.join(map(convert_string, output[0].strip().split())).split() if h]    
    raw_data = map(lambda s: convert_string(s).strip().split(None, len(headers) - 1), output[1:])
    print(f"headers: {headers}")
    
    return list(raw_data)
    #return [dict(zip(headers, r)) for r in raw_data]


def linux_command(command="ps aux"):
    f = os.popen(command)
    command_output = f.read()
    return command_output


def convert_string(val):
    if isinstance(val, bytes): #only check byte type
        return val.rstrip(b'\0').decode() #rstrip is trimming the null characters \0 before decoding byte string 
    return val


if __name__ == '__main__':
    #linuxProcess = LinuxProcess()
    process = get_processes()
    
    lstLinuxProcess = []
    for p in process:
        lstLinuxProcess.append(LinuxProcess._make(p))

    
    


# @filename: [m034p2]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [Create LinuxProcList Class]
# @resources


fav_properties = [
    'comm',
    'pid',
    'ppid',
    'rss',
    'rsslim',
    'startcode',
    'endcode',
    'startstack',
    'start_data',
    'end_data',
    'start_brk',
    'arg_start',
    'arg_end',
    'env_start',
    'env_end']


import os
import sys
from collections import namedtuple
from helper import Helper

class ProcessStat(namedtuple('processStat', 'pid comm state ppid pgrp session tty_nr tpgid flags' +
                         ' minflt cminflt majflt cmajflt utime stime cutime cstime priority' + 
                         ' nice num_threads itrealvalue starttime vsize rss rsslim startcode' + 
                         ' endcode startstack kstkesp kstkeip signal blocked sigignore sigcatch' + 
                         ' wchan nswap cnswap exit_signal processor rt_priority policy' + 
                         ' delayacct_blkio_ticks guest_time cguest_time start_data end_data' + 
                         ' start_brk arg_start arg_end env_start env_end exit_code')):

    def __init__(self):
        pass


    @property
    def name(self):
        if "(python3)" in self.comm:
            return Helper.linux_command("cat /proc/" + self.pid + "/cmdline")


class LinuxProcess(namedtuple('linuxProcess', 'user pid cpu mem vsz rss tty stat start time command')):
    
    def __init__(self):
        pass


    def get_proc_stat(self):
        try:
            pid_path = os.path.join('/proc', str(self.pid), 'stat')
            with open(pid_path, 'r') as pidfile:
                procStat = pidfile.readline()

                return ProcessStat._make(map(Helper.convert_string, procStat.strip().split())) 
        except IOError as e:
            print('ERROR: %s' % e)
            sys.exit(2)
    
    def get_command_line(self):
        return Helper.linux_command("cat /proc/" + self.pid + "/cmdline")


class LinuxProcList:

    def __init__():
        pass

    @staticmethod
    def proclist():
        all_process = Helper.get_processes()
        all_pids = [LinuxProcess._make(proc).pid for proc in all_process]
        
        return all_pids

    @staticmethod
    def cmdline(pid):
        return Helper.linux_command("cat /proc/" + pid + "/cmdline")

    @staticmethod
    def children(pid):
        children = Helper.linux_command("pgrep -P " + pid)
        return children.strip().split()


# Python code to create child process  
def create_child(): 
    n = os.fork() 
    parent = '0'
    # n greater than 0  means parent process 
    if n > 0: 
        print("Parent process and id is : ", os.getpid()) 
        parent = str(os.getpid())

    # n equals to 0 means child process 
    else: 
        print("Child process and id is : ", os.getpid())

    print(parent)
    test = Helper.linux_command("pgrep -P " + parent)
    
    print("inicio*******")
    print(test.strip().split())
    print("fim*******")

def main():
    pids = LinuxProcList.proclist() #get list of pids running
    print(f"pids: {pids}")
    print("\n")

    cmdline = LinuxProcList.cmdline(pids[0])
    print(f"cmdline: {cmdline}")
    print("\n")

    children = LinuxProcList.children(pids[0])
    print(f"children: {children}")
    print("\n")
    
if __name__ == '__main__':
    main()
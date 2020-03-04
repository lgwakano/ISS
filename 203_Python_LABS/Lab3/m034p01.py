# @filename: [m034p1]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [Linux Process]
# @resources: http://man7.org/linux/man-pages/man5/proc.5.html

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


def calc_or_tx_process():
    #start process like calculator or lxterminal
    proc = None
    try:
        proc = Helper.start_process("gnome-calculator")
    except:
        proc = Helper.start_process("lxterminal")

    return proc


def print_proc_stat(proc_stat):
    class_attrs = [attr for attr in dir(proc_stat) if not attr.startswith("_")]
    class_attrs = [attr for attr in class_attrs if attr in fav_properties]

    max_len = max([len(getattr(proc_stat, attr)) for attr in class_attrs]) #data with max len
    
    for str_attr in class_attrs:
        if str_attr == "comm":
            str_attr = "name"

        attr = getattr(proc_stat, str_attr) #get class attribute by using string attr name
        
        print("{0:>15}: {1:>{width}}".format(str_attr, attr, width=max_len))


def main():
    #current process pid
    current_pid = os.getpid()

    #get list of process running
    process = Helper.get_processes()
    lstLinuxProcess = []
    for p in process:
        lstLinuxProcess.append(LinuxProcess._make(p))

    #grab the process by id
    proc = next((x for x in lstLinuxProcess if x.pid == str(current_pid)), None)
    
    proc_stat = proc.get_proc_stat() #parsed into class proc_stat
    
    print_proc_stat(proc_stat)


if __name__ == '__main__':
    main()
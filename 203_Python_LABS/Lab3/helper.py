import os
import subprocess

class Helper:

    @staticmethod
    def start_process(commandList):
        proc = subprocess.Popen(commandList, stdout=subprocess.PIPE)
        return proc

    @staticmethod
    def get_processes():
        """
        Parse the output of `ps aux` into a list of dictionaries representing the parsed 
        process information from each row of the output. Keys are mapped to column names,
        parsed from the first line of the process' output.
        :rtype: list[dict]
        :returns: List of dictionaries, each representing a parsed row from the command output
        """
        proc = Helper.start_process(['ps', 'aux'])
        output = proc.stdout.readlines()
        headers = [h for h in ' '.join(map(Helper.convert_string, output[0].strip().split())).split() if h]    
        raw_data = map(lambda s: Helper.convert_string(s).strip().split(None, len(headers) - 1), output[1:])
        
        return list(raw_data)
        #return [dict(zip(headers, r)) for r in raw_data]

    @staticmethod
    def linux_command(command="ps aux"):
        f = os.popen(command)
        command_output = f.read()
        return command_output

    @staticmethod
    def convert_string(val):
        if isinstance(val, bytes): #only check byte type
            return val.rstrip(b'\0').decode() #rstrip is trimming the null characters \0 before decoding byte string 
        return val


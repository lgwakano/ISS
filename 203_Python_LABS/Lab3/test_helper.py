from helper import Helper

if __name__ == '__main__':
    process = Helper.get_processes()
    #print(process)

    proc = Helper.start_process(["galculator"])
    print(proc.pid)
    
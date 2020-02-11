# @filename: [m2p4]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources

import sys
import os

def hex_dump(file_path):
    with open(file_path, "rb") as f:
        index = 0
        size = 16
        total_length = 0
        byte = f.read(size)

        while byte:
            hex_bytes = " ".join([f"{b:02x}" for b in byte])
        
            #consider only the readable char on ASCII
            char_bytes = "".join([f"{chr(b)}" if 32 <= b <= 127 else "." for b in byte])
            
            print(f"[{index * 16:08x}]:  {hex_bytes:<{50}}  {char_bytes}") # parameterized width

            total_length += len(char_bytes)
            index += 1
            byte = f.read(size)

        print(f"Total length: {total_length} bytes ({total_length:02x}h)")
        print(f"Total length: {os.path.getsize(file_path)} bytes")
if __name__ == "__main__":
    if len(sys.argv) > 1: 
        hex_dump(sys.argv[1])
    else:
        print("Provide a C file!")
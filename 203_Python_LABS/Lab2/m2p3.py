# @filename: [m2p3]
# @author [Luiz Wakano]
# @course ITSC203
# @create date 2020-01-20 12:30:29
# @details [description]
# @resources https://en.wikipedia.org/wiki/Executable_and_Linkable_Format 
# https://docs.python.org/3/library/struct.html

import sys
import struct

format = {
    1: "x86",
    2: "x64"
}

endian = {
    1: "little",
    2: "big"
}

machine = {
    0x00: "No specific instruction set",
    0x02: "SPARC",
    0x03: "x86",
    0x08: "MIPS",
    0x14: "PowerPC",
    0x16: "S390",
    0x28: "ARM",
    0x2A: "SuperH",
    0x32: "IA-64",
    0x3E: "amd64",
    0xB7: "AArch64",
    0xF3: "RISC-V"
}

if __name__ == '__main__':
    file_path = 'test'
    if len(sys.argv) > 1: 
        file_path = sys.argv[1]    

    with open(file_path, 'rb') as f:
        data = f.read()

        e_magic = struct.unpack('>I', data[0x00:0x00 + 4])[0]
        e_format = struct.unpack('<B', data[0x04:0x04 + 1])[0]
        e_endian = struct.unpack('<B', data[0x05:0x05 + 1])[0]
        e_machine = struct.unpack('<H', data[0x12:0x12 + 2])[0]

    print(f"File: test")
    print(f"Magic: {e_magic} | hex: {hex(e_magic)}")
    print(f"Format: {format[e_format]} bit")
    print(f"Endian: {endian[e_endian]}")
    print(f"Machine: {machine[e_machine]}")

    print("\n" + "*" * 30)
    print(f"e_magic: {e_magic} | hex: {hex(e_magic)}")
    print(f"e_format: {e_format} | hex: {hex(e_format)}")
    print(f"e_endian: {e_endian} | hex: {hex(e_endian)}")
    print(f"e_machine: {e_machine} | hex: {hex(e_machine)}")
    print("*" * 30)
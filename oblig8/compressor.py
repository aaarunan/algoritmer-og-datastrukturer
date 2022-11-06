import lz
import huffman
import sys

i = 1

if len(sys.argv) == 1:
    print("[COMPRESS/DECOMPRESS] INPUT FILE OUTPUT FILE")
    print("[-c compress] [-d decompress]\n")

while i < len(sys.argv) - 2:
    arg = sys.argv[i]
    i += 1
    arg2 = sys.argv[i]
    i += 1
    arg3 = sys.argv[i]
    i+=1
    if arg == "-c":
        print("compressing...")
        lz.compress(arg2, arg3)
        huffman.compress(arg3, arg3)
        print("done.")
    elif arg == "-d":
        print("decompressing...")
        huffman.decompress(arg2, arg3)
        lz.decompress(arg3, arg3)
        print("done.")
    else:
        print("Invalid arguments.")
        print("[-c compress] [-d decompress] ")

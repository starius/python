from mycrc32 import Crc32

def crc32(t):
    return Crc32(t, len(t))

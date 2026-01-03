def get_size(hex_string):
    hex_string = hex_string.lower()
    
    byte0 = hex_string[:2]
    
    if byte0 not in ("fd", "fe", "ff"):
        return int(byte0, 16)
    elif byte0 == "fd":
        byte_count = 2
    elif byte0 == "fe":
        byte_count = 4
    elif byte0 == "ff":
        byte_count = 8
    
    size_bytes = hex_string[2:(byte_count * 2) + 3]
    return int(size_bytes, 16)

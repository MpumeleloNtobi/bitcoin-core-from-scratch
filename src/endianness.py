def reverse(hex_string):
    """
        Reverse the endianness of a hexadecimal string.

        Args:
            hex_string (str): the hexadecimal string to reverse.

        Returns:
            (str): hexadecimal string with reversed endianness.
    """
    return bytes.fromhex(hex_string)[::-1].hex()

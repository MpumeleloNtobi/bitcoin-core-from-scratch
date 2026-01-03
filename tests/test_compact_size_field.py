import sys

# Add the project src directory tp the python search path
sys.path.insert(0, "src")

import compact_size_field 

def test_compact_size_field_1byte():
    assert compact_size_field.get_size("00") == 0
    assert compact_size_field.get_size("FC") == 252
    assert compact_size_field.get_size("fc") == 252

def test_compact_size_field_2bytes():
    assert compact_size_field.get_size("FD0100") == 256 
    assert compact_size_field.get_size("fd0100") == 256
    assert compact_size_field.get_size("FDFFFF") == 65535 
    assert compact_size_field.get_size("fdffff") == 65535

def test_compact_size_field_4bytes():
    assert compact_size_field.get_size("FE00010000") == 65536
    assert compact_size_field.get_size("fe00010000") == 65536
    assert compact_size_field.get_size("FEFFFFFFFF") == 4294967295
    assert compact_size_field.get_size("feffffffff") == 4294967295

def test_compact_size_field_8bytes():
    assert compact_size_field.get_size("FF0000000100000000") == 4294967296
    assert compact_size_field.get_size("ff0000000100000000") == 4294967296
    assert compact_size_field.get_size("FFFFFFFFFFFFFFFFFF") == 18446744073709551615
    assert compact_size_field.get_size("ffffffffffffffffff") == 18446744073709551615

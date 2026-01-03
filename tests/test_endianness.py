import sys

# Add the project src directory tp the python search path
sys.path.insert(0, "src")

import endianness

def test_endianness_1byte():
    assert endianness.reverse("01") == "01"

def test_endianness_multibytes():
    assert endianness.reverse("01000000") == "00000001"
    assert endianness.reverse("c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704") == "0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9"

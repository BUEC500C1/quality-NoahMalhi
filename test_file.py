import arab_to_rom
import sys
import pytest

def test_awnser():
    sys.stdin = 4
    x, y = arab_to_rom.conv_to_rom()
    assert y == "IV"

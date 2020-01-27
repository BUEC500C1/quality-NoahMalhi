import arab_to_rom
import pytest

def test_awnser():
    y = ""
    x, y = arab_to_rom.conv_to_rom(4, y)
    assert y == "IV"

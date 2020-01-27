import arab_to_rom
import pytest

def test_awnser():
    arab_to_rom.input = lambda: '4'
    output = arab_to_rom.conv_to_rom(x, y)
    assert y == "IV"

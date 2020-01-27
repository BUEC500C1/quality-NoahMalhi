import arab_to_rom
import pytest

def test_awnser():
    arab_to_rom.input = lambda: '4'
    x, y = arab_to_rom.conv_to_rom()
    assert y == "IV"

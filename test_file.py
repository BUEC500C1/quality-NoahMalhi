import arab_to_rom
import pytest

def test_num():
    
    arab_to_rom.input = lambda x: 4
    output = arab_to_rom.conv_to_rom()
    assert output == "IV"

    arab_to_rom.input = lambda x: 52
    output = arab_to_rom.conv_to_rom()
    assert output == "LII"

    arab_to_rom.input = lambda x: 1022
    output = arab_to_rom.conv_to_rom()
    assert output == "MXXII"


def test_neg():
    arab_to_rom.input = lambda x: -2
    output = arab_to_rom.conv_to_rom()
    assert output == "-"

def test_upperbound():
    arab_to_rom.input = lambda x: 10000
    output = arab_to_rom.conv_to_rom()
    assert output == "-"

def test_nonint():
    arab_to_rom.input = lambda x: "hello"
    output = arab_to_rom.conv_to_rom()
    assert output == "-"
import arab_to_rom
import pytest

def test_awnser():
    
    arab_to_rom.input = lambda: '4'
    output = arab_to_rom.main()

    assert output == "IV"

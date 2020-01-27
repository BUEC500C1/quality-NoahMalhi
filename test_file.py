import arab_to_rom
import mock
import builtins
import pytest

def test_awnser():
    
    arab_to_rom.input = lamba: '4'
    output = arab_to_rom.main()

    assert output == "IV"

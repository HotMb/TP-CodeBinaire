import pytest

from sem1 import from_string, from_user_input
from sem1.code_binaire import Bit, CodeBinaire


def test_from_string_creates_code_binaire():
    code = from_string(" 1010 ")
    assert code == CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)


def test_from_user_input_uses_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "1001")

    code = from_user_input()
    assert code == CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_0, Bit.BIT_1)


def test_from_string_invalid_character_raises_value_error():
    with pytest.raises(ValueError):
        from_string("10a1")


def test_from_string_empty_raises_value_error():
    with pytest.raises(ValueError):
        from_string("   \n")

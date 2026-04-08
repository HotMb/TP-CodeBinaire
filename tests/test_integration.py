import pytest

from sem1 import from_string, from_user_input
from sem1.code_binaire import Bit, CodeBinaire


class TestIntegrationLectureAndCodeBinaire:
    """Tests d'intégration entre lecture et manipulation de CodeBinaire."""

    def test_read_and_concatenate(self):
        """Lire deux codes et les concaténer."""
        c1 = from_string("101")
        c2 = from_string("011")
        result = c1 + c2
        assert str(result) == "101011"
        assert len(result) == 6

    def test_read_and_modify(self):
        """Lire un code, le modifier et vérifier."""
        code = from_string("1010")
        code.ajouter(Bit.BIT_1)
        assert str(code) == "10101"
        assert len(code) == 5

    def test_read_slice_and_verify(self):
        """Lire un code, le découper et vérifier."""
        code = from_string("11001100")
        sub = code[2:5]
        assert str(sub) == "001"
        assert len(sub) == 3

    def test_read_modify_with_setitem(self):
        """Lire un code et modifier avec l'indexation."""
        code = from_string("1010")
        code[2] = Bit.BIT_0
        assert str(code) == "1000"

    def test_read_multiple_operations_chain(self):
        """Lecture, concaténation, modification et vérification."""
        c1 = from_string("10")
        c2 = from_string("01")
        combined = c1 + c2
        combined.ajouter(Bit.BIT_1)
        assert str(combined) == "10011"
        assert combined == CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_0, Bit.BIT_1, Bit.BIT_1)


class TestIntegrationWithUserInputMock:
    """Tests d'intégration avec entrée utilisateur mockée."""

    def test_user_input_then_concatenate(self, monkeypatch):
        """Récupérer deux entrées utilisateur et les concaténer."""
        inputs = iter(["101", "010"])
        monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

        c1 = from_user_input("Premier: ")
        c2 = from_user_input("Deuxième: ")
        result = c1 + c2
        assert str(result) == "101010"

    def test_user_input_with_error_then_retry(self, monkeypatch):
        """L'utilisateur entre une valeur invalide, puis valide."""
        inputs = iter(["10a1", "1010"])
        
        def mock_input(prompt=""):
            return next(inputs)
        
        monkeypatch.setattr("builtins.input", mock_input)

        # Premier appel échoue
        with pytest.raises(ValueError):
            from_user_input()

        # Deuxième appel réussit
        code = from_user_input()
        assert str(code) == "1010"
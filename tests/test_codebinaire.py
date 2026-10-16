import pytest

from code_binaire import Bit, CodeBinaire, AuMoinsUnBitErreur


def test_egalite():
    c1 = CodeBinaire(Bit.BIT_0)
    c2 = CodeBinaire(Bit.BIT_0)
    assert c1 == c2

    c3 = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    c4 = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    assert c3 == c4
    assert c1 != c3


def test_ajouter():
    c = CodeBinaire(Bit.BIT_0)
    c.ajouter(Bit.BIT_1)
    assert c.bits == (Bit.BIT_0, Bit.BIT_1)
    assert len(c) == 2


def test_getitem_lecture():
    c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)

    assert c[0] == Bit.BIT_0
    assert c[1] == Bit.BIT_1

    sub = c[1:3]
    assert isinstance(sub, CodeBinaire)
    assert sub == CodeBinaire(Bit.BIT_1, Bit.BIT_0)


def test_setitem_ecriture():
    c = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    c[0] = Bit.BIT_1
    assert c == CodeBinaire(Bit.BIT_1, Bit.BIT_1)

    c[0:2] = [Bit.BIT_1, Bit.BIT_1, Bit.BIT_0]
    assert c == CodeBinaire(Bit.BIT_1, Bit.BIT_1, Bit.BIT_0)

    c[0:2] = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    assert c == CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)

    c[0:3] = [Bit.BIT_1]
    assert len(c) == 1
    assert c[0] == Bit.BIT_1


def test_delitem():
    c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0)

    del c[0]
    assert c == CodeBinaire(Bit.BIT_1, Bit.BIT_0)

    c = CodeBinaire(Bit.BIT_0, Bit.BIT_1, Bit.BIT_0, Bit.BIT_1)
    del c[1:3]
    assert c == CodeBinaire(Bit.BIT_0, Bit.BIT_1)


def test_addition_concat():
    c1 = CodeBinaire(Bit.BIT_0)
    c2 = CodeBinaire(Bit.BIT_1)
    res = c1 + c2
    assert res == CodeBinaire(Bit.BIT_0, Bit.BIT_1)

    with pytest.raises(TypeError):
        c1 + "pas un code binaire"


def test_longueur():
    c = CodeBinaire(Bit.BIT_0)
    assert len(c) == 1
    c.ajouter(Bit.BIT_1)
    assert len(c) == 2
    c2 = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    c3 = c + c2
    assert len(c3) == 4


def test_au_moins_un_bit_erreur():
    c = CodeBinaire(Bit.BIT_0)
    with pytest.raises(AuMoinsUnBitErreur):
        del c[0]

    c2 = CodeBinaire(Bit.BIT_1)
    with pytest.raises(AuMoinsUnBitErreur):
        c2[0:1] = []


def test_repr_eval():
    c = CodeBinaire(Bit.BIT_0, Bit.BIT_1)
    c_eval = eval(repr(c))
    assert c_eval == c
    assert repr(c) == "CodeBinaire(Bit.BIT_0, Bit.BIT_1)"


def test_str():
    c = CodeBinaire(Bit.BIT_1, Bit.BIT_0, Bit.BIT_0)
    assert str(c) == "100"
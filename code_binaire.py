from enum import Enum


class AuMoinsUnBitErreur(Exception):
    pass


class Bit(Enum):
    BIT_0 = 0
    BIT_1 = 1

    def __str__(self):
        return str(self.value)


class CodeBinaire:
    def __init__(self, bit, *bits):
        self._bits = (bit,) + bits

    @property
    def bits(self):
        return self._bits

    def ajouter(self, bit):
        self._bits = self._bits + (bit,)

    def __len__(self):
        return len(self._bits)

    def __add__(self, b):
        if not isinstance(b, CodeBinaire):
            raise TypeError(
                f"unsupported operand type(s) for +: 'CodeBinaire' and '{type(b).__name__}'"
            )
        return CodeBinaire(*(self._bits + b._bits))

    def __getitem__(self, i):
        if isinstance(i, slice):
            return CodeBinaire(*self._bits[i])
        return self._bits[i]

    def __setitem__(self, i, b):
        temp = list(self._bits)

        if isinstance(i, slice):
            if isinstance(b, CodeBinaire):
                temp[i] = list(b.bits)
            else:
                temp[i] = list(b)
        else:
            if isinstance(b, CodeBinaire):
                temp[i] = b.bits[0]
            else:
                temp[i] = b

        if len(temp) == 0:
            raise AuMoinsUnBitErreur("Un CodeBinaire doit contenir au moins un bit.")

        self._bits = tuple(temp)

    def __delitem__(self, i):
        temp = list(self._bits)
        del temp[i]
        if len(temp) == 0:
            raise AuMoinsUnBitErreur("Un CodeBinaire doit contenir au moins un bit.")
        self._bits = tuple(temp)

    def __iter__(self):
        return iter(self._bits)

    def __eq__(self, other):
        if not isinstance(other, CodeBinaire):
            return NotImplemented
        return self._bits == other._bits

    def __repr__(self):
        bits_str = ", ".join(f"Bit.{b.name}" for b in self._bits)
        return f"CodeBinaire({bits_str})"

    def __str__(self):
        return "".join(str(b) for b in self._bits)
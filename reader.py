from .code_binaire import Bit, CodeBinaire


def _parse_bits(text: str) -> list[Bit]:
    raw = "".join(ch for ch in text if not ch.isspace())
    if not raw:
        raise ValueError("Le code binaire ne peut pas être vide.")

    bits: list[Bit] = []
    for ch in raw:
        if ch == "0":
            bits.append(Bit.BIT_0)
        elif ch == "1":
            bits.append(Bit.BIT_1)
        else:
            raise ValueError(f"Caractère invalide '{ch}' dans le code binaire.")
    return bits


def from_string(text: str) -> CodeBinaire:
    """Créer un CodeBinaire à partir d'une chaîne de caractères."""
    return CodeBinaire(*_parse_bits(text))


def from_user_input(prompt: str = "Entrez un code binaire: ") -> CodeBinaire:
    """Demander un code binaire à l'utilisateur et créer un CodeBinaire."""
    return from_string(input(prompt))


if __name__ == "__main__":
    code = from_user_input()
    print(code)

class Decoder:

    def __init__(
        self,
        decryption_key: str = "",
        alphabet: str = "",
    ):
        self.decryption_key_to_alphabet = dict(zip(decryption_key, alphabet))

    def _decrypt_character(self, character):
        return self.decryption_key_to_alphabet.get(character, "X")


    def decrypt(self, message):
        decrypted = ""
        for character in message:
            decrypted += self._decrypt_character(character)
        return decrypted

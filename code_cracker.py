def decode(message: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    decryption_key = '!)"(£*%&><@abcdefghijklmno '

    if message == "":
        return ""
    else:
        decoded_message = ""
        for character in message:
            for element in decryption_key:
                if character == element:
                    index = decryption_key.index(character)
                    decoded_message += alphabet[index]
    return decoded_message
        
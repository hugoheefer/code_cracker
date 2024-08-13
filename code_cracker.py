def decode(message_to_decode: str, decryption_key: str = "") -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decryption_key = '!)"(£*%&><@abcdefghijklmno'
    if message_to_decode == "":
        return ""
    else:
        decoded_message = ""
        for character in message_to_decode:
            if character == " ":
                    decoded_message += " "
            for element in decryption_key:
                if character == element:
                    index = decryption_key.index(character)
                    decoded_message += alphabet[index]

        return decoded_message
def decode(message_to_decode: str) -> str:
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
    
def encode(message_to_encode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encryption_key = '!)"(£*%&><@abcdefghijklmno'
    if message_to_encode == "":
        return ""
    else:
        encoded_message = ""
        for character in message_to_encode:
            if character == " ":
                    encoded_message += " "
            for element in alphabet:
                if character == element:
                    index = alphabet.index(character)
                    encoded_message += encryption_key[index]

        return encoded_message
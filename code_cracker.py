def decode_or_encode(message_to_process: str, type: str ="decode") -> str:
    if type == "decode":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        decryption_key = '!)"(£*%&><@abcdefghijklmno'
    elif type == "encode":
        decryption_key = "abcdefghijklmnopqrstuvwxyz"
        alphabet = '!)"(£*%&><@abcdefghijklmno'
    if message_to_process == "":
        return ""
    else:
        decoded_message = ""
        for character in message_to_process:
            if character == " ":
                    decoded_message += " "
            for element in decryption_key:
                if character == element:
                    index = decryption_key.index(character)
                    decoded_message += alphabet[index]

        return decoded_message
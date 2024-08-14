def decode(message: str) -> str:
    if message == "":
        return ""
    else:
        alphabet = "ab"
        decryption_key = "!)"

        decoded_message = ""
        for element in message:
            for character in decryption_key:
                if character == element:
                    index = decryption_key.index(character)
                    decoded_message += alphabet[index]
        
        return decoded_message
        
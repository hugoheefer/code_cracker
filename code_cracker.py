def decode(message_to_decode: str, decryption_key: str = "") -> str:
    alphabet = "ab"
    decryption_key = '!)'
    if message_to_decode == "":
        return ""
    else:
        decoded_message = ""
        for character in message_to_decode:
            for element in decryption_key:
                if character == element:
                    index = message_to_decode.index(character)
                    decoded_message += alphabet[index]
        
        return decoded_message
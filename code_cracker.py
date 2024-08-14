def decode(message: str) -> str:
    if message == "":
        return ""
    else:
        alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        decryption_key = '! ) " ( £ * % & > < @ a b c d e f g h i j k l m n o'
        decoded_message = ""
        for element in message:
            for character in decryption_key:
                if element == character:
                    index = decryption_key.index(character)
                    decoded_message += alphabet[index]
        
        return decoded_message
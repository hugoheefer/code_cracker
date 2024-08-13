def decode_or_encode(message_to_process: str, type: str ="decode") -> str:
    if type == "decode":
        characters_for_input = "abcdefghijklmnopqrstuvwxyz"
        characters_for_output = '!)"(£*%&><@abcdefghijklmno'
    elif type == "encode":
        characters_for_input = '!)"(£*%&><@abcdefghijklmno'
        characters_for_output = "abcdefghijklmnopqrstuvwxyz"
        
    if message_to_process == "":
        return ""
    else:
        processed_message = ""
        for character in message_to_process:
            if character == " ":
                    processed_message += " "
            for element in characters_for_output:
                if character == element:
                    index = characters_for_output.index(character)
                    processed_message += characters_for_input[index]

        return processed_message
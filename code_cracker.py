conversion_data: dict = {'input':["abcdefghijklmnopqrstuvwxyz ", '!)"(£*%&><@abcdefghijklmno '], 
                         'output':['!)"(£*%&><@abcdefghijklmno ', "abcdefghijklmnopqrstuvwxyz "]}
 
def decode_or_encode(message_to_process: str, type: str ="decode") -> str:
    characters_for_input = get_conversion_strings(type)[0]
    characters_for_output = get_conversion_strings(type)[1]
        
    if message_to_process == "":
        return ""
    else:
        processed_message = ""
        for character in message_to_process:
            for element in characters_for_output:
                if character == element:
                    index = characters_for_output.index(character)
                    processed_message += characters_for_input[index]

        return processed_message
    
def get_conversion_strings(type: str) -> list[str]:
    if type == "decode":
        return conversion_data["input"]
    elif type == "encode":
        return conversion_data["output"]

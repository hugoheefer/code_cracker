from code_cracker import decode

def test_an_empty_message_results_in_an_empty_result():
    #given
    message = ""

    #then
    assert decode(message=message) == ""


def test_a_one_character_message_is_decoded_according_to_the_decryption_key():
    #given
    message = "!"

    #then
    assert decode(message=message) == "a"

def test_another_one_character_message_is_decoded_also_according_to_the_decryption_key():
    #given
    message = ")"

    #then
    assert decode(message=message) == "b"

def test_a_two_character_message_is_decoded_according_to_the_decription_key():
    #given
    message = "!)"

    #then
    assert decode(message=message) == "ab"



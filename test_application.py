from code_cracker import decode

def test_an_empty_message_results_in_an_empty_result():
    #given
    message = ""

    #then
    assert decode(message) == ""

def test_a_one_character_message_is_decoded_correctly():
    #given
    message = "!"

    #then
    assert decode(message) == "a"

def test_a_another_one_character_message_is_decoded_correctly():
    #given
    message = ")"

    #then
    assert decode(message) == "b"

def test_a_two_character_message_is_decoded_correctly():
    #given
    message = "!)"

    #then
    assert decode(message) == "ab"

def test_a_multi_character_message_is_decoded_correctly():
    #given
    message = '"d(£'

    #then
    assert decode(message) == "code"






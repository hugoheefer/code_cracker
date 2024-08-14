from code_cracker import decode

def test_an_empty_message_gives_an_empty_decoded_message():
    #given
    message = ""

    #then
    assert decode(message) == ""
 
def test_a_message_with_one_character_is_decoded_correctly():
    #given
    message = "!"

    #then
    assert decode(message) == "a"

def test_a_message_with_two_characters_is_decoded_correctly():
    #given
    message = "!)"

    #then
    assert decode(message) == "ab"

def test_a_message_with_three_characters_in_reverse_order_is_decoded_correctly():
    #given
    message = 'onm'

    #then
    assert decode(message) == "zyx" 
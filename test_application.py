from code_cracker import decode_or_encode

def test_decoding_an_empty_message_results_in_an_empty_decoded_message():
    #given
    a_message = ""
    
    #when

    #then
    assert decode_or_encode(a_message) == ""

def test_a_message_with_only_one_character_is_decoded_correctly():
    #given
    a_message = "!"

    #when

    #then
    assert decode_or_encode(a_message) == "a"    

def test_a_message_with_two_subsequent_characters_is_decoded_correctly():
    #given
    a_message = "!)"

    #when

    #then
    assert decode_or_encode(a_message) == "ab"      

def test_a_message_with_three_subsequent_characters_is_decoded_correctly():
    #given
    a_message = 'mno'

    #when

    #then
    assert decode_or_encode(a_message) == "xyz"     

def test_a_message_with_three_random_characters_is_decoded_correctly():
    #given
    a_message = '&j%'

    #when

    #then
    assert decode_or_encode(a_message) == "hug"

def test_a_message_with_three_words_is_decoded_correctly():
    #given
    a_message = '&j%d &££*£g'

    #when

    #then
    assert decode_or_encode(a_message) == "hugo heefer"

##### encoding

def test_an_empty_message_results_in_an_empty_encoded_message():
    #given
    a_message = ''

    #then
    assert decode_or_encode(a_message, type="encode") == ""

def test_a_message_with_one_character_results_in_a_correct_encoded_message():
    #given
    a_message = 'a'

    #then
    assert decode_or_encode(a_message, type="encode") == "!"


def test_a_message_with_two_characters_results_in_a_correct_encoded_message():
    #given
    a_message = 'hugo heefer'

    #then
    assert decode_or_encode(a_message, type="encode") == "&j%d &££*£g"
from code_cracker import decode

def test_decoding_an_empty_message_results_in_an_empty_decoded_message():
    #given
    a_message = ""
    
    #when

    #then
    assert decode(a_message) == ""

def test_a_message_with_only_one_character_is_decoded_correctly():
    #given
    a_message = "!"

    #when

    #then
    assert decode(a_message) == "a"    

def test_a_message_with_two_subsequent_characters_is_decoded_correctly():
    #given
    a_message = "!)"

    #when

    #then
    assert decode(a_message) == "ab"      

def test_a_message_with_three_subsequent_characters_is_decoded_correctly():
    #given
    a_message = 'mno'

    #when

    #then
    assert decode(a_message) == "xyz"     

def test_a_message_with_three_random_characters_is_decoded_correctly():
    #given
    a_message = '&j%'

    #when

    #then
    assert decode(a_message) == "hug"

def test_a_message_with_three_words_is_decoded_correctly():
    #given
    a_message = '&j%d &££*£g'

    #when

    #then
    assert decode(a_message) == "hugo heefer"
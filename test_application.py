from code_cracker import Decoder
import pytest

# Wat als de decryption key langer is dan het alfabet?
# Wat als een teken in de message niet in de decryption key staat?


@pytest.fixture
def a_decoder():
    return Decoder(
        decryption_key="12",
        alphabet="ab",
    )


def test_an_empty_message_decodes_to_an_empty_result():
    assert Decoder().decrypt("") == ""


def test_an_encryption_key_character_translates_to_decoded_character(a_decoder):
    encrypted_message = "1"
    decrypted_message = "a"
    assert a_decoder.decrypt(encrypted_message) == decrypted_message


def test_a_two_character_message_translates_to_a_two_character_result(a_decoder):
    encrypted_message = "12"
    decrypted_message = "ab"
    assert a_decoder.decrypt(encrypted_message) == decrypted_message

def test_it_replaces_characters_in_the_message_not_in_decryption_key_with_a_capital_X(a_decoder):
    encrypted_message = "3"
    decrypted_message = "X"
    assert a_decoder.decrypt(encrypted_message) == decrypted_message
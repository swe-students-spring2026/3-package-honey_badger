import pytest
from textmodifier.functions import fixed_length_decode, fixed_length_encode


def test_fixed_length_decode_default():
    assert fixed_length_decode('🦭🐈🦭🦭🐈🦭🐈🦭🐈🐈', {'E': '🦭🦭', 'H': '🦭🐈', 'L': '🐈🦭', 'O': '🐈🐈'}) == "HELLO"

def test_fixed_length_decode_empty_text():
    assert fixed_length_decode('', {}) == ""

def test_fixed_length_decode_single_character():
    mapping = {'A': '0'}
    encoded_text = '0000'
    assert fixed_length_decode(encoded_text, mapping) == 'AAAA'

def test_fixed_length_decode_empty_text():
    assert fixed_length_decode("", {'A': '0', 'B': '1'}) == ""

def test_fixed_length_decode_empty_mapping():
    assert fixed_length_decode("0101", {}) == ""


def test_fixed_length_decode_from_encode_function():
    text = "This is the msg to decode!"
    encoded_text, mapping = fixed_length_encode(text)
    assert fixed_length_decode(encoded_text, mapping) == text
    



import pytest 
from src.functions import reverse_text
def test_reversing():
    assert reverse_text("hello")=="olleh"
def test_empty():
    assert reverse_text("")==""
def test_textType():
    with pytest.raises(TypeError,match="Reverse Test Function takes a string as an argument"):
        reverse_text(12345)
def test_whitespaces():
    assert reverse_text(" n a@me !#")=="#! em@a n "
def test_numberString():
    assert reverse_text("12345")=="54321"
def test_palindrome():
    assert reverse_text("abba")=="abba"

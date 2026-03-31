import pytest
from textmodifier.functions import remove_vowels

def test_remove_vowels_keeps_y_default():
    #Assertion 1: 'y' should not be removed when remove_y is False
    assert remove_vowels("happy") == "hppy"

def test_remove_vowels_removes_y_when_true():
    #Assertion 2: 'y' should be removed when remove_y is True
    assert remove_vowels("Yellow puppy", remove_y=True) == "llw ppp"

def test_remove_vowels_raises_type_error_for_non_string_input():
    #Assertion 3: Should raise TypeError when text is not a string
    with pytest.raises(TypeError, match="Text must be a string."):
        remove_vowels(123)

def test_remove_vowels_raises_type_error_for_non_boolean_remove_y():
    #Assertion 4: Should raise TypeError when remove_y is not a boolean
    with pytest.raises(TypeError, match="remove_y must be a boolean."):
        remove_vowels("hello", remove_y="true")
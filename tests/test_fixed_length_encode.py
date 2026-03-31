from textmodifier.functions import fixed_length_encode

def test_fixed_length_encode_default():
    assert fixed_length_encode("HELLO") == "{'E': '00', 'H': '01', 'L': '10', 'O': '11'}\n0100101011"

def test_fixed_length_encode_only_code_true():
    assert fixed_length_encode("HELLO", only_code=True) == "0100101011"

def test_fixed_length_encode_ignore_case_true():
    assert fixed_length_encode("HelLO", ignore_case=True) == "{'E': '00', 'H': '01', 'L': '10', 'O': '11'}\n0100101011"
    
def test_fixed_length_encode_custom_bit_style():
    assert fixed_length_encode("HELLO", bit_style=("🐈", "🦭")) == "{'E': '🦭🦭', 'H': '🦭🐈', 'L': '🐈🦭', 'O': '🐈🐈'}\n🦭🐈🦭🦭🐈🦭🐈🦭🐈🐈"

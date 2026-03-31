import pytest

from textmodifier.functions import block_text


def test_block_text_renders_expected_output():
    expected = "\n".join(
        [
            " ###",
            "#   #",
            "#####",
            "#   #",
            "#   #",
        ]
    )

    assert block_text("A") == expected


def test_block_text_is_case_insensitive():
    assert block_text("ab") == block_text("AB")


def test_block_text_applies_scaling_to_width_and_height():
    expected = "\n".join(
        [
            "  ######",
            "  ######",
            "##      ##",
            "##      ##",
            "##########",
            "##########",
            "##      ##",
            "##      ##",
            "##      ##",
            "##      ##",
        ]
    )

    assert block_text("A", scale=2) == expected


def test_block_text_returns_empty_string_for_empty_input():
    assert block_text("") == ""


@pytest.mark.parametrize(
    ("text", "scale", "expected_message"),
    [
        (123, 1, "Text must be a string."),
        ("A", "2", "Scale must be an integer."),
    ],
)
def test_block_text_raises_type_error_for_invalid_inputs(text, scale, expected_message):
    with pytest.raises(TypeError, match=expected_message):
        block_text(text, scale=scale)


@pytest.mark.parametrize(
    ("text", "scale", "expected_message"),
    [
        ("A", 0, "Scale must be at least 1."),
        ("@", 1, "Character '@' is not supported in block font."),
    ],
)
def test_block_text_raises_value_error_for_invalid_values(text, scale, expected_message):
    with pytest.raises(ValueError, match=expected_message):
        block_text(text, scale=scale)

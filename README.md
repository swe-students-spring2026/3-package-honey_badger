[![CI](https://github.com/swe-students-spring2026/3-package-honey_badger/actions/workflows/build.yaml/badge.svg)](https://github.com/swe-students-spring2026/3-package-honey_badger/actions/workflows/build.yaml)

# Text Modifier Package

## Built by

[Minho Eune](https://github.com/minhoeune)

[Alejandro Fiestas](https://github.com/avf8449)

[Diya Greben](https://github.com/diyagreben)

[Rehan Gupta](https://github.com/rehanguptaNYU)

[Ani Guduru](https://github.com/AniGuduru)

## Features
### Block Font

The main function, `block_text(text, scale=1)`, takes a string and returns a block-font version of that text. Input is converted to uppercase before rendering, so lowercase and uppercase letters behave the same.

Supported characters:
- `A-Z`
- `0-9`
- space
- `!`
- `?`
- `.`
- `,`

The `scale` argument increases the size of the rendered output. Larger scale values make each character wider and taller.

#### Example Usage:

```python
from textmodifier import block_text

print(block_text("Hi!"))
# Output:
# #   # #####   #
# #   #   #     #
# #####   #     #
# #   #   #
# #   # #####   #
```

#### Known limitation

Very long input strings or large `scale` values can produce extremely large outputs. Since the function builds the full rendered string in memory before returning it, performance or memory issues may happen for oversized output.

### Fixed Length Encode

The function `fixed_length_encode(text, only_code=False, ignore_case=False, bit_style=("1", "0"))` encodes text into a binary-style string.

Arguments:

- `text` (str): The text to encode.

- `only_code` (bool): If True, returns only the encoded string without the character mapping (default is False).

- `ignore_case` (bool): If True, ignores capitalization (default is False).

- `bit_style` (tuple): Allows custom characters to represent "1" and "0".

#### Example Usage:

```python
from textmodifier import fixed_length_encode

encoded_text, mapping = fixed_length_encode("Hello", False, False,("👾", "🦭"))
print(encoded_text)
# Output: 🦭🦭🦭👾👾🦭👾🦭👾👾
print(mapping)
#Output: {'H': '🦭🦭', 'e': '🦭👾', 'l': '👾🦭', 'o': '👾👾'}

print(fixed_length_encode("Hello World", True))
# Output: 001100101101110000010110111101011
```

### Fixed Length Decode
The function `fixed_length_decode(encoded_text, mapping)` decodes a binary-style text using the provided mapping.

Arguments:
- `encoded_text` (str): The encoded string to decode.
- `mapping` (dict): The dictionary mapping original characters to their codes.

#### Example Usage:
```python 
from textmodifier import fixed_length_decode

encoded_text = "FFFTTFTFTT"
mapping = {'H': 'FF', 'e': 'FT', 'l': 'TF', 'o': 'TT'}
print(fixed_length_decode(encoded_text, mapping))
# Output: "Hello"
```

### Remove Vowels

The function `remove_vowels(text, remove_y=False)` takes a string and returns a new string with all the vowels (a, e, i, o, u) removed. 

Arguments:

- `text` (str): The input text from which to remove vowels.

- `remove_y` (bool): If True, the function will also remove the letters 'y' and 'Y' from the text (default is False).

#### Example Usage:
```python
from textmodifier import remove_vowels

# Default behavior (keeps 'y')
print(remove_vowels("Yellow puppy"))
# Output: "Yllw pppy"

# Modified behavior (removes 'y')
print(remove_vowels("Yellow puppy", remove_y=True))
# Output: "llw ppp"
```

### Reverse Text

The function `reverse_text(text)` takes a string and returns a new string with all the characters in reverse order (left to right).

**Arguments:**
- `text` (str): The string to reverse

#### Behavior

This function works for all characters in a string, including numbers ("5"), letters ("h"), whitespace (" "), and special characters ("!").

#### Example Program

```python
from textmodifier import reverse_text

print(reverse_text("hello"))  # Output: "olleh"
```

## How to run unit tests
Simple unit tests are included within the 'test' directory. This project uses pytest. To run the tests:
1. Install `pytest` into the virtual environment
1. Run the tests from the main project directory: `python3 -m pytest`.
1. Tests should not fail. If the tests fail, it means that the production code is behaving differently from the behavior the tests expect.

## Install and Try the Package
To install the package with `pip`, run:

```bash
pip install honey-badger-text-modifier
```

To install the package with `pipenv`, run:

```bash
pipenv install honey-badger-text-modifier
```

To try the package with the included demo program, run `example.py` from the project root:

```bash
python example.py
```

The demo walks through the package functions and also includes an interactive mode.


## How to calculate code coverage
To check how much of the codebase is covered by unit tests, run:
`python3 -m pytest --cov=.` 


## Continuous integration
This project has a continuous integration workflow that builds and runs unit tests automatically with every _pull request_ of the code to GitHub.

[![CI](https://github.com/swe-students-spring2026/3-package-honey_badger/actions/workflows/build.yaml/badge.svg)](https://github.com/swe-students-spring2026/3-package-honey_badger/actions/workflows/build.yaml)

# Text Modifier Package

## Built by

[Minho Eune](https://github.com/minhoeune)


## Block Font

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

### Known limitation

Very long input strings or large `scale` values can produce extremely large outputs. Since the function builds the full rendered string in memory before returning it, performance or memory issues may happen for oversized output.

## Continuous integration

This project has a continuous integration workflow that builds and runs unit tests automatically with every _push_ of the code to GitHub.

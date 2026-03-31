from textmodifier import *
import ast


def print_divider():
    print("\n" + "=" * 70)


def print_title(title):
    print_divider()
    print(title)
    print_divider()


def demo_block_text():
    print_title("BLOCK TEXT DEMONSTRATION")

    print("Example 1: Basic block text")
    print(block_text("Hi"))

    print("\nExample 2: Larger scale")
    print(block_text("Go", scale=2))

    print("\nExample 3: Word in block font")
    print(block_text("Code"))

    print("\nExample 4: Empty string")
    print(repr(block_text("")))

    print("\nExample 5: Error handling for unsupported character")
    try:
        print(block_text("hi!"))
    except ValueError as e:
        print("Caught ValueError:", e)

    print("\nExample 6: Error handling for invalid scale")
    try:
        print(block_text("Test", scale=0))
    except ValueError as e:
        print("Caught ValueError:", e)

    print("\nExample 7: Error handling for invalid text type")
    try:
        print(block_text(123))
    except TypeError as e:
        print("Caught TypeError:", e)


def demo_remove_vowels():
    print_title("REMOVE VOWELS DEMONSTRATION")

    print("Example 1: Basic vowel removal")
    print(remove_vowels("Hello World"))

    print("\nExample 2: Remove vowels but keep y")
    print(remove_vowels("mystery"))

    print("\nExample 3: Remove vowels including y")
    print(remove_vowels("mystery", remove_y=True))

    print("\nExample 4: Sentence")
    print(remove_vowels("Software engineering is fun!"))

    print("\nExample 5: Empty string")
    print(repr(remove_vowels("")))

    print("\nExample 6: Error handling for invalid text type")
    try:
        print(remove_vowels(42))
    except TypeError as e:
        print("Caught TypeError:", e)

    print("\nExample 7: Error handling for invalid remove_y type")
    try:
        print(remove_vowels("hello", remove_y="yes"))
    except TypeError as e:
        print("Caught TypeError:", e)


def demo_reverse_text():
    print_title("REVERSE TEXT DEMONSTRATION")

    print("Example 1: Basic reverse")
    print(reverse_text("hello"))

    print("\nExample 2: Reverse a phrase")
    print(reverse_text("software engineering"))

    print("\nExample 3: Reverse with punctuation")
    print(reverse_text("Ani!"))

    print("\nExample 4: Reverse empty string")
    print(repr(reverse_text("")))

    print("\nExample 5: Reverse palindrome")
    print(reverse_text("racecar"))

    print("\nExample 6: Error handling for invalid type")
    try:
        print(reverse_text(12345))
    except TypeError as e:
        print("Caught TypeError:", e)


def demo_fixed_length_encode():
    print_title("FIXED LENGTH ENCODE DEMONSTRATION")

    print("Example 1: Default encoding")
    print(fixed_length_encode("hello"))

    print("\nExample 2: Only encoded output")
    print(fixed_length_encode("hello", only_code=True))

    print("\nExample 3: Ignore case")
    print(fixed_length_encode("HeLLo", ignore_case=True))

    print("\nExample 4: Custom bit style")
    print(fixed_length_encode("banana", bit_style=("X", "-")))

    print("\nExample 5: Only code with custom bit style")
    print(fixed_length_encode("data", only_code=True, bit_style=("A", "B")))

    print("\nExample 6: Empty string")
    print(repr(fixed_length_encode("")))


def demo_fixed_length_decode():
    print_title("FIXED LENGTH DECODE DEMONSTRATION")

    print("Example 1: Default decoding")
    mapping = {'e': '00', 'h': '01', 'l': '10', 'o': '11'}
    print(fixed_length_decode('0100101011', mapping))

    print("\nExample 2: Custom bit style decoding")
    mapping_banana = {'a': '--', 'b': '-X', 'n': 'X-'}
    print(fixed_length_decode("-X--X---X---", mapping_banana))

    print("\nExample 3: Single character edge case")
    print(fixed_length_decode('00000', {'a': '0'}))

    print("\nExample 4: From Encode to Decode")
    text = "This is the msg to decode!"
    encoded_text, generated_mapping = fixed_length_encode(text)
    print("Encoded  : " + encoded_text)
    print("Decoded  : " + fixed_length_decode(encoded_text, generated_mapping))


def run_all_demos():
    print_title("TEXTMODIFIER PACKAGE EXAMPLE PROGRAM")
    print("This example program demonstrates the full functionality")
    print("of the textmodifier package.\n")

    demo_block_text()
    demo_remove_vowels()
    demo_reverse_text()
    demo_fixed_length_encode()
    demo_fixed_length_decode()

    print_title("END OF DEMONSTRATION")
    print("All package functions were demonstrated successfully.")


def interactive_menu():
    while True:
        print_title("INTERACTIVE TEXTMODIFIER MENU")
        print("1. Block text")
        print("2. Remove vowels")
        print("3. Reverse text")
        print("4. Fixed length encode")
        print("5. Fixed length decode")
        print("6. Run full demo")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            text = input("Enter text: ")
            scale_input = input("Enter scale (default 1): ").strip()
            scale = 1 if scale_input == "" else int(scale_input)
            try:
                print(block_text(text, scale=scale))
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            text = input("Enter text: ")
            remove_y_input = input("Remove y too? (y/n): ").strip().lower()
            remove_y = remove_y_input == "y"
            try:
                print(remove_vowels(text, remove_y=remove_y))
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            text = input("Enter text: ")
            try:
                print(reverse_text(text))
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            text = input("Enter text: ")
            only_code = input("Only show encoded bits? (y/n): ").strip().lower() == "y"
            ignore_case = input("Ignore case? (y/n): ").strip().lower() == "y"
            try:
                print(
                    fixed_length_encode(
                        text,
                        only_code=only_code,
                        ignore_case=ignore_case,
                    )
                )
            except Exception as e:
                print("Error:", e)

        elif choice == "5":
            text = input("Enter encoded text (bits): ").strip()
            mapping_str = input("Enter mapping dictionary (e.g., {'a': '00', 'b': '01'}): ").strip()
            try:
                mapping = ast.literal_eval(mapping_str)
                print(fixed_length_decode(text, mapping))
            except (SyntaxError, ValueError):
                print("Error: Invalid dictionary format. Please ensure it is like {'key': 'value'}.")
            except Exception as e:
                print("Error:", e)

        elif choice == "6":
            run_all_demos()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    print("Welcome to the textmodifier example program.")
    mode = input("Enter '1' for full demo or '2' for interactive mode: ").strip()

    if mode == "1":
        run_all_demos()
    elif mode == "2":
        interactive_menu()
    else:
        print("Invalid selection. Running full demo by default.")
        run_all_demos()


if __name__ == "__main__":
    main()
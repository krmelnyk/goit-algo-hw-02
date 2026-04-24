from collections import deque


def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Create a deque from the string
    char_deque = deque(s)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


def main():
    input_string = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(input_string):
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is not a palindrome.')


if __name__ == "__main__":
    main()

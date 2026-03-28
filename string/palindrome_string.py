def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome, ignoring case and non-alphanumeric characters.
    """
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the filtered string is equal to its reverse
    return filtered == filtered[::-1]

# Example usage
test_cases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "",
    "No lemon, no melon"
]

for s in test_cases:
    print(f'Input: {s!r} -> Output: {is_palindrome(s)}')

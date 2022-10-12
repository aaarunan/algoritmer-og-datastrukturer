def is_palindrome(n: int, string: str):
    if n < len(string) / 2:
        if string[n] == string[len(string)-n-1]:
            return is_palindrome(n + 1, string)
        return False
    return True


def main():
    print(is_palindrome(0, "hei"))
    print(is_palindrome(0, "redder"))
    print(is_palindrome(0, "hei"))

main()

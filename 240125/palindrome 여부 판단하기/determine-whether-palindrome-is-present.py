def palindrome(str_):
    return "Yes" if str_ == str_[::-1] else "No"

str_ = input()
print(palindrome(str_))
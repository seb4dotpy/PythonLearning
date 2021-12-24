
def palindrome(string):
    return string == string[::-1]

user_word = input('Write a word ')
if user_word.isalpha():
    try:
        print(palindrome(user_word))
    except ValueError:
        print('Only Write words please')

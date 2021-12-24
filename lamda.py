
#Functions without id

palindrome = lambda string: string == string[::-1] #boolean

word = input('write your word')
print(palindrome(word))
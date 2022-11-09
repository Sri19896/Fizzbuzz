def checkio(s):
    if s % 3 == 0 and s % 5 == 0:
        return('Fizz Buzz')
    if s % 3 == 0:
        return('Fizz')
    if s % 5 == 0:
        return('Buzz')
    elif (s % 3 != 0 and s % 5 != 0):
        return(str(s))


print(checkio(7))

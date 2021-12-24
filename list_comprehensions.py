def normalList():
    squares = []
    for i in range(1, 101):  #Fill squares with numbre square in normal form
        squares.append(i**2)
    print('Normal Squares' , squares)


def listComprehensions():
    squares = [i**2 for i in range (1, 101)] #You can add if statement after in range parameters
    print('Squares Comprehensions' , squares)


if __name__ == '__main__':
    normalList()
    listComprehensions()
def normalDict():
    my_dict = {}
    for i in range(1,101):
        my_dict[i] = i**3

    print('Nomal Dict ', my_dict)


def dictComprehensions():
    my_dict = {i: i**3 for i in range(1, 101)} #you can put if statement afte for parameters

    print('Dict Comprehensions' , my_dict) 


if __name__ == '__main__':
    normalDict()
    dictComprehensions()

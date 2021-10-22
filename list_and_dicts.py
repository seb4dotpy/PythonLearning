def main():
    my_list = [1,'Hello', True,4.5]
    my_dict = {'firstname:' 'Sebastian'}

    super_list = [ #list of dicts
        {'firstname': 'Sebastian'},
        {'firstname': 'Catalina'},
        {'firstname': 'Mama'}
    ]

    super_dict = { #dict of lists
        'natural_nums' : [1,2,3,4],
        'integer_nums' : [-1,1,0], 
        'floating_nums' : [1.1,2.2,3.3]
    }
 
    for key, value in super_dict.items():#.items show key and value at same time on a dict
        print(key,'-',value)


    for values in super_list:#show super_list values and keys
        for key, value in values.items():
            print(f'{key} - {value}')


if __name__ == '__main__':
    main()
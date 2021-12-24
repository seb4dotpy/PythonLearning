
# Simple use of files

#open
# with open("./rute/file.txt" , "r") as f: 

def read(): #read file
    numbers = []
    with open('./filetest/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write(): #write file
    names = ['sebastian','catalina','pedro']
    with open('./filetest/names.txt' , 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def main():
    read()
    write()


if __name__ == "__main__":
    main()